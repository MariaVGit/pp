#players = {"Tomek":[10,20,70], etc...}

def define_player(player_no):
    players_points = []
    player_name = input("Podaj imię {} gracza".format(player_no))
    return {player_name: players_points}

def define_players():
    players = {}
    players_total = int(input("Podaj liczbę graczy(1-8): "))
    for i in range(players_total):
        player = define_player(i+1)
        players.update(player)
    return players
def define_win_points():
    return int(input("Zdefiniuj liczbę punktów wygranej: "))

def is_winner(players, win_points):
    for player in players.keys():
        if sum(players[player]) >= win_points:
            return True

def count_points(players, win_points):
    counter = 1
    while True:
        print("\nTura ", counter)
        for player in players.keys():
            player_points = int(input("podaj punkty dla gracza - {}: ".format(player)))
            players[player].append(player_points)
        if is_winner(players, win_points):
            return player
        counter += 1
    return "winner"

def show_results(players, winner):
    print("Wygrał gracz o imieniu {}:".format(winner))
    print()
    print("Szczegółowa tabela wyników:")
    for player in players.items():
        print(player,)        #add "points at the end of ("player, ...)

players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
print(players)
show_results(players,winner)
