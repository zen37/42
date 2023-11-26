import locale

FILE_NAME_GREETINGS = '1-greetings.txt'
ENCODE = 'UTF'

current_locale = locale.getlocale()
print("Current Locale:", current_locale)
language_code = current_locale[0]
encoding = current_locale[1]

""" locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
current_locale = locale.getlocale()
print("Current Locale:", current_locale)
language_code = current_locale[0] """

try:
    with open(FILE_NAME_GREETINGS, 'r') as file:
        lines = file.readlines()

    # Find the matching greeting based on language code
    for line in lines:
        lang_code, greeting = line.strip().split(':')
        if language_code.startswith(lang_code):
            if encoding.startswith(ENCODE):
                print(greeting +  ' ' + '🌍!')
            else:
                print(greeting +  ' ' + 'World!')
            break
    else:
        print(f"No matching greeting found for the detected language: '{language_code}'; using default English")
        print("Hello 🌍!")

except FileNotFoundError:
    print(f"The file '{FILE_NAME_GREETINGS}' does not exist; using default English.")
    print("Hello 🌍!")
except Exception as e:
    print(f"An error occurred: {e}")