import os
import time
import shutil

board = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Win Flags
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

# This Function Draws Game Board


def DrawBoard():   
    os.system("clear") 
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("   |   |   ")
    print('High Score Player 2: ' + str(HighScorePlayer1))
    print('High Score Player 1: ' + str(HighScorePlayer2))
   
#This Function Checks position is empty or not    
def CheckPosition(x): 
    try:   
        if(board[x] == ' '):    
            return True
    except IndexError:
        print("Invalid input")
    else:    
        return False

# This Function Checks player has won or not


def CheckWin():
    global Game
    # Horizontal winning condition
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
    # Vertical Winning Condition
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
    # Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game = Win
    # Match Tie or Draw Condition    
    elif(board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):    
        Game = Draw
    else:
        Game = Running


print("Tic-Tac-Toe Game By Andras & Feri")
print("Player 1 [X] --- Player 2 [O]\n")
print("Please Wait...")


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