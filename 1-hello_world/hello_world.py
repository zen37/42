import locale
from constants import *

def read_greetings_file(file_name):
    """Read greetings from a file."""
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def find_greeting(lines, language_code):
    """Find the matching greeting based on language code."""

    language_found = False

    for line in lines:
        lang_code, greeting = line.strip().split(':')
        if language_code.startswith(lang_code):
            return greeting
            break
        else:
            continue

    if not language_found:
        return None

def set_locale(language, encoding):
    """Set the locale."""
    try:
        locale.setlocale(locale.LC_ALL, f'{language}.{encoding}')
    except Exception as e:
        print(f"Error setting the locale: {e}")
        return None

def print_greeting():

    # Uncomment the lines below if you want to set the locale to other language for testing
    #set_locale('es_ES', 'UTF-8')
    #set_locale('zh_CN', 'UTF-8')
    #set_locale('ja_JP', 'UTF-8')
    #set_locale('ja_JP', 'SJIS')

    current_locale = locale.getlocale()
    print("Current Locale:", current_locale)
    language_code = current_locale[0]
    encoding = current_locale[1]

    emoji_supported = True

    if encoding in EMOJI_ENCODINGS:
        greeting_final = GREETING_SECOND_EMOJI + GREETING_PUNCTUATION
    else:
        emoji_supported = False
        greeting_final = DEFAULT_GREETING_SECOND + GREETING_PUNCTUATION


    lines = read_greetings_file(FILE_NAME_GREETINGS)

    if lines:
        result = find_greeting(lines, language_code)
        if result:
            if not emoji_supported: print(f"Locale encoding '{encoding}' not found; using default English instead of emoji")
            print(result + SEP + greeting_final)
        else:
            if emoji_supported:
                print(f"No greeting found for the locale language '{language_code}'; using default English")
                print(DEFAULT_GREETING_FIRST + SEP + greeting_final)
            else:
                print(f"No greeting found for the locale language '{language_code}' and encoding '{encoding}'; using default English")
                print(DEFAULT_GREETING_FIRST + SEP + greeting_final)
    else:
        print("Error reading the greetings file.")