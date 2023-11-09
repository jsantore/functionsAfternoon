

def get_data():
    data = []
    data_file = open("data.txt", encoding='UTF-8')
    game_data_strings = data_file.readlines()
    for game in game_data_strings:
        game_data = game.split("|")
        game_dict = {"name":game_data[0],
                     "release":int(game_data[1]),
                     "price":float(game_data[2]),
                     "total_sales": int(game_data[3])}
        data.append(game_dict)
    return data

def main():
    all_games = get_data()
    while True:
        print_menu()
        selection = input("type the number for your selection:")
        if '1' in selection:
            pass
        elif "2" == selection:
            find_average_revenue(all_games)
        elif "3" == selection:
            break
        else:
            print("That is not a valid option, please try again")

def find_average_revenue(list_of_games):
    for game in list_of_games:
        age = 2024 - game['release']
        revenue = game['total_sales']
        average_revenue = revenue/age
        print(f"{game['name']} averaged ${average_revenue} over {age} years")

def print_menu():
    menu = """
[1]Add a new Game
[2]Find average revenue per year
[3]Quit 
    """
    print(menu)


main()