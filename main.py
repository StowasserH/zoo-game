from player import Player

# --- Spiel-Logik ---
def run_game() -> None:
    """Startet das Zoo-Tycoon-Spiel."""
    print("Willkommen beim Zoo-Tycoon-Spiel!")
    player_name = input("Wie heißt du? ")
    player = Player(player_name)

    for year in range(1, 11):
        print(f"\n=== Jahr {year} ===")
        for month in range(1, 13):
            print(f"\n--- Monat {month} ---")
            player.monthly_update()
            player.show_menue()

    print(f"\nSpiel beendet! Gesamteinnahmen in 10 Jahren: {player.total_revenue:.2f} Euro")


# --- Start ---
if __name__ == "__main__":
    run_game()
