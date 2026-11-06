import csv
from pathlib import Path


def read_sales(file_path):
    game_sales = []
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for game_sale in reader:
                game_sales.append(game_sale)
    except:
        print(f"Error: The File {file_path} does not exist.")
        return None
    return game_sales

def get_popular_games(sales):
    popular_games = []
    for game in sales:
        revenue = float(game['Price']) * int(game['Quantity'])
        if revenue >= 100:
            new_dic = {
                'Game': f'{game['Game']}', 
                'Category': f'{game['Category']}', 
                'Revenue': f'{revenue:.2f}'}
            popular_games.append(new_dic)
    return popular_games

def write_report(file_path, games):
    fieldnames = ["Game", "Category", "Revenue"]
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        if games:
            for game in games:
                writer.writerow(game)

def main():
    read_file_path = Path(__file__).parent/'data'/'game_sales.csv'
    write_file_path = Path(__file__).parent/'data'/'popular_games.csv'
    sales = read_sales(read_file_path)
    if sales == None:
        return
    else:
        popular_games = get_popular_games(sales)
        write_report(write_file_path, popular_games)
        if popular_games:
            print(f"Sale records read: {len(sales)}")
            print()
            for game in popular_games:
                print(f"{game['Game']}: ${game['Revenue']}")
            print()
            print(f"Report file path: {write_file_path}")
        else:
            print('No games earned at least $100')

if __name__ == "__main__":
    main()