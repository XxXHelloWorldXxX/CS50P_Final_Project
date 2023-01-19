from sys import exit
from pyfiglet import Figlet
from random import choice


# Set the field to an empty state
squares = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def main():
    if input("Two Players? (yes/no): ").lower() in ["y", "yes"]:
        start_two_player_game()
    else:
        start_one_player_game()


def print_field(player):
    global squares

    if player == "X":
        print("\nPlayer 1", end="")
    elif player == "O":
        print("\nPlayer 2", end="")


    print("\n-------------------")
    print(f"|  {squares[0]}  |  {squares[1]}  |  {squares[2]}  |")
    print("-------------------")
    print(f"|  {squares[3]}  |  {squares[4]}  |  {squares[5]}  |")
    print("-------------------")
    print(f"|  {squares[6]}  |  {squares[7]}  |  {squares[8]}  |")
    print("-------------------\n")


def bot_gamestart():
    global squares

    # Check if it's an empty field
    if not "X" in squares and "O" not in squares:
        res = choice(range(0, 101))

        # 50% chance for corner edge 
        if res >= 0 and res <= 50:
            return choice([1, 3, 7, 9])
        # 30% chance for center
        elif res > 50 and res <= 80:
            return choice([2, 4, 6, 8])
        # 20% chance for edge
        else:
            return 5

    else: 
        return ""

# Check to see if you can win this turn
def check_winning_condition():
    global squares

    for square in squares:
        if square == "O":
            try:
                ...
            except:
                ...

def bot_turn():
    global squares

    bot_decision = []

    # Gives back a string, saying which field to choose
    # IF the bot starts the match
    next_move = bot_gamestart()
    if not next_move == "":
       squares[next_move - 1] = "O"
       return
    
    check_winning_condition()


def player_turn(player):
    global squares
    while True:
        # Choosing a square
        try:
            number = int(input("Choose a square (1 - 9): "))
        except ValueError:
            print("Wrong input. Please choose a number from 1 - 9: ")
            continue
        # Check if not number 1 - 9
        if number < 1 or number > 9:
            print("Please choose a number from 1 - 9: ")
            continue
        # Check that square if it's still empty
        if squares[number - 1] == " ":
            squares[number - 1] = player
            break
        else:
            print("That square was already chosen. Pick another")
            continue


def check_row(n1, n2, n3):
    # If the first square is still empty, 
    # then we can skip this check
    if squares[n1 - 1] == " ":
        return
    
    if squares[n1 - 1] == squares[n2 - 1]:
        if squares[n2 - 1] == squares[n3 - 1]:
            if squares[n3 - 1] == "X":
                print("\n-----------------------------------------------------")
                print(game_over(), end="")
                print("------------------------------------------------------")   
                print_field("")
                exit(f"Player 1 won with the row {n1, n2, n3}")
            else:
                exit(f"Player 2/Bot won with the row {n1, n2, n3}")
                print_field("")



# Check if somebody won or if it's a tie
def check_field():

    # Check left to right
    check_row(1, 2, 3)
    check_row(4, 5, 6)
    check_row(7, 8, 9)

    # Check top to bottom
    check_row(1, 4, 7)
    check_row(2, 5, 8)
    check_row(3, 6, 9)

    # Check diagonals
    check_row(1, 5, 9)
    check_row(3, 5, 7)

    if not " " in squares:
        print("\n----------------------------------------")
        print(game_over())
        print("----------------------------------------")        
        print_field("")
        exit("It's a tie!")


def game_over():
    f = Figlet()
    return f.renderText("GAMEOVER")


def start_two_player_game():
    print("\nPlayer 1 is X\nPlayer 2 is O\n")
    while True:
        print_field("X")
        player_turn("X")
        check_field()
        print_field("O")
        player_turn("O")
        check_field()


def start_one_player_game():
    print("\nPlayer is X\nBot is O\n")
    result = choice(["Player 1", "Bot"])
    print(result, "begins")
    if result == "Player 1":
        print_field("X")
        player_turn("X")
        check_field()
        bot_turn()
        check_field()
    



# selected_squares = []

# ------------------
# |     |     |    |
# ------------------
# |     |     |    |
# ------------------
# |     |     |    |
# ------------------

if __name__ == "__main__":
    main()