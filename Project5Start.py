def get_project5_data() -> list[dict]:
    data = []
    data_file = open("data.txt")
    game_data_strings = data_file.readlines()
    for game in game_data_strings:
        game_data = game.split("|")
        game_dict = {"name":game_data[0],
                     "release":int(game_data[1]),
                     "price":float(game_data[2]),
                     "total_sales": int(game_data[3])}
        data.append(game_dict)
    return data
