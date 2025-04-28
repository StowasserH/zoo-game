import random
from typing import List
from animal import Animal

# --- Konkrete Tiere ---
class Lion(Animal):
    """
    Klasse zur Darstellung eines Löwen im Zoo-Spiel.
    Erbt von Animal und erweitert es um spezielle Löwen-Logik (z.B. Namen und Verhalten).
    """
    # Liste typischer Löwen-Namen
    lion_names: List[str] = [
        "Simba", "Mufasa", "Aslan", "Leo", "Rex", "Scar", "Nala", "Shenzi",
        "Caesar", "Majesto", "Brutus", "Zuba", "Kovu", "Sahari", "Thunder",
        "Fang", "Kingo", "Roary", "Khan", "Barafu"
    ]
    def __init__(self) -> None:
        """
        Initialisiert einen Löwen mit festen Kosten, Unterhalt und Attraktivität.
        """
        super().__init__("Löwe", cost=5000, upkeep=300, attractiveness=50)

    def livespan(self) -> bool:
        """
        Bestimmt, ob der Löwe seine maximale Lebensspanne überschritten hat.

        Returns:
            bool: True, wenn die Lebensdauer überschritten ist, sonst False.
        """
        return self.age > 12 * 6  # Lebensspanne: 6 Jahre (bei 12 Monaten pro Jahr)

    def create_name(self) -> None:
        """
        Weist dem Löwen zufällig einen typischen Namen aus der Namensliste zu.
        """
        self.name = random.choice(Lion.lion_names)

    def get_art(self) -> str:
        """
        Gibt die Art des Tieres zurück.

        Returns:
            str: Die Tierart ("Löwe").
        """
        return "Löwe"

    def special_behavior(self, player: "Player") -> None:
        """
        Bestimmt spezielle Verhaltensweise des Löwen abhängig vom Alter:
        - Junge Löwen (Alter < 2 Jahre) sind besonders attraktiv.
        - Ältere Löwen (Alter == 12 Jahre) verlieren an Attraktivität.

        Args:
            player (Player): Der Spieler, dem der Löwe gehört.
        """
        if self.age < 2:
            self.attractiveness = 100
        elif self.age == 12:
            self.attractiveness = 50
