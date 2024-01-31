import sys
import webbrowser

WEBSITE = 'https://www.google.com/maps/place/'

if __name__ ==  "__main__":
    if len(sys.argv) > 1:
        input = ' '.join(sys.argv[1:])
        print("input: ", input)

        webbrowser.open( WEBSITE + input)