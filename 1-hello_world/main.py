from hello_world import print_greeting
import translator

def main():
    try:
        print_greeting()
        #translated_text = translator.get_translation('Hello')
        #print(f"Translated text: {translated_text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()