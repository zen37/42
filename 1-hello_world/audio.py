import os
import sys
import json
import azure.cognitiveservices.speech as speechsdk
# https://stackoverflow.com/questions/51464455/how-to-disable-welcome-message-when-importing-pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


from constants import FILE_AUDIO_EXTENSION

with open("config.json", "r", encoding='utf-8') as file:
    config = json.load(file)

REGION = config["region"]
KEY = config["key_speech"]


def talk(language_code, text):

    directory = 'audio'

    # Check if the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    lang = language_code[:2]

    print(lang)

    filename = lang + '.' + FILE_AUDIO_EXTENSION
    filepath = os.path.join(directory, filename)

    print(filepath)


    if os.path.isfile(filepath):

        pygame.init()

        # Load the audio file
        pygame.mixer.music.load(filepath)

        # Play the audio file
        pygame.mixer.music.play()

        # Wait for the audio to finish playing (optional)
        pygame.time.wait(int(pygame.mixer.Sound(filepath).get_length() * 1000))

        # Clean up resources
        pygame.mixer.quit()
        pygame.quit()

    else:

        #speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
        speech_config = speechsdk.SpeechConfig(subscription=KEY, region=REGION)

        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename = filepath)

        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name='en-US-JennyNeural'
        #speech_config.speech_synthesis_voice_name='de-DE-KatjaNeural'
        #speech_config.speech_synthesis_voice_name='es-ES-ElviraNeural'

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            #Pylint did not like it as it's not Pythonic,
            #the code is from Microsoft Learn, not an excuse as for sure I would have not known to do it by myself anyway
            #print("Speech synthesized for text [{}]".format(text))
            print(f"Speech synthesized for [{text}]")
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            #print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            print(f"Speech synthesis canceled: [{cancellation_details.reason}]")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print(f"Speech synthesized for text [{cancellation_details.error_details}]")
                    print("Did you set the speech resource key and region values?")
