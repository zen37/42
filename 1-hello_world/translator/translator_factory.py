# translator_factory.py

from helpers import get_config

def get_translator_instance(config):
    service = config.get("translation_service", "").lower()

    config = get_config(service)

    if service == "azure":
        from translator.translator_azure import AzureTranslator
        return AzureTranslator(service)
    #elif translation_service == "openai":
    #    from translator_openai import OpenAITranslator
    #    return OpenAITranslator(config)
    else:
        raise ValueError("Invalid translation service specified in the config.")
