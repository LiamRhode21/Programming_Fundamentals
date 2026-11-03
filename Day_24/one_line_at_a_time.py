from pathlib import Path

def read_one_movie(file_path):
    movies=[]
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            line = file.readline()
            while line !="":
                movie = line.strip()
                if movie:
                    movies.append(movie)
                line = file.readline()
        return movies
    except FileNotFoundError:
        return None

def main():
    file_path = Path(__file__).parent/"movies.txt"
    movies = read_one_movie(file_path)

    if movies is None:
        print("The file could not be found")
    else:
        for movie in movies:
            print(movie)


if __name__ == "__main__":
    main()