"""Wordle game"""

__author__ = "703666919"


def contains_char(word: str, lettersearch: str) -> bool:
    """builds emojified and checks the string for a single letter"""
    assert len(lettersearch) == 1, f"len('{lettersearch}') is not 1"
    w: int = 0
    while w < len(word):
        if word[w] == lettersearch:
            return True
        w += 1
    return False


def emojified(word_guess: str, secret_word: str) -> str:
    """checks to see if letters are correct using using the colored boxes in the wordle"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(word_guess) == len(secret_word)
    """Guess must be the same length as secret """
    w: int = 0
    answer: str = ""
    while w < len(secret_word):
        if word_guess[w] == secret_word[w]:
            answer += GREEN_BOX
        elif contains_char(secret_word, word_guess[w]) is True:
            answer += YELLOW_BOX
        else:
            answer += WHITE_BOX
        w += 1
    return answer


def input_guess(N: int) -> str:
    w = input(f"Enter a {N} character word:")
    """allows the user to input a number of characters and tells if word is that amount of characters"""
    while N != len(w):
        w = input(f"That wasn't {N} characters! Try again:")
    return w


def main(secret: str) -> None:
    """the entry point of the program"""
    """Contains the program of the game"""
    print("== Turn 1/6 ==")

    _secret_word: str = secret
    w: int = 1
    _guess: str = ""

    while w <= 6 and _guess != _secret_word:
        print(f"=== Turn {w}/6 ===")
        _guess = input_guess(len(_secret_word))
        print(emojified(_guess, _secret_word))
        if _guess == _secret_word:
            print(f"You won in {w}/6 turns!")
        else:
            w += 1

    if w > 6 and _guess != _secret_word:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
