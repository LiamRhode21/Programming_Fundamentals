def display_game_settings(**settings):
    print("Game settings: ")
    if len(settings) != 0:
        for setting,value in settings.items():
            print(f"{setting}: {value}") 
    print(f"Setting count: {len(settings)}")

display_game_settings(difficulty = "easy", sound = True, lives = 3)
display_game_settings()