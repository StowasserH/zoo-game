import random

# --- Basisklasse für Tiere ---
class Animal:
    """
    Basisklasse für Tiere im Zoo-Spiel.
    Enthält allgemeine Eigenschaften und Verhalten, die für alle Tiere gelten.
    """

    def __init__(self, name: str, cost: int, upkeep: int, attractiveness: int):
        """
        Initialisiert ein Tier mit Name, Anschaffungskosten, Unterhalt und Attraktivität.

        Args:
            name (str): Name des Tiers (kann durch get_art() ersetzt werden, falls leer).
            cost (int): Anschaffungskosten des Tiers.
            upkeep (int): Monatliche Unterhaltskosten.
            attractiveness (int): Anfangswert der Attraktivität.
        """
        if not name:
            self.name = self.get_art()
        else:
            self.name = name
        self.cost = cost
        self.upkeep = upkeep
        self.attractiveness = attractiveness
        self.age = 1  # Alter in Monaten

    def __str__(self) -> str:
        """
        Gibt eine String-Repräsentation des Tiers zurück.

        Returns:
            str: Beschreibender Text über Name, Alter und Attraktivität.
        """
        return f"{self.name} alter:{self.age} attractiveness:{self.attractiveness:.2f}"

    def create_name(self) -> None:
        """
        Erzeugt einen generischen Namen für das Tier anhand seiner Art und eines Zählers.
        Beispiel: 'Lion #1', 'Elephant #2' usw.
        """
        cls = self.__class__
        if not hasattr(cls, "counter"):
            cls.counter = 1
        self.name = f"{self.get_art()} #{cls.counter}"
        cls.counter += 1

    def get_art(self) -> str:
        """
        Gibt die Tierart basierend auf dem Klassennamen zurück.

        Returns:
            str: Tierart (z.B. 'Lion').
        """
        return self.__class__.__name__

    def special_behavior(self, player: "Player") -> None:
        """
        Spezifisches Verhalten der Tier-Unterklassen.

        Args:
            player (Player): Der Spieler, dem das Tier gehört.
        """
        pass  # Wird von Unterklassen überschrieben

    def is_too_old(self) -> bool:
        """
        Prüft, ob das Tier seine maximale Lebensdauer überschritten hat.

        Returns:
            bool: True, wenn das Tier zu alt ist, sonst False.
        """
        return self.age > 24  # Beispiel: 2 Jahre Lebensspanne

    def is_random_death(self) -> bool:
        """
        Berechnet, ob das Tier durch ein zufälliges Ereignis stirbt.

        Returns:
            bool: True, wenn zufälliger Tod eintritt (1 % Chance), sonst False.
        """
        return random.random() < 0.01

    def is_random_ill(self) -> bool:
        """
        Berechnet, ob das Tier krank wird.

        Returns:
            bool: True, wenn Krankheit eintritt (5 % Chance), sonst False.
        """
        return random.random() < 0.05

    def update_attractiveness(self) -> None:
        """
        Aktualisiert die Attraktivität des Tieres.
        Mit zunehmendem Alter sinkt die Attraktivität leicht.
        """
        if self.attractiveness > 10:
            self.attractiveness -= 1

    def update(self, player: "Player") -> None:
        """
        Führt das monatliche Update für ein Tier durch.
        Prüft auf Alterstod, plötzlichen Tod, Krankheit und aktualisiert Alter und Attraktivität.

        Args:
            player (Player): Der Spieler, dem das Tier gehört.
        """
        if self.is_too_old():
            print(f"{self.name} hat sein maximales Alter erreicht und ist gestorben.")
            player.zoo.animals.remove(self)
            return
        if self.is_random_death():
            print(f"{self.name} ist plötzlich gestorben durch ein unerwartetes Ereignis.")
            player.zoo.animals.remove(self)
            return
        if self.is_random_ill():
            kosten = random.randint(1, 10) * 10
            print(f"{self.name} war krank und hat {kosten} gekostet.")
            player.money -= kosten
        self.update_attractiveness()
        self.special_behavior(player)
        self.age += 1

    def get_monthly_cost(self) -> int:
        """
        Gibt die monatlichen Unterhaltskosten des Tieres zurück.

        Returns:
            int: Monatliche Kosten in Währungseinheiten.
        """
        return self.upkeep

    def get_attractiveness(self) -> int:
        """
        Gibt die aktuelle Attraktivität des Tieres zurück.

        Returns:
            int: Attraktivitätswert.
        """
        return self.attractiveness
