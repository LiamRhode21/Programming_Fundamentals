def movie_night(*movies, **details):
    print("Movies:")
    for movie in movies:
        print(f"- {movie}")
    print("Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

movie_night("Shrek", "Toy Story", snack="Popcorn", start="7 PM")