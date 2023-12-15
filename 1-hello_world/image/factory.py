from utils import get_config_service


def get_image_instance(config):

    service = config.get("image_service", "").lower()
    config_service = get_config_service(service)

    if service == "azure":
        from image.services.azure import AzureImageService
        return AzureImageService(config_service)
    #elif translation_service == "openai":
    #    from translator_openai import OpenAITranslator
    #    return OpenAITranslator(config)
    else:
        raise ValueError("Invalid image service specified in the config.")

