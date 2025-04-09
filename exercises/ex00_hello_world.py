"""My first exercise in COMP110"""

__author__ = "730666919"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "hello, " + name + "!"


greet(name="studnet")
greet(name="Adam")

if __name__ == "__main__":
    print(greet(name=input("what is your name? ")))
