#ask users for movies, add to list until q to quit then call function to write list to file using write

from pathlib import Path

def write_movies(file_path, movies):
        with open(file_path,"w",encoding="utf-8") as file:
            for movie in movies:
                file.write(f"{movie}\n")

def input_list():
    movies = []
    while True:
        user_input = input("Enter a movie(q to quit): ")
        if user_input.strip().lower() == "q":
             break
        else:
             movies.append(user_input)
    return movies
             

def main():
    file_path = Path(__file__).parent/"exercise_movies.txt"
    movies = input_list()

    write_movies(file_path, movies)

if __name__ == "__main__":
     main()