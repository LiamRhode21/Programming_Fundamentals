from pathlib import Path

def write_movies_writelines(file_path, movies):
    with open(file_path,"w",encoding="utf-8") as file:
        file.writelines(f"{movie}\n" for movie in movies)



def main():
    file_path = Path(__file__).parent/"write_movies_writelines.txt"
    movies = ["Shrek", "Paul", "Star wars"]

    write_movies_writelines(file_path, movies)

if __name__ == "__main__":
     main()