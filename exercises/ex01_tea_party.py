"""ex01_tea_party.py_AdamLaken_"""

__AdamLaken__: str = "730666919"


def main_planner(guests: int) -> None:
    """connects the program together"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))

    print(
        "Cost: $"
        + str(
            cost(
                tea_count=(tea_bags(people=guests)), treat_count=(treats(people=guests))
            )
        )
    )


def tea_bags(people: int) -> int:
    """Number of tea bags needed for each person"""

    return people * 2


def treats(people: int) -> int:
    """the amount of treats needed for each person"""

    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """tells me the total cost of treats and teabags"""

    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
