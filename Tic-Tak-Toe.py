# from IPython.display import clear_output
import random

#shpw the board
def display_board(board):
    # clear_output()
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])

#choose which marker each player has
def player_input():
    """
    OUTPUT= (Player 1 marker, Player 2 marker)
    """

    marker = ""

    while marker != "X" and marker != "O":
        marker = input("Player1: Choose X or O: ").upper()

        if marker == "X":
            return ("X", "O")
        else:
            return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker

#see if player wwon
def win_check(board, mark):
    return (
        (board[7] == mark and board[8] == mark and board[9] == mark)
        or (board[4] == mark and board[5] == mark and board[6] == mark)
        or (board[1] == mark and board[2] == mark and board[3] == mark)
        or (board[7] == mark and board[4] == mark and board[1] == mark)
        or (board[8] == mark and board[5] == mark and board[2] == mark)
        or (board[9] == mark and board[6] == mark and board[3] == mark)
        or (board[7] == mark and board[5] == mark and board[3] == mark)
        or (board[9] == mark and board[5] == mark and board[1] == mark)
    )

#who goes first
def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

#check if space is open or closed
def space_check(board, position):
    return board[position] == " "

# check if board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

#player chooses where to put their marker
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(
        board, position
    ):
        position = int(input("Choose a position: (1-9)"))

    return position

#ask if player would like to play again
def replay():
    choice = input("Play again? Enter Yes or No")

    return choice == "Yes"

#put all functions together
print("Welcome to Tic Tac Toe")
#make board empty 
#choose player marker and who is going first
while True:
    the_board = [" "] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")
#ask player  if they are ready to play
    play_game = input("Ready to play? y or n?")
    if play_game == "y":
        game_on = True
    else:
        game_on = False
#begin game
#play game if player 1 goes first
#player 1 play 
#check if player 1 win
#player 2 play
#check if player 2 win
#repeat till win 
#or show tie screen
    while game_on:
        if turn == "Player 1":
            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!!")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = "Player 2"

        else:
            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON!!")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break
