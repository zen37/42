import locale

from constants import *
from translator import *


def read_greetings_file(file_name):
    """Read greetings from a file."""
    try:
        with open(file_name, 'r', encoding=ENCODING) as file_greeting:
            return file_greeting.readlines()
    except FileNotFoundError:
        print(f"file '{file_name}' does not exist.")
        return None
    except OSError as e:
        print(f"Error: {e}")


def get_greeting(language_code):
    """Find the matching greeting based on language code."""

    lines = read_greetings_file(FILE_NAME_GREETINGS)

    language_found = False

    for line in lines:
        lang_code, greeting = line.strip().split(':')
        if language_code.startswith(lang_code):
            return greeting
        else:
            continue

    if not language_found:
        print("not found")
        return None


def save_greeting(language_code, greeting_text):
    """Save greetings in a local file."""
    try:
        data_to_save = f"{language_code}:{greeting_text}"

        with open(FILE_NAME_GREETINGS, 'a', encoding=ENCODING) as file_greeting:
            file_greeting.write("\n")
            file_greeting.write(data_to_save)

        print(f"Data appended to {FILE_NAME_GREETINGS}")
    except OSError as e:
        print(f"Error: {e}")


def print_greeting(current_locale):

    language_code = current_locale[0]
    encoding = current_locale[1]

    emoji_supported = True

    if encoding in EMOJI_ENCODINGS:
        greeting_final = GREETING_SECOND_EMOJI + GREETING_PUNCTUATION
    else:
        emoji_supported = False
        print(f"locale encoding '{encoding}' not found; not using emoji")
        greeting_final = GREETING_PUNCTUATION

    result = get_greeting(language_code)
    if result:
        print(result + SEP + greeting_final)
    else:
        if emoji_supported:
                print(f"no greeting found for the locale language '{language_code}'; going to retrieve the translation")
                lang = language_code[:2]
                greeting = get_translation(DEFAULT_GREETING_FIRST, lang)
                if greeting.strip():
                    print(greeting + SEP + greeting_final)
                    #save retrieved translation in the local file
                    save_greeting(lang, greeting)
                else:
                    print(f"translation could not be retrieved for the locale language '{language_code}'; using default English")
                    print(DEFAULT_GREETING_FIRST + SEP + greeting_final)
        else:
            print(f"no greeting found for the locale language '{language_code}' and encoding '{encoding}'; using default English")
            print(DEFAULT_GREETING_FIRST + SEP + greeting_final)