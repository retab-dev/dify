from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class RetabProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        api_key = credentials.get("retab_api_key")
        if not api_key:
            raise ToolProviderCredentialValidationError("Retab API Key cannot be empty.")
        
        from retab import Retab
        reclient = Retab(api_key=api_key)
        try:
            reclient.usage.monthly_credits_usage()
        except Exception as e:
            raise ToolProviderCredentialValidationError("Exception occured while validating credentials: " + str(e))
