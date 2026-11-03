from pathlib import Path

def write_movie(file_path, movie):
    with open(file_path,"a",encoding="utf-8") as file:
        file.write(f"{movie}\n")




file_path = Path(__file__).parent/"movies.txt"
write_movie(file_path,"Nightmare before Christmas")
write_movie(file_path,"Cujo")

#ask users for movies, add to list until q to quit then call function to write list to file using write

