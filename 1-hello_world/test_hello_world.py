import locale

from helpers import set_locale
from text import get_greeting, read_greetings_file, print_greeting
from constants import FILE_NAME_GREETINGS, GREETING_SECOND_EMOJI, SEP

def test_get_greeting():
    lines = read_greetings_file(FILE_NAME_GREETINGS)
    assert lines is not None

    greeting = get_greeting('en_US')
    assert greeting == 'Hello World'

    greeting = get_greeting('es_ES')
    assert greeting == '¡Hola mundo'

    greeting = get_greeting('ro_MD')
    assert greeting == None
    # Add more test cases based on different language codes

def test_print_greeting(capfd):

    current_locale = locale.getlocale()
    print_greeting(current_locale)

    captured = capfd.readouterr()
    # Print the captured output for inspection (optional, for debugging)
    print("Captured Output:", captured.out)

    language_code = current_locale[0]
    greeting =  get_greeting(language_code)
    assert greeting + SEP + GREETING_SECOND_EMOJI in captured.out

def test_print_greeting_other_lang(capfd):

    langs = ["fr_FR", "de_DE", "it_IT", "ja_JP"]
    captured_outputs = []  # List to store captured outputs

    for lang in langs:
        print(f"Captured Output for {lang}:")
        set_locale(lang, 'UTF-8')
        current_locale = locale.getlocale()
        print_greeting(current_locale)

        captured = capfd.readouterr()
        # Print the captured output for inspection (optional, for debugging)
        print(captured.out)

        # Store the captured output in the list
        captured_outputs.append(captured.out)

        language_code = current_locale[0]
        greeting =  get_greeting(language_code)

        assert greeting + SEP + GREETING_SECOND_EMOJI in captured.out