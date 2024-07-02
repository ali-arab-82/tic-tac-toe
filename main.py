from os import system
from random import randint
from platform import system as sysName

user_sign = 'X'
bot_sign = 'O'

board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

def clearScreen():
    # mac and linux
    if sysName() == "Linux" or sysName == "Darwin":
        system("clear")
    # windows
    elif sysName() == "Windows":
        system("cls")

def showBoard():
    clearScreen()
    for i in range(3):
        for j in range(3):
            print(' ', end='')
            print(board[i][j], end='')
            if j < 2:
                print(' |', end='')
        print()
        if i < 2:
            print("-----------")
    print()

def getInput():
    x, y = input("x, y: ").split(' ')
    x = int(x) - 1
    y = int(y) - 1

    while not isEmpty(x, y):
        print("try again!\n")
        x, y = input("x, y: ").split(' ')
        x = int(x) - 1
        y = int(y) - 1

    board[x][y] = 'X'

def isEmpty(x, y):
    if board[x][y] == '_':
        return True
    return False

def isWinning(sign = user_sign):
    # horizontal check
    for i in range(len(board)):
        if board[i].count(sign) == 2 and '_' in board[i]:
            return True, i, board[i].index('_')

    # vertical check
    for i in range(3):
        col = []
        for j in range(3):
            col.append(board[j][i])
        if col.count(sign) == 2 and '_' in col:
            return True, col.index('_'), i
    
    # diagnal check
    diag = []
    for i in range(3):
        diag.append(board[i][i])
        if diag.count(sign) == 2 and '_' in diag:
            return True, diag.index('_'), diag.index('_')
    diag = []
    for i in range(3):
        diag.append(board[i][2 - i])
        if diag.count(sign) == 2 and '_' in diag:
            return True, diag.index('_'), 2 - diag.index('_')
    
    return False, None, None

def bot():
    if isEmpty(1, 1):
        board[1][1] = bot_sign
        return False
    elif board[1][1] == user_sign:
        index = randint(0, 3)
        coordinates = [(0, 0), (0, 2), (2, 0), (2, 2)]
        x, y = coordinates[index]
        board[x][y] = bot_sign
        return False
    
    is_winning, x, y = isWinning(bot_sign)
    if is_winning and isEmpty(x, y):
        board[x][y] = bot_sign
        showBoard()
        return True
    
    is_winning, x, y = isWinning(user_sign)
    if is_winning and isEmpty(x, y):
        print(x, y)
        board[x][y] = bot_sign
    else:
        x = randint(0, 2)
        y = randint(0, 2)
        
        while not isEmpty(x, y) and ('_' in board[0] or '_' in board[1] or '_' in board[2]):
            x = randint(0, 2)
            y = randint(0, 2)
        board[x][y] = bot_sign

    return False

is_bot_wins = False

first_player = randint(0, 1)
first_player = "bot" if first_player == 0 else "user"

while '_' in board[0] or '_' in board[1] or '_' in board[2]:
    if first_player == "user":
        showBoard()
        getInput()
        if bot():
            is_bot_wins = True
            print("Bot wins")
            break
    else:
        if bot():
            is_bot_wins = True
            print("Bot wins")
            break
        showBoard()
        getInput()

# user can't win the bot (the bot won't make mistakes)
if is_bot_wins == False:
    showBoard()
    print("Draw")
