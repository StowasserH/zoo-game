from animal import Animal

class Monkey(Animal):
    def __init__(self):
        super().__init__("Affe", cost=3000, upkeep=150, attractiveness=30)

    def livespan(self) -> bool:
        return self.age > 12 * 4

    def get_art(self) -> str:
        return "Affe"