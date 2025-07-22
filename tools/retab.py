from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.file.file import File
from dify_plugin.entities.tool import ToolInvokeMessage

class RetabTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        from retab import Retab
        from retab.types.mime import MIMEData
        import base64

        api_key = self.runtime.credentials.get("retab_api_key")
        if not api_key:
            yield self.create_text_message("API key for Retab is required but not provided in credentials.")
            return

        reclient = Retab(api_key=api_key)
    
        project_id = tool_parameters.get("project_id")
        if not project_id:
            yield self.create_text_message("project_id is required but not provided.")
            return
    
        iteration_id = tool_parameters.get("iteration_id")
        if not iteration_id:
            yield self.create_text_message("iteration_id is required but not provided.")
            return
        
        documents = tool_parameters.get("documents")
        if not documents:
            yield self.create_text_message("Documents is required but not provided.")
            return
        if not isinstance(documents, list):
            yield self.create_text_message("Documents must be of type List.")
            return
        if not all(isinstance(doc, File) for doc in documents):
            yield self.create_text_message("All documents must be of type File.")
            return

        optional_parameters = {
            "temperature": tool_parameters.get("temperature"),
            "seed": tool_parameters.get("seed"),
        }
        optional_parameters = {k: v for k, v in optional_parameters.items() if v is not None}

        try:
            result = reclient.deployments.extract(
                project_id=project_id,
                iteration_id=iteration_id,
                documents=[MIMEData(
                    filename=document.filename or "document",
                    url="data:" + (document.mime_type or "octet/stream") + ";base64," + base64.b64encode(document.blob).decode('utf-8'),
                ) for document in documents], # type: ignore[assignment]
                store=False,
                **optional_parameters # type: ignore[call-arg]
            ).model_dump()
        except Exception as e:
            yield self.create_text_message(str(e))
            return
        
        yield self.create_variable_message("choices", result["choices"])
        yield self.create_variable_message("likelihoods", result["likelihoods"])

