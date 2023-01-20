from sys import exit
from pyfiglet import Figlet
from random import choice

# Set the field to an empty state
squares = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def main():
    try:
        if input("Two Players? (yes/no): ").lower() in ["y", "yes"]:
            start_two_player_game()
        else:
            start_one_player_game()
    except KeyboardInterrupt:
        exit("The Game was canceled")

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
            return choice([0, 2, 6, 8])
        # 30% chance for center
        elif res > 50 and res <= 80:
            return 4
        # 20% chance for edge
        else:
            return choice([1, 3, 5, 7])

    else: 
        return ""


# Returns the indexes of every free square
def avaliable_squares():
    global squares
    return [i for i in range(len(squares)) if squares[i] == " "]


def two_squares_owned(n1, n2, X_or_O):
    global squares

    if squares[n1] == X_or_O and squares[n2] == X_or_O:
        return True


# Returns a square to pick, if it wins the match this/next turn
def check_winning_condition(options, X_or_O):
    for o in options:
        if o == 0:
            if two_squares_owned(1, 2, X_or_O):
                return 0
            elif two_squares_owned(3, 6, X_or_O):
                return 0
            elif two_squares_owned(4, 8, X_or_O):
                return 0

        elif o == 1:
            if two_squares_owned(0, 2, X_or_O):
                return 1
            elif two_squares_owned(4, 7, X_or_O):
                return 1

        elif o == 2:
            if two_squares_owned(0, 1, X_or_O):
                return 2
            elif two_squares_owned(4, 6, X_or_O):
                return 2
            elif two_squares_owned(5, 8, X_or_O):
                return 2

        elif o == 3:
            if two_squares_owned(0, 6, X_or_O):
                return 3
            elif two_squares_owned(4, 5, X_or_O):
                return 3

        elif o == 4:
            if two_squares_owned(0, 8, X_or_O):
                return 4
            elif two_squares_owned(1, 7, X_or_O):
                return 4
            elif two_squares_owned(3, 5, X_or_O):
                return 4
            elif two_squares_owned(2, 6, X_or_O):
                return 4

        elif o == 5:
            if two_squares_owned(3, 4, X_or_O):
                return 5
            elif two_squares_owned(2, 8, X_or_O):
                return 5

        elif o == 6:
            if two_squares_owned(0, 3, X_or_O):
                return 6
            elif two_squares_owned(2, 4, X_or_O):
                return 6
            elif two_squares_owned(7, 8, X_or_O):
                return 6

        elif o == 7:
            if two_squares_owned(6, 8, X_or_O):
                return 7
            elif two_squares_owned(1, 4, X_or_O):
                return 7

        elif o == 8:
            if two_squares_owned(6, 7, X_or_O):
                return 8
            elif two_squares_owned(2, 5, X_or_O):
                return 8
            elif two_squares_owned(0, 4, X_or_O):
                return 8

        else:
            raise ValueError("check_winning_condition got a square option that isn't in the range 0 - 8")

    return ""


def choose_square(options):
    center = 4
    corner_edge = [0, 2, 6, 8]
    edge = [1, 3, 5, 7]

    # Lists with high to low priority
    high_prio = []
    medium_prio = []
    low_prio = []

    for option in options:
        if option in corner_edge:
            high_prio.append(option)
        elif option == center:
            medium_prio.append(option)
        elif option in edge:
            low_prio.append(option)
        else:
            raise ValueError("choose_square option wasn't in range 0 - 8")
    
    if not len(high_prio) == 0:
        if len(high_prio) > 1:
            return choice(high_prio)
        else:
            return high_prio[0]
    elif not len(medium_prio) == 0:
        if len(medium_prio) > 1:
            return choice(medium_prio)
        else:
            return medium_prio[0]
    else:
        if len(low_prio) > 1:
            return choice(low_prio)
        else:
            return low_prio[0]


def bot_decision():
    # If its the last avaliable square then no need to consider other things
    options = avaliable_squares()
    if len(options) == 1:
        return options[0]

    # If there is a way for the bot to win this turn then return that square
    if winning_condition := check_winning_condition(options, "O"):
        return winning_condition
    
    # If the player has the possibility to win next round 
    # return the first square. If there are more than one
    # then the bot can't do anything about it anyway
    if loosing_condition := check_winning_condition(options, "X"):
        return loosing_condition

    return choose_square(options)


def bot_turn():
    global squares
    # Gives back a string, saying which field to choose
    # IF the bot starts the match
    next_move = bot_gamestart()
    if not next_move == "":
       squares[next_move] = "O"
       return
    
    squares[bot_decision()] = "O"
    

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
            # Check who won
            if squares[n3 - 1] == "X":
                print("\n-----------------------------------------------------")
                print(game_over(), end="")
                print("------------------------------------------------------")   
                print_field("")
                exit(f"Player 1 won with the row {n1, n2, n3}")
            else:
                print("\n-----------------------------------------------------")
                print(game_over(), end="")
                print("------------------------------------------------------")   
                print_field("")
                exit(f"Player 2/Bot won with the row {n1, n2, n3}")


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
    print("\nPlayer 1 is X\nBot is O\n")
    result = choice(["Player 1", "Bot"])
    print(result, "begins")
    if result == "Player 1":
        while True:
            print_field("X")
            player_turn("X")
            check_field()
            bot_turn()
            check_field()
    else:
        while True:
            bot_turn()
            check_field()
            print_field("X")
            player_turn("X")
            check_field()
    

if __name__ == "__main__":
    main()