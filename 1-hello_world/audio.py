"""
 provides the speech services
"""

import os
import random
import azure.cognitiveservices.speech as speechsdk

#https://stackoverflow.com/questions/51464455/how-to-disable-welcome-message-when-importing-pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from helpers import get_config_service, get_key_speech, log_function_call
from constants import DEFAULT_VOICE, DIRECTORY_AUDIO, ENCODING


def get_available_voices():
    """gets the available voices list as provided by transkaotor service"""
    speech_synthesizer = get_speech_synthesizer()
    # request the list of available voices
    result = speech_synthesizer.get_voices_async().get()
    if result.reason == speechsdk.ResultReason.VoicesListRetrieved:
        print('available voices successfully retrieved')
        return result.voices
    elif result.reason == speechsdk.ResultReason.Canceled:
        print(f"Speech synthesis canceled; error details: {result.error_details}")
        return None


def get_voice(language_code):
    """gets random voice for provided language, in case multiple voices are retrieved"""
    voice_names = []
    voices = get_available_voices()
    for voice in voices:
        #print(voice.__dict__)  #inspect attributes of voice object
        if (voice.locale[:2] == language_code):
            voice_names.append(voice.short_name)

    if voice_names:
        return random.choice(voice_names)
    else:
        return DEFAULT_VOICE


def get_filepath(language_code, filename):
    """gets path to audio file"""
    language_folder = os.path.join(DIRECTORY_AUDIO, language_code)
    os.makedirs(language_folder, exist_ok=True)
    filepath = os.path.join(language_folder, filename)

    return filepath


def play(filepath):
    """play the audio file"""
    pygame.init()

    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing (optional)
    pygame.time.wait(int(pygame.mixer.Sound(filepath).get_length() * 1000))

    # Clean up resources
    pygame.mixer.quit()
    pygame.quit()


def get_audio_file(language_code):
    """gets local audio file based on the provided language"""
    #check if the directory exists
    if not os.path.exists(DIRECTORY_AUDIO):
        os.makedirs(DIRECTORY_AUDIO)
        return None  # just created the directory, obviously there is no file
    else:
        # Get all files that start with language_code
        path = os.path.join(DIRECTORY_AUDIO, language_code)
        if not os.path.exists(path):
            os.makedirs(path)
            return None  # just created the directory, obviously there is no file

        files = [f for f in os.listdir(path) if f.startswith(language_code)]

        print(f"audio files found locally for '{language_code}': {len(files)}")

        for file in files:
            print(file)

        # Return a random file from the list
        if files:
            random_file = random.choice(files)
            print("randomly chosen voice: ", random_file)
            return random_file
        else:
            return None


def get_speech_config(voice=None):

    config = get_config_service("azure")
    REGION = config["region"]
    KEY = get_key_speech()
    print("key:", KEY)

    #speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config = speechsdk.SpeechConfig(subscription=KEY, region=REGION)
    if voice:
        speech_config.speech_synthesis_voice_name = voice

    return speech_config


def get_speech_synthesizer(voice=None, audio_config=None):
    speech_config       = get_speech_config(voice)
    if audio_config:
        speech_synthesizer  = speechsdk.SpeechSynthesizer(speech_config=speech_config , audio_config=audio_config)
    else:
        speech_synthesizer  = speechsdk.SpeechSynthesizer(speech_config=speech_config , audio_config=None)

    return speech_synthesizer


def talk(language_locale, text):
    """speaks the text in the provided language"""

    language_code = language_locale[:2]
    voice = get_audio_file(language_code)

    if voice:
        filepath = get_filepath(language_code, voice)
        play(filepath)
    else:
        voice = get_voice(language_code)
        print("voice: ", voice)
        filepath = get_filepath(language_code, voice)
        print("filepath: ", filepath)
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename = filepath)
        speech_synthesizer = get_speech_synthesizer(voice, audio_config)
        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            #Pylint did not like it as it's not Pythonic,
            #the code is from Microsoft Learn, not an excuse as for sure I would have not known to do it by myself anyway
            #print("Speech synthesized for text [{}]".format(text))
            print(f"speech synthesized for voice [{voice}] and text [{text}]")
            filepath = get_filepath(language_code, voice)
            if os.path.isfile(filepath):
                play(filepath)
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            #print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            print(f"Speech synthesis canceled: [{cancellation_details.reason}]")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print(f"Speech synthesized for text [{cancellation_details.error_details}]")
                    print("Did you set the speech resource key and region values?")
