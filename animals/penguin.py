import random
from animal import Animal

class Penguin(Animal):
    def __init__(self):
        super().__init__("Pinguin", cost=2000, upkeep=50, attractiveness=20)

    def special_behavior(self, player: "Player") -> None:
        """Pinguine altern schneller, wenn sie alleine sind."""
        count_penguins = sum(1 for animal in player.zoo.animals if isinstance(animal, Penguin))
        if count_penguins < 2:
            self.age += 2

    def get_art(self) -> str:
        return "Pinguin"
    # pinguine sind selten krank und sterben auch selten einfach so
    def randdeath(self) -> bool:
        return random.random() < 0.001
    def randillnes(self) -> bool:
        return random.random() < 0.02

