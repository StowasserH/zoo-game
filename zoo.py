import math
from collections import defaultdict
from typing import Dict, List, Type
from animal import Animal

# --- Zoo-Klasse ---
class Zoo:
    def __init__(self):
        self.animals: List[Animal] = []

    def add_animal(self, animal: Animal) -> None:
        """Fügt ein Tier zum Zoo hinzu."""
        self.animals.append(animal)

    def get_monthly_upkeep(self) -> int:
        """Berechnet die monatlichen Unterhaltskosten aller Tiere."""
        return sum(animal.get_monthly_cost() for animal in self.animals)

    def get_animal_counts_by_type(self) -> Dict[Type[Animal], int]:
        """Zählt alle Tiere nach ihrer Art."""
        counts = defaultdict(int)
        for animal in self.animals:
            counts[type(animal)] += 1
        return counts

    def get_total_attractiveness(self) -> float:
        """Berechnet die Gesamtattraktivität basierend auf der Anzahl je Art."""
        total = 0.0
        types={}
        for animal in self.animals:
            art = animal.get_art()
            if art not in types.keys():
                types[art] = 1
            else:
                types[art] += 1
            total += animal.attractiveness / types[art]
        return round(total, 2)


