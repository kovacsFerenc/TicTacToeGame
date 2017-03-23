import os
import time
import shutil

board = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Stuffs for checking
player = 1
Win = 1
Draw = -1
Running = 0
Stop = 1
# others
Game = Running
Mark = 'X'
HighScorePlayer1 = 0
HighScorePlayer2 = 0
columns = shutil.get_terminal_size().columns

# The Function what is Draws the board


def DrawBoard():
    os.system("clear")
    print("    %c | %c | %c " .center(columns) % (board[7], board[8], board[9]))
    print("___|___|___" .center(columns))
    print("    %c | %c | %c " .center(columns) % (board[4], board[5], board[6]))
    print("___|___|___" .center(columns))
    print("    %c | %c | %c " .center(columns) % (board[1], board[2], board[3]))
    print("   |   |   " .center(columns))
    print('High Score Player 2: ' + str(HighScorePlayer1))
    print('High Score Player 1: ' + str(HighScorePlayer2))


#  Function Checks position is empty or not


def CheckPosition(x):
    try:
        if(board[x] == ' '):
            return True
    except IndexError:
        print("Invalid input")
    else:
        return False

# Function for Winner checking


def CheckWin():
    global Game
    # Horizontal Winning Conditions
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
    # Vertical Winning Conditions
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
    # Diagonal Winning Conditions
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
    # Match Tie or Draw Conditions
    elif(board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and
         board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and
         board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running


print("Player 1 [X] --- Player 2 [O]\n")


def running_loop():
    global player
    while(Game == Running):
        DrawBoard()
        if(player % 2 != 0):
            print("Player 1's chance")
            Mark = 'X'
        else:
            print("Player 2's chance")
            Mark = 'O'
        try:
            choice = int(input("Enter the position between [1-9] where you want to mark: "))
        except ValueError:
            print("It's not a typing game, Please select a number from 1-9")
            time.sleep(2)
            continue
        if(CheckPosition(choice)):
            board[choice] = Mark
            player += 1
            CheckWin()
            DrawBoard()


def highscore():
    global HighScorePlayer1
    global HighScorePlayer2
    if Game == Win and player % 2 != 0:
        HighScorePlayer1 += 1
        print('High Score Player 2: ' + str(HighScorePlayer1))
    elif Game == Win and player % 2 == 0:
        HighScorePlayer2 += 1
        print('High Score Player 1: ' + str(HighScorePlayer2))


def game_start():
    global player
    global HighScorePlayer1
    global HighScorePlayer2

    if(Game == Draw):
        print("Game Draw")
    elif(Game == Win):
        player -= 1
        if(player % 2 != 0):
            print("Player 1 Won")
            HighScorePlayer1 += 1
        else:
            print("Player 2 Won")
            HighScorePlayer2 += 1

# Main


def main():
    global board
    global Running
    global Game
    playagain = "yes"
    while playagain == "yes":
        board = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        game_start()
        running_loop()
        print('Do you want to play again? (yes or no)')
        highscore()
        playagain = input()
        Game = Running

main()
