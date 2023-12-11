"""
import os
provides functionality related to the operating system,
including file and directory operations using the os module

import pygame
https://stackoverflow.com/questions/51464455/how-to-disable-welcome-message-when-importing-pygame
"""

import os
import json
import random
import azure.cognitiveservices.speech as speechsdk
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from constants import DEFAULT_VOICE, DIRECTORY_AUDIO, ENCODING


with open("config.json", "r", encoding = ENCODING) as file:
    config = json.load(file)

REGION = config["region"]
KEY = config["key_speech"]

#speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
speech_config = speechsdk.SpeechConfig(subscription=KEY, region=REGION)

def get_available_voices():
    """gets the available voices list"""
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config , audio_config=None)

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
            #print(voice.short_name)
            voice_names.append(voice.short_name)

    if voice_names:
        return random.choice(voice_names)
    else:
        return DEFAULT_VOICE


def get_filepath(voice):
    """gets path to audio file"""

    filename = voice
    filepath = os.path.join(DIRECTORY_AUDIO, filename)

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
 # Check if the directory exists
    if not os.path.exists(DIRECTORY_AUDIO):
        os.makedirs(DIRECTORY_AUDIO)
        return None  # just created the directory, obviously there is no file
    else:
        # Get all files that start with language_code
        files = [f for f in os.listdir(DIRECTORY_AUDIO) if f.startswith(language_code)]

        print(f"audio files (voices) found locally: {len(files)}")

        for file in files:
            print(file)

        # Return a random file from the list
        if files:
            random_file = random.choice(files)
            print("randomly chosen voice: ", random_file)
            return random_file
        else:
            return None


def talk(language_locale, text):
    """speaks the text in the provided language"""

    language_code = language_locale[:2]

    voice = get_audio_file(language_code)

    if voice:
        filepath = get_filepath(voice)
        play(filepath)
    else:
        voice = get_voice(language_code)

        filepath = get_filepath(voice)

        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename = filepath)

        speech_config.speech_synthesis_voice_name=voice

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            #Pylint did not like it as it's not Pythonic,
            #the code is from Microsoft Learn, not an excuse as for sure I would have not known to do it by myself anyway
            #print("Speech synthesized for text [{}]".format(text))
            print(f"speech synthesized for voice [{voice}] and text [{text}]")
            filepath = get_filepath(voice)
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
