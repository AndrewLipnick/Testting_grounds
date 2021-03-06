import itertools 

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    
    #horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    #diag
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)!")
        return True

    #vert
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {row[0]} is the winner vertically!")
            return True
    return False


def game_board(game_map, player=0, row=0, column=0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print("This position has already been taken! Choose another.")
            return game_map, False
            
        row_label = "    "
        row_number = 0
        for number in game_map:
            row_label += (str(row_number) + "  ")
            row_number += 1

        print(row_label)

        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count ,row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0,1, or 2")
        return game_map,False

    


player_choice = itertools.cycle([1,2])
play = True
players = [1,2]
print("You are going to play a game of tic-tac-toe. You will need two people to play")
print("The game board will be square and the winner is the first person to get an entire row, column, or diagonal.")
while play:
    game_size = int(input("What size game would you like to play (integer): "))
    rows = []    
    game = []
    options = "("
    for column in range(game_size):
        rows.append(0)
        options += (str(column) + ",")
    
    options = options[:-1]
    options += "):"

    for row in range(game_size):
        game.append(rows[:])

    game_won = False
    game, _ = game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_choice)
        print(f"current_player: {current_player}")
        played = False

        while not played:   
            column_choice = int(input("What column do you want to play? " +  options))
            row_choice = int(input("What row do you want to play?" +  options))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again (y/n)?")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Bye")
                play = False
            else:
                print("Not a valid answer, so game not restarting")
                play = False