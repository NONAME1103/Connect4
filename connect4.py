import sys
import os
import random
import time

class bcolors:
    HEADER    = '\033[95m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK     = '\33[5m'
    BLINK2    = '\33[6m'
    SELECTED  = '\33[7m'
    RED       = '\33[31m'
    YELLOW    = '\033[93m'
    GREY      = '\33[90m'
    WHITE     = '\33[37m'
    GREEN     = '\033[92m'

def reset():
    if sys.platform.startswith('win32'):
        os.system('cls')
    else:
        os.system('clear')

def title():
    print (bcolors.WHITE + bcolors.BOLD + """
   _____                                  _     _  _
  / ____|                                | |   | || |
 | |      ___   _ __   _ __    ___   ___ | |_  | || |_
 | |     / _ \ | '_ \ | '_ \  / _ \ / __|| __| |__   _|
 | |____| (_) || | | || | | ||  __/| (__ | |_     | |
  \_____|\___/ |_| |_||_| |_| \___| \___| \__|    |_|  """ + bcolors.ENDC)

def board():
    print (bcolors.GREY + """
       |  """ + bcolors.ENDC + bcolors.WHITE + bcolors.BOLD + """◉  ◉  ◉  ◉  ◉  ◉  ◉  """ + bcolors.ENDC + bcolors.GREY + """|
       |  """ + bcolors.ENDC + bcolors.WHITE + bcolors.BOLD + """◉  ◉  ◉  ◉  ◉  ◉  ◉  """ + bcolors.ENDC + bcolors.GREY + """|
       |  """ + bcolors.ENDC + bcolors.WHITE + bcolors.BOLD + """◉  ◉  ◉  ◉  ◉  ◉  ◉  """ + bcolors.ENDC + bcolors.GREY + """|
       |  """ + bcolors.ENDC + bcolors.WHITE + bcolors.BOLD + """◉  ◉  ◉  ◉  ◉  ◉  ◉  """ + bcolors.ENDC + bcolors.GREY + """|
       |  """ + bcolors.ENDC + bcolors.WHITE + bcolors.BOLD + """◉  ◉  ◉  ◉  ◉  ◉  ◉  """ + bcolors.ENDC + bcolors.GREY + """|
       |  """ + bcolors.ENDC + bcolors.WHITE + bcolors.BOLD + """◉  ◉  ◉  ◉  ◉  ◉  ◉  """ + bcolors.ENDC + bcolors.GREY + """|
     | ----------------------------- |
     |   """ + bcolors.ENDC + bcolors.WHITE + bcolors.BOLD + """1   2   3   4   5   6   7   """ + bcolors.ENDC + bcolors.GREY + """|
    """ + bcolors.ENDC,end = "")

def updateBoard():
    rows = {"r1":[columns["c1"][5],columns["c2"][5],columns["c3"][5],columns["c4"][5],columns["c5"][5],columns["c6"][5],columns["c7"][5]],
    "r2":[columns["c1"][4],columns["c2"][4],columns["c3"][4],columns["c4"][4],columns["c5"][4],columns["c6"][4],columns["c7"][4]],
    "r3":[columns["c1"][3],columns["c2"][3],columns["c3"][3],columns["c4"][3],columns["c5"][3],columns["c6"][3],columns["c7"][3]],
    "r4":[columns["c1"][2],columns["c2"][2],columns["c3"][2],columns["c4"][2],columns["c5"][2],columns["c6"][2],columns["c7"][2]],
    "r5":[columns["c1"][1],columns["c2"][1],columns["c3"][1],columns["c4"][1],columns["c5"][1],columns["c6"][1],columns["c7"][1]],
    "r6":[columns["c1"][0],columns["c2"][0],columns["c3"][0],columns["c4"][0],columns["c5"][0],columns["c6"][0],columns["c7"][0]]}
    print (bcolors.WHITE + bcolors.BOLD + "\n\n______________________________________________________________\n\n" + bcolors.ENDC)
    print (bcolors.GREY + "       |  " + bcolors.ENDC,end = "")
    for row in rows:
        for space in range (len (rows[row])):
            if rows[row][space] == "free":
                print (bcolors.WHITE + bcolors.BOLD + "◉  " + bcolors.ENDC,end = "")
            elif rows[row][space] == "p1":
                print (bcolors.RED + "◉  " + bcolors.ENDC,end = "")
            elif rows[row][space] == "p2":
                print (bcolors.YELLOW + "◉  " + bcolors.ENDC,end = "")
        print (bcolors.GREY + "|" + bcolors.ENDC)
        if row != "r6":
            print ( bcolors.GREY + "       |  " + bcolors.ENDC,end = "")
    print (bcolors.GREY + "     | ----------------------------- |" + bcolors.ENDC)
    print (bcolors.GREY + "     |   " + bcolors.ENDC +  bcolors.WHITE + bcolors.BOLD + "1   2   3   4   5   6   7   " + bcolors.ENDC +  bcolors.GREY + "|" + bcolors.ENDC)
    return rows

def winner1():
    print (bcolors.WHITE + bcolors.BOLD + bcolors.BOLD + """
 __          __ _                                _____   _                              __
 \ \        / /(_)                          _   |  __ \ | |                            /_ |
  \ \  /\  / /  _  _ __   _ __    ___  _ __(_)  | |__) || |  __ _  _   _   ___  _ __    | |
   \ \/  \/ /  | || '_ \ | '_ \  / _ \| '__|    |  ___/ | | / _` || | | | / _ \| '__|   | |
    \  /\  /   | || | | || | | ||  __/| |   _   | |     | || (_| || |_| ||  __/| |      | |
     \/  \/    |_||_| |_||_| |_| \___||_|  (_)  |_|     |_| \__,_| \__, | \___||_|      |_|
                                                                    __/ |
                                                                   |___/                   """ + bcolors.ENDC)

def winner2():
    print (bcolors.WHITE + bcolors.BOLD + bcolors.BOLD + """
 __          __ _                                _____   _                              ___
 \ \        / /(_)                          _   |  __ \ | |                            |__  \\
  \ \  /\  / /  _  _ __   _ __    ___  _ __(_)  | |__) || |  __ _  _   _   ___  _ __      ) |
   \ \/  \/ /  | || '_ \ | '_ \  / _ \| '__|    |  ___/ | | / _` || | | | / _ \| '__|    / /
    \  /\  /   | || | | || | | ||  __/| |   _   | |     | || (_| || |_| ||  __/| |      / /_
     \/  \/    |_||_| |_||_| |_| \___||_|  (_)  |_|     |_| \__,_| \__, | \___||_|     |____|
                                                                    __/ |
                                                                   |___/                     """ + bcolors.ENDC)

def draw():
    print (bcolors.WHITE + bcolors.BOLD + bcolors.BOLD + """
    _____
    |  __ \\
    | |  | | _ __  __ _ __      __
    | |  | || '__|/ _` |\ \ /\ / /
    | |__| || |  | (_| | \ V  V /
    |_____/ |_|   \__,_|  \_/\_/
                               """ + bcolors.ENDC)

def normMode(rows,col,close,priority,close2,priority2):
    if priority2 == 0:
        if priority == 0 and close != "any":
            update = False
            col = validColumn(col,update)
            while col == int (close[1]):
                full = 0
                for c in range (len (rows["r1"])):
                    if int (close[1]) != rows["r1"][c] and rows["r1"][c] != "free":
                        full += 1
                if full == 6:
                    col = int (close[1])
                    break
                else:
                    col = random.randint (1,7)
                    update = False
                    col = validColumn(col,update)
        elif priority == 0:
            update = False
            col = validColumn(col,update)
        elif priority == 1:
            col = int (close[1])
        else:
            update = False
            col = validColumn(col,update)
    else:
        col = int (close2[1])
    for column in columns:
        for c in range (len (columns[column])):
            if col == int (column[1]) and columns[column][c] == "free":
                columns[column][c] = "p2"
                valid = True
                break
    return col

def validColumn(col,update):
    valid = False
    while not valid:
        if 1 <= col <= 7:
            for column in columns:
                if columns["c" + str (col)][5] == "free":
                        valid = True
                        if update:
                            for c in range (len (columns[column])):
                                if col == int (column[1]) and columns[column][c] == "free":
                                    columns[column][c] = "p2"
                                    break
                        else:
                            break
                else:
                    col = random.randint (1,7)
                    valid = False
        else:
            col = random.randint (1,7)
            valid = False
    return col

def validChoice(col,player):
    valid = False
    message = False
    while not valid:
        try:
            int (col)
        except ValueError:
            message = True
        else:
            col = int (col)
            if 1 <= col <= 7:
                for column in columns:
                    for c in range (len (columns[column])):
                        if columns[column][5] == "free":
                            if int (col) == int (column[1]) and columns[column][c] == "free":
                                if player == 1:
                                    columns[column][c] = "p1"
                                if player == 2:
                                    columns[column][c] = "p2"
                                valid = True
                                message = False
                                break
                            else:
                                message = True
                        else:
                            message = True
                    if not message:
                        break
            else:
                message = True
        if message:
            print (bcolors.RED + "\nInvalid choice!\n" + bcolors.ENDC)
            col = input (bcolors.GREEN + "Column: " + bcolors.ENDC)
            valid = False
    return col

def checkGameOver(rows):
    gameOver = False
    close = "any"
    close2 = "any"
    priority = 0
    priority2 = 0
    #Player 1 Vertical
    if not gameOver:
        colCount = 0
        for column in columns:
            if not gameOver:
                colCount += 1
                count = 0
                for c in range (len (columns[column])):
                    if columns[column][c] == "p1":
                        count += 1
                    if count < 4 and columns[column][c] != "p1":
                        if columns[column][c] == "free" and count == 3 and priority < 1:
                            close = "c" + str (colCount)
                            priority = 1
                        count = 0
                    if count >= 4:
                        winner = "p1"
                        gameOver = True
                    else:
                        gameOver = False
                        winner = "none"
    #Player 2 Vertical
    if not gameOver:
        colCount2 = 0
        for column in columns:
            if not gameOver:
                colCount2 += 1
                count2 = 0
                for c in range (len (columns[column])):
                    if columns[column][c] == "p2":
                        count2 += 1
                    if count2 < 4 and columns[column][c] != "p2":
                        if columns[column][c] == "free" and count2 == 3 and priority2 < 1:
                            close2 = "c" + str (colCount)
                            priority2 = 1
                        count2 = 0
                    if count2 >= 4:
                        winner = "p2"
                        gameOver = True
                    else:
                        gameOver = False
                        winner = "none"
    #Player 1 Horizontal
    if not gameOver:
        rCount = 0
        for row in rows:
            if not gameOver:
                rCount += 1
                count = 0
                for r in range (len (rows[row])):
                    if rows[row][r] == "p1":
                        count += 1
                        if count == 1:
                            if r != 0 and rows[row][r - 1] == "free":
                                checkLeft = True
                                left = r - 1
                            else:
                                checkLeft = False
                    if count < 4 and rows[row][r] != "p1":
                        if rows[row][r] == "free" and count == 3 and priority < 1:
                            close = "c" + str (r + 1) + " r" + str (row[1])
                            if rCount < 6:
                                ro = "r" + str (rCount + 1)
                                if rows[ro][r] == "free":
                                    priority = 0
                                else:
                                    priority = 1
                        if count == 3 and checkLeft and priority < 1:
                            close = "c" + str (left + 1) + " r" + str (rCount)
                            if rCount < 6:
                                ro = "r" + str (rCount + 1)
                                if rows[ro][left] == "free":
                                    priority = 0
                                else:
                                    priority = 1
                            else:
                                priority = 1
                        count = 0
                    if count >= 4:
                        winner = "p1"
                        gameOver = True
                    else:
                        gameOver = False
                        winner = "none"
    #Player 2 Horizontal
    if not gameOver:
        rCount2 = 0
        for row in rows:
            if not gameOver:
                rCount2 += 1
                count2 = 0
                for r in range (len (rows[row])):
                    if rows[row][r] == "p2":
                        count2 += 1
                        if count2 == 1:
                            if r != 0 and rows[row][r - 1] == "free":
                                checkLeft2 = True
                                left2 = r - 1
                            else:
                                checkLeft2 = False
                    if count2 < 4 and rows[row][r] != "p2":
                        if rows[row][r] == "free" and count2 == 3 and priority2 < 1:
                            close2 = "c" + str (r + 1) + " r" + str (row[1])
                            if rCount2 < 6:
                                ro2 = "r" + str (rCount2 + 1)
                                if rows[ro2][r] == "free":
                                    priority2 = 0
                                else:
                                    priority2 = 1
                        if count2 == 3 and checkLeft2 and priority2 < 1:
                            close2 = "c" + str (left2 + 1) + " r" + str (rCount2)
                            if rCount2 < 6:
                                ro2 = "r" + str (rCount2 + 1)
                                if rows[ro2][left2] == "free":
                                    priority2 = 0
                                else:
                                    priority2 = 1
                            else:
                                priority2 = 1
                        count2 = 0
                    if count2 >= 4:
                        winner = "p2"
                        gameOver = True
                    else:
                        gameOver = False
                        winner = "none"
    #Player 1 Diagonal (Up-Right)
    if not gameOver:
        colCount = 0
        for column in columns:
            if not gameOver:
                colCount += 1
                if colCount == 5:
                    break
                count = 0
                for d in range (3):
                    if columns[column][d] == "p1":
                        count += 1
                    if columns["c" + str(colCount + 1)][d + 1] == "p1":
                        count += 1
                    if columns["c" + str(colCount + 2)][d + 2] == "p1":
                        count += 1
                    if columns["c" + str(colCount + 3)][d + 3] == "p1":
                        count += 1
                    if columns["c" + str(colCount + 3)][d + 3] == "free" and count == 3 and priority < 1:
                        close = "c" + str(colCount + 3) + "[" + str (d + 3) + "]"
                        if columns["c" + str(colCount + 3)][d + 2] == "free":
                            priority = 0
                        else:
                            priority = 1
                    elif columns[column][d] == "free" and count == 3 and priority < 1:
                        close = "c" + str(colCount) + "[" + str (d) + "]"
                        if d == 0:
                            priority = 1
                        else:
                            if columns[column][d - 1] == "free":
                                priority = 0
                            else:
                                priority = 1
                    if count < 4:
                        count = 0
                    if count >= 4:
                        winner = "p1"
                        gameOver = True
                    else:
                        gameOver = False
                        winner = "none"
    #Player 2 Diagonal (Up-Right)
    if not gameOver:
        colCount2 = 0
        for column in columns:
            if not gameOver:
                colCount2 += 1
                if colCount2 == 5:
                    break
                count2 = 0
                for d in range (3):
                    if columns[column][d] == "p2":
                        count2 += 1
                    if columns["c" + str(colCount2 + 1)][d + 1] == "p2":
                        count2 += 1
                    if columns["c" + str(colCount2 + 2)][d + 2] == "p2":
                        count2 += 1
                    if columns["c" + str(colCount2 + 3)][d + 3] == "p2":
                        count2 += 1
                    if columns["c" + str(colCount2 + 3)][d + 3] == "free" and count2 == 3 and priority2 < 1:
                        close2 = "c" + str (colCount2 + 3) + "[" + str (d + 3) + "]"
                        if columns["c" + str(colCount2 + 3)][d + 2] == "free":
                            priority2 = 0
                        else:
                            priority2 = 1
                    elif columns[column][d] == "free" and count2 == 3 and priority2 < 1:
                        close2 = "c" + str(colCount2) + "[" + str (d) + "]"
                        if d == 0:
                            priority2 = 1
                        else:
                            if columns[column][d - 1] == "free":
                                priority2 = 0
                            else:
                                priority2 = 1
                    if count2 < 4:
                        count2 = 0
                    if count2 >= 4:
                        winner = "p2"
                        gameOver = True
                    else:
                        gameOver = False
                        winner = "none"
    #Player 1 Diagonal (Up-Left)
    if not gameOver:
        colCount = 0
        for column in columns:
            if not gameOver:
                colCount += 1
                if colCount > 3:
                    count = 0
                    for d in range (3):
                        if columns[column][d] == "p1":
                            count += 1
                        if columns["c" + str(colCount - 1)][d + 1] == "p1":
                            count += 1
                        if columns["c" + str(colCount - 2)][d + 2] == "p1":
                            count += 1
                        if columns["c" + str(colCount - 3)][d + 3] == "p1":
                            count += 1
                        if columns["c" + str(colCount - 3)][d + 3] == "free" and count == 3 and priority < 1:
                            close = "c" + str (colCount - 3) + "[" + str (d + 3) + "]"
                            if columns["c" + str(colCount - 3)][d + 2] == "free":
                                priority = 0
                            else:
                                priority = 1
                        elif columns[column][d] == "free" and count == 3 and priority < 1:
                            close = "c" + str(colCount) + "[" + str (d) + "]"
                            if d == 0:
                                priority = 1
                            else:
                                if columns[column][d - 1] == "free":
                                    priority = 0
                                else:
                                    priority = 1
                        if count < 4:
                            count = 0
                        if count >= 4:
                            winner = "p1"
                            gameOver = True
                        else:
                            gameOver = False
                            winner = "none"
    #Player 2 Diagonal (Up-Left)
    if not gameOver:
        colCount2 = 0
        for column in columns:
            if not gameOver:
                colCount2 += 1
                if colCount2 > 3:
                    count2 = 0
                    for d in range (3):
                        if columns[column][d] == "p2":
                            count2 += 1
                        if columns["c" + str(colCount2 - 1)][d + 1] == "p2":
                            count2 += 1
                        if columns["c" + str(colCount2 - 2)][d + 2] == "p2":
                            count2 += 1
                        if columns["c" + str(colCount2 - 3)][d + 3] == "p2":
                            count2 += 1
                        if columns["c" + str(colCount2 - 3)][d + 3] == "free" and count2 == 3 and priority2 < 1:
                            close2 = "c" + str (colCount2 - 3) + "[" + str (d + 3) + "]"
                            if columns["c" + str(colCount2 - 3)][d + 2] == "free":
                                priority2 = 0
                            else:
                                priority2 = 1
                        elif columns[column][d] == "free" and count2 == 3 and priority2 < 1:
                            close2 = "c" + str(colCount2) + "[" + str (d) + "]"
                            if d == 0:
                                priority2 = 1
                            else:
                                if columns[column][d - 1] == "free":
                                    priority2 = 0
                                else:
                                    priority2 = 1
                        if count2 < 4:
                            count2 = 0
                        if count2 >= 4:
                            winner = "p2"
                            gameOver = True
                        else:
                            gameOver = False
                            winner = "none"
    #Draw
    if not gameOver:
        for space in range (7):
            if rows["r1"][space] == "free":
                gameOver = False
                winner = "none"
                break
            gameOver = True
            winner = "none"
    return gameOver,winner,close,priority,close2,priority2

#Main
again = "Y"

while again.upper() == "Y":
    reset()
    columns = {"c1":["free","free","free","free","free","free"],
    "c2":["free","free","free","free","free","free"],
    "c3":["free","free","free","free","free","free"],
    "c4":["free","free","free","free","free","free"],
    "c5":["free","free","free","free","free","free"],
    "c6":["free","free","free","free","free","free"],
    "c7":["free","free","free","free","free","free"]}
    title()
    print(bcolors.YELLOW + '''
Choose a Game Mode:
1) 1 player (against computer)
2) 2 players (1v1)
''' + bcolors.ENDC + '--------------------------------------------------------------')
    solo = input (bcolors.GREEN + "\nChoice: " + bcolors.ENDC)

    if solo == "1":
        gameOver = False
        valid = False
        while not valid:
            print(bcolors.YELLOW + '''
    Choose a Difficulty:
    1) Easy
    2) Normal
    ''' + bcolors.ENDC + '--------------------------------------------------------------')
            difficulty = input (bcolors.GREEN + "\nChoice: " + bcolors.ENDC)
            if difficulty == "1":
                dif = "ez"
                valid = True
            elif difficulty == "2":
                dif = "norm"
                valid = True
            else:
                print (bcolors.RED + "\nInvalid choice!" + bcolors.ENDC)
                valid = False
        board()
        while not gameOver:
            player = 1
            choice = input (bcolors.GREEN + "\nColumn: " + bcolors.ENDC)
            choice = validChoice(choice,player)
            reset()
            rows = updateBoard()
            gameOver,winner,close,priority,close2,priority2 = checkGameOver(rows)
            if gameOver:
                break
            time.sleep (0.5)
            comp = random.randint (1,7)
            if dif == "norm":
                comp = normMode(rows,comp,close,priority,close2,priority2)
            else:
                update = True
                comp = validColumn(comp,update)
            reset()
            rows = updateBoard()
            gameOver,winner,close,priority,close2,priority2 = checkGameOver(rows)
        if winner == "p1":
            winner1()
        elif winner == "p2":
            winner2()
        else:
            draw()
        again = input (bcolors.GREEN + "\nWant to play again? (Y/N): " + bcolors.ENDC)
        print ("")

    elif solo == "2":
        gameOver = False
        board()
        while not gameOver:
            player = 1
            choice = input (bcolors.GREEN + "\nPlayer 1 column: " + bcolors.ENDC)
            choice = validChoice(choice,player)
            reset()
            rows = updateBoard()
            gameOver,winner,close,priority,close2,priority2 = checkGameOver(rows)
            if gameOver:
                break
            player = 2
            choice2 = input (bcolors.GREEN + "\nPlayer 2 column: " + bcolors.ENDC)
            choice2 = validChoice(choice2,player)
            reset()
            rows = updateBoard()
            gameOver,winner,close,priority,close2,priority2 = checkGameOver(rows)
        if winner == "p1":
            winner1()
        elif winner == "p2":
            winner2()
        else:
            draw()
        again = input (bcolors.GREEN + "\nWant to play again? (Y/N): " + bcolors.ENDC)
        print ("")
    else:
        print (bcolors.RED + "\nInvalid choice!\n" + bcolors.ENDC)
