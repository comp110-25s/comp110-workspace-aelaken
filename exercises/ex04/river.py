"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]
    """Class to define River."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())


    def check_ages(self):
        """ makes sure the fish does not live past 3 and bears dont live past 5"""
        for fish in self.fish:
                if fish.age > 3:
                    self.fish.remove(fish)

        for bear in self.bears:
            if bear.age>5:
                self.bears.remove(bear)
        return None

    def bears_eating(self):
        """if there are at least 5 fish the bear will eat 3"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
            
        return None

    def check_hunger(self):
        """Checks if the bear is starving and kills them"""
        for bear in self.bears:
            if bear.hunger_score < 0:
                self.bears.remove(bear)
        return None

    def repopulate_fish(self) -> None:
        """modles fish reporduction"""
        num_new_fish = (len(self.fish) // 2) * 4
        for fish in range(num_new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """modles bear reporduction"""
        num_new_bears = len(self.bears) // 2
        for bear in range(num_new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):-> None
        """ tells me the status of my bears and fish in the river"""
        print(f"~~Day {self.day}:~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bears population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()


    def one_river_week(self):
        """Tells me about the river in one week"""
        for _ in range(0, 7):
            self.one_river_day()
        return None



def remove_fish(self, amount: int) -> None:
    """should remove the frontmost fish in the list/river"""
    for x in range(amount):
        if len(self.fish) > 0:
            self.fish.pop(0)