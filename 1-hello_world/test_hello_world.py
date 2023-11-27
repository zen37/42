import pytest
from hello_world import *
from constants import *

def test_find_greeting():
    lines = read_greetings_file(FILE_NAME_GREETINGS)
    assert lines is not None

    greeting = find_greeting(lines, 'en_US')
    assert greeting == 'Hello'

    greeting = find_greeting(lines, 'es_ES')
    assert greeting == '¡Hola'

    greeting = find_greeting(lines, 'de_DE')
    assert greeting == None
    # Add more test cases based on different language codes

def test_print_greeting(capfd):

    print_greeting()

    # Print the capfd object itself for inspection
    #print("Captured FD object:", capfd)

    captured = capfd.readouterr()
    # Print the captured output for inspection (optional, for debugging)
    print("Captured Output:", captured.out)

    #assert "Current Locale:" in captured.out

    assert '🌍' in captured.out
    # Add more assertions based on your expectations for the printed output