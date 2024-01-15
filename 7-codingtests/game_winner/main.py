# main.py
from collections import Counter
from constants import ONE, TWO, TIE, VALID, rounds


def valid(input):
    """
    Checks the validity of the provided list of rounds.

    Parameters:
    - rounds (list): A list containing rounds played.

    Returns:
    - bool: True if the rounds are valid, False otherwise.
    """
    if not set(input).issubset(VALID):
        print("There are elements in rounds other than 1 or 2")
        return False

    if not rounds:
        print("The list is empty")
        return False

    return True


def who_won(input):
    """
    Determines the winner based on the provided list of rounds.

    Parameters:
    - rounds (list): A list containing rounds played.

    Returns:
    - str: The winner or "it was a tie" if the game is a tie.
    """
    count = Counter(input)
    game = {ONE: count[1], TWO: count[2]}

    w = max(game, key=game.get)

    if game[ONE] == game[TWO]:
        return TIE
    else:
        return w


if __name__ == "__main__":
    if valid(rounds):
        winner = who_won(rounds)
        print(winner)
