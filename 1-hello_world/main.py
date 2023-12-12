import sys
import locale

from helpers import set_locale, load_environment_variables
from text import get_greeting, print_greeting
from audio import talk


def main():
    try:
        load_environment_variables()

        current_locale = locale.getlocale()
        language_code = current_locale[0]

        greeting = get_greeting(current_locale)
        print_greeting(greeting)

        talk(language_code, greeting)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        lang = sys.argv[1]
        print("argument: ", lang)
        set_locale(lang, 'UTF-8')

    print("current locale:", locale.getlocale())
    main()