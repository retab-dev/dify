from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.file.file import File
from dify_plugin.entities.tool import ToolInvokeMessage

class RetabParsingTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        from retab import Retab
        from retab.types.mime import MIMEData
        import base64

        api_key = self.runtime.credentials.get("retab_api_key")
        if not api_key:
            yield self.create_text_message("API key for Retab is required but not provided in credentials.")
            return

        reclient = Retab(api_key=api_key)

        model = tool_parameters.get("model")
        if not model:
            yield self.create_text_message("Model is required but not provided.")
            return
        
        document = tool_parameters.get("document")
        if not document:
            yield self.create_text_message("Document is required but not provided.")
            return
        if not isinstance(document, File):
            yield self.create_text_message("Document must be of type File.")
            return
        
        optional_parameters = {
            "image_resolution_dpi": tool_parameters.get("image_resolution_dpi"),
            "browser_canvas": tool_parameters.get("browser_canvas"),
            "table_parsing_format": tool_parameters.get("table_parsing_format"),
        }
        optional_parameters = {k: v for k, v in optional_parameters.items() if v is not None}

        try:
            result = reclient.documents.parse(
                document=MIMEData(
                    filename=document.filename or "document",
                    url="data:" + (document.mime_type or "octet/stream") + ";base64," + base64.b64encode(document.blob).decode('utf-8'),
                ), # type: ignore[assignment]
                model=model,
                **optional_parameters # type: ignore[call-arg]
            ).model_dump()
        except Exception as e:
            yield self.create_text_message(str(e))
            return
        
        yield self.create_variable_message("pages", result["pages"])
        yield self.create_variable_message("usage", result["usage"])

