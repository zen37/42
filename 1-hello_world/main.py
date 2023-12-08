import sys

from hello_world import print_greeting

def main(lang):
    try:
        print_greeting(lang)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        lang = sys.argv[1]
        print("Arguments received:", lang)
    else:
        lang = ""
    main(lang)