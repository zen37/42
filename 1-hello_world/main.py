import sys
import locale

from text import print_greeting
from speech import talk


def set_locale(language, encoding):
    """Set the locale."""
    try:
        locale.setlocale(locale.LC_ALL, f'{language}.{encoding}')
    except Exception as e:
        print(f"Error setting the locale: {e}")
        return None

def main(current_locale):
    try:
        print_greeting(current_locale)
        #print("Enter some text that you want to speak >")
        #text = input()
        talk("hello world")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        lang = sys.argv[1]
        print("argument: ", lang)
        set_locale(lang, 'UTF-8')

    current_locale = locale.getlocale()
    print("current locale:", current_locale)

    main(current_locale)