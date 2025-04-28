import inspect

from typing import List

from zoo import Zoo
from animal import Animal
from animals import *

# --- Spieler-Klasse ---
class Player:
    def __init__(self, name: str):
        self.name = name
        self.zoo = Zoo()
        self.money: float = 20000.0
        self.total_revenue: float = 0.0

    def buy_animal(self, animal: Animal) -> None:
        """Versucht, ein Tier zu kaufen und zum Zoo hinzuzufügen."""
        if self.money >= animal.cost:
            self.money -= animal.cost
            self.zoo.add_animal(animal)
            animal.create_name()
            print(f"{self.name} hat ein Tier gekauft: {animal.name}")
        else:
            print(f"{self.name} hat nicht genug Geld für {animal.get_art()}!")

    def overview(self) -> None:
        """Zeigt eine Übersicht über alle Tiere im Zoo."""
        for animal in self.zoo.animals:
            print(animal)

    def monthly_update(self) -> None:
        """Führt alle monatlichen Änderungen durch (Tierpflege, Einnahmen, Kosten)."""
        for animal in list(self.zoo.animals):  # Kopie, um bei Entfernung stabil zu bleiben
            animal.update(self)
        upkeep = self.zoo.get_monthly_upkeep()
        income = self.zoo.get_total_attractiveness() * 10
        self.money += income - upkeep
        self.total_revenue += income
        print(f"{self.name}: Einnahmen: {income}, Unterhalt: {upkeep}, Kontostand: {self.money:.2f}")

    def show_menue(self) -> None:
        """Zeigt das Tierkaufmenü und behandelt die Eingabe."""
        animal_classes = [
            cls for name, cls in globals().items()
            if inspect.isclass(cls) and issubclass(cls, Animal) and cls != Animal
        ]
        #for cls in globals().items():
        #    print (cls)
        options: List[Animal] = [cls() for cls in animal_classes]
        print(f"\n{self.name}, wähle ein Tier:")
        for idx, animal in enumerate(options, 1):
            print(f"{idx}. {animal.get_art()} (Kosten: {animal.cost}, Unterhalt: {animal.upkeep}, Attraktivität: {animal.attractiveness})")
        while True:
            choice = input("q = quit, o = Übersicht, Tiernummer (oder leer zum Überspringen): ")
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(options):
                    self.buy_animal(options[index])
                break
            if choice == "q":
                exit()
            if choice == "o":
                self.overview()
            if choice.strip() == "":
                break
