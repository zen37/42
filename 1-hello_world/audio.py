from helpers import get_config
from speech.factory import get_speech_service


def talk(language_code, text):

    config = get_config()
    speech = get_speech_service(config)
    speech.talk(language_code, text)