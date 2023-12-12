import locale
import os
from dotenv import load_dotenv
import json

from constants import ENCODING, DIR_CONFIG, FILE_COMMON_CONFIG, FILE_AZURE_CONFIG

def set_locale(language, encoding):
    """Set the locale."""
    try:
        locale.setlocale(locale.LC_ALL, f'{language}.{encoding}')
    except Exception as e:
        print(f"Error setting the locale: {e}")
        return None



def get_config():

    config_path = os.path.join(DIR_CONFIG, FILE_COMMON_CONFIG)

    with open(config_path, "r", encoding = ENCODING) as file:
        config = json.load(file)

    return config


def get_config_service(provider):

    file_config = provider + ".json"

    config_path = os.path.join(DIR_CONFIG, file_config )

    with open(config_path, "r", encoding = ENCODING) as file:
        config = json.load(file)

    return config


def load_environment_variables():
    config = get_config()
    service = config.get("translation_service", "").lower()

    secrets_path = os.path.join("env/", service + ".env")
    load_dotenv(dotenv_path=secrets_path )


def get_key_translation():
    key = os.getenv("KEY_TRANSLATION")
    return key

def get_key_speech():
    key = os.getenv("KEY_SPEECH")
    return key