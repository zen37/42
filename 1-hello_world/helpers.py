import locale
import os
import json

from constants import ENCODING, DIR_CONFIG, FILE_COMMON_CONFIG, FILE_AZURE_CONFIG

def set_locale(language, encoding):
    """Set the locale."""
    try:
        locale.setlocale(locale.LC_ALL, f'{language}.{encoding}')
    except Exception as e:
        print(f"Error setting the locale: {e}")
        return None


def get_config(provider=None):

    if provider:
        config_path = os.path.join(DIR_CONFIG, FILE_AZURE_CONFIG)
    else:
        config_path = os.path.join(DIR_CONFIG, FILE_COMMON_CONFIG)

    with open(config_path, "r", encoding = ENCODING) as file:
        config = json.load(file)

    return config


def get_secrets(provider):
    """only temporary for ease of testing"""
    secrets_path = os.path.join(".secrets", provider + ".json")
    with open(secrets_path, "r", encoding = ENCODING) as file:
        secrets = json.load(file)
    return secrets