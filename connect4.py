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
    r1 = [c1[5],c2[5],c3[5],c4[5],c5[5],c6[5],c7[5]]
    r2 = [c1[4],c2[4],c3[4],c4[4],c5[4],c6[4],c7[4]]
    r3 = [c1[3],c2[3],c3[3],c4[3],c5[3],c6[3],c7[3]]
    r4 = [c1[2],c2[2],c3[2],c4[2],c5[2],c6[2],c7[2]]
    r5 = [c1[1],c2[1],c3[1],c4[1],c5[1],c6[1],c7[1]]
    r6 = [c1[0],c2[0],c3[0],c4[0],c5[0],c6[0],c7[0]]

    print (bcolors.WHITE + bcolors.BOLD + "\n\n___________________________________________________________________________________________________________________\n\n" + bcolors.ENDC)
    print (bcolors.GREY + "       |  " + bcolors.ENDC,end = "")
    for space in range (len (r1)):
        if r1[space] == "free":
            print ( bcolors.WHITE + bcolors.BOLD + "◉  " + bcolors.ENDC,end = "")
        elif r1[space] == "p1":
            print ( bcolors.RED + "◉  " + bcolors.ENDC,end = "")
        elif r1[space] == "p2":
            print ( bcolors.YELLOW + "◉  " + bcolors.ENDC,end = "")
    print ( bcolors.GREY + "|" + bcolors.ENDC)
    print ( bcolors.GREY + "       |  " + bcolors.ENDC,end = "")
    for space in range (len (r2)):
        if r2[space] == "free":
            print ( bcolors.WHITE + bcolors.BOLD + "◉  " + bcolors.ENDC,end = "")
        elif r2[space] == "p1":
            print ( bcolors.RED + "◉  " + bcolors.ENDC,end = "")
        elif r2[space] == "p2":
            print ( bcolors.YELLOW + "◉  " + bcolors.ENDC,end = "")
    print ( bcolors.GREY + "|" + bcolors.ENDC)
    print ( bcolors.GREY + "       |  " + bcolors.ENDC,end = "")
    for space in range (len (r3)):
        if r3[space] == "free":
            print ( bcolors.WHITE + bcolors.BOLD + "◉  " + bcolors.ENDC,end = "")
        elif r3[space] == "p1":
            print ( bcolors.RED + "◉  " + bcolors.ENDC,end = "")
        elif r3[space] == "p2":
            print ( bcolors.YELLOW + "◉  " + bcolors.ENDC,end = "")
    print ( bcolors.GREY + "|" + bcolors.ENDC)
    print ( bcolors.GREY + "       |  " + bcolors.ENDC,end = "")
    for space in range (len (r4)):
        if r4[space] == "free":
            print ( bcolors.WHITE + bcolors.BOLD + "◉  " + bcolors.ENDC,end = "")
        elif r4[space] == "p1":
            print ( bcolors.RED + "◉  " + bcolors.ENDC,end = "")
        elif r4[space] == "p2":
            print ( bcolors.YELLOW + "◉  " + bcolors.ENDC,end = "")
    print ( bcolors.GREY + "|" + bcolors.ENDC)
    print ( bcolors.GREY + "       |  " + bcolors.ENDC,end = "")
    for space in range (len (r5)):
        if r5[space] == "free":
            print ( bcolors.WHITE + bcolors.BOLD + "◉  " + bcolors.ENDC,end = "")
        elif r5[space] == "p1":
            print ( bcolors.RED + "◉  " + bcolors.ENDC,end = "")
        elif r5[space] == "p2":
            print ( bcolors.YELLOW + "◉  " + bcolors.ENDC,end = "")
    print ( bcolors.GREY + "|" + bcolors.ENDC)
    print ( bcolors.GREY + "       |  " + bcolors.ENDC,end = "")
    for space in range (len (r6)):
        if r6[space] == "free":
            print ( bcolors.WHITE + bcolors.BOLD + "◉  " + bcolors.ENDC,end = "")
        elif r6[space] == "p1":
            print ( bcolors.RED + "◉  " + bcolors.ENDC,end = "")
        elif r6[space] == "p2":
            print ( bcolors.YELLOW + "◉  " + bcolors.ENDC,end = "")
    print ( bcolors.GREY + "|" + bcolors.ENDC)
    print ( bcolors.GREY + "     | ----------------------------- |" + bcolors.ENDC)
    print ( bcolors.GREY + "     |   " + bcolors.ENDC +  bcolors.WHITE + bcolors.BOLD + "1   2   3   4   5   6   7   " + bcolors.ENDC +  bcolors.GREY + "|" + bcolors.ENDC)
    return r1,r2,r3,r4,r5,r6

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

def normMode(r1,col,close,priority,close2,priority2):
    if priority2 == 0:
        if 0 < priority < 3:
            while col == int (close[1]):
                col = random.randint (1,7)
                if int (close[1]) == 1 and r1[1] != "free" and r1[2] != "free" and r1[3] != "free" and r1[4] != "free" and r1[5] != "free" and r1[6] != "free":
                    col = 1
                    break
                elif int (close[1]) == 2 and r1[0] != "free" and r1[2] != "free" and r1[3] != "free" and r1[4] != "free" and r1[5] != "free" and r1[6] != "free":
                    col = 2
                    break
                elif int (close[1]) == 3 and r1[0] != "free" and r1[1] != "free" and r1[3] != "free" and r1[4] != "free" and r1[5] != "free" and r1[6] != "free":
                    col = 3
                    break
                elif int (close[1]) == 4 and r1[0] != "free" and r1[1] != "free" and r1[2] != "free" and r1[4] != "free" and r1[5] != "free" and r1[6] != "free":
                    col = 4
                    break
                elif int (close[1]) == 5 and r1[0] != "free" and r1[1] != "free" and r1[2] != "free" and r1[3] != "free" and r1[5] != "free" and r1[6] != "free":
                    col = 5
                    break
                elif int (close[1]) == 6 and r1[0] != "free" and r1[1] != "free" and r1[2] != "free" and r1[3] != "free" and r1[4] != "free" and r1[6] != "free":
                    col = 6
                    break
                elif int (close[1]) == 7 and r1[0] != "free" and r1[1] != "free" and r1[2] != "free" and r1[3] != "free" and r1[4] != "free" and r1[5] != "free":
                    col = 7
                    break
            skip = False
        elif priority >= 3:
            col = int (close[1])
            skip = False
        else:
            col = validColumn(col)
            skip = True
    else:
        col = int (close2[1])
        skip = False
    if not skip:
        if col == 1:
            for c in range (len (c1)):
                if c1[c] == "free":
                    c1[c] = "p2"
                    break
        if col == 2:
            for c in range (len (c2)):
                if c2[c] == "free":
                    c2[c] = "p2"
                    break
        if col == 3:
            for c in range (len (c3)):
                if c3[c] == "free":
                    c3[c] = "p2"
                    break
        if col == 4:
            for c in range (len (c4)):
                if c4[c] == "free":
                    c4[c] = "p2"
                    break
        if col == 5:
            for c in range (len (c5)):
                if c5[c] == "free":
                    c5[c] = "p2"
                    break
        if col == 6:
            for c in range (len (c6)):
                if c6[c] == "free":
                    c6[c] = "p2"
                    break
        if col == 7:
            for c in range (len (c7)):
                if c7[c] == "free":
                    c7[c] = "p2"
                    break
    return col

def validColumn(column):
    valid = False
    while not valid:
        if 1 <= column <= 7:
            if column == 1:
                if c1[5] == "free":
                    for c in range (len (c1)):
                        if c1[c] == "free":
                            c1[c] = "p2"
                            valid = True
                            break
                else:
                    column = random.randint (1,7)
            elif column == 2:
                if c2[5] == "free":
                    for c in range (len (c2)):
                        if c2[c] == "free":
                            c2[c] = "p2"
                            valid = True
                            break
                else:
                    column = random.randint (1,7)
            elif column == 3:
                if c3[5] == "free":
                    for c in range (len (c3)):
                        if c3[c] == "free":
                            c3[c] = "p2"
                            valid = True
                            break
                else:
                    column = random.randint (1,7)
            elif column == 4:
                if c4[5] == "free":
                    for c in range (len (c4)):
                        if c4[c] == "free":
                            c4[c] = "p2"
                            valid = True
                            break
                else:
                    column = random.randint (1,7)
            elif column == 5:
                if c5[5] == "free":
                    for c in range (len (c5)):
                        if c5[c] == "free":
                            c5[c] = "p2"
                            valid = True
                            break
                else:
                    column = random.randint (1,7)
            elif column == 6:
                if c6[5] == "free":
                    for c in range (len (c6)):
                        if c6[c] == "free":
                            c6[c] = "p2"
                            valid = True
                            break
                else:
                    column = random.randint (1,7)
            elif column == 7:
                if c7[5] == "free":
                    for c in range (len (c7)):
                        if c7[c] == "free":
                            c7[c] = "p2"
                            valid = True
                            break
                else:
                    column = random.randint (1,7)
        else:
            column = random.randint (1,7)
    return column

def validChoice(column,player):
    valid = False
    message = False
    while not valid:
        try:
            int (column)
        except ValueError:
            message = True
        else:
            column = int (column)
            if 1 <= column <= 7:
                if column == 1:
                    if c1[5] == "free":
                        for c in range (len (c1)):
                            if c1[c] == "free":
                                if player == 1:
                                    c1[c] = "p1"
                                if player == 2:
                                    c1[c] = "p2"
                                valid = True
                                message = False
                                break
                    else:
                        message = True
                elif column == 2:
                    if c2[5] == "free":
                        for c in range (len (c2)):
                            if c2[c] == "free":
                                if player == 1:
                                    c2[c] = "p1"
                                if player == 2:
                                    c2[c] = "p2"
                                valid = True
                                message = False
                                break
                    else:
                        message = True
                elif column == 3:
                    if c3[5] == "free":
                        for c in range (len (c3)):
                            if c3[c] == "free":
                                if player == 1:
                                    c3[c] = "p1"
                                if player == 2:
                                    c3[c] = "p2"
                                valid = True
                                message = False
                                break
                    else:
                        message = True
                elif column == 4:
                    if c4[5] == "free":
                        for c in range (len (c4)):
                            if c4[c] == "free":
                                if player == 1:
                                    c4[c] = "p1"
                                if player == 2:
                                    c4[c] = "p2"
                                valid = True
                                message = False
                                break
                    else:
                        message = True
                elif column == 5:
                    if c5[5] == "free":
                        for c in range (len (c5)):
                            if c5[c] == "free":
                                if player == 1:
                                    c5[c] = "p1"
                                if player == 2:
                                    c5[c] = "p2"
                                valid = True
                                message = False
                                break
                    else:
                        message = True
                elif column == 6:
                    if c6[5] == "free":
                        for c in range (len (c6)):
                            if c6[c] == "free":
                                if player == 1:
                                    c6[c] = "p1"
                                if player == 2:
                                    c6[c] = "p2"
                                valid = True
                                message = False
                                break
                    else:
                        message = True
                elif column == 7:
                    if c7[5] == "free":
                        for c in range (len (c7)):
                            if c7[c] == "free":
                                if player == 1:
                                    c7[c] = "p1"
                                if player == 2:
                                    c7[c] = "p2"
                                valid = True
                                message = False
                                break
                    else:
                        message = True
            else:
                message = True
        if message:
            print (bcolors.RED + "\nInvalid choice!\n" + bcolors.ENDC)
            column = input (bcolors.GREEN + "Column: " + bcolors.ENDC)
            valid = False
    return column

def checkGameOver(r1,r2,r3,r4,r5,r6):
    gameOver = False
    close = "any"
    close2 = "any"
    priority = 0
    priority2 = 0
    #Player 1 Vertical
    if not gameOver:
        count = 0
        for c in range (6):
            if c1[c] == "p1":
                count += 1
            if count < 4 and c1[c] != "p1":
                if c1[c] == "free" and count == 3 and priority < 5:
                    close = "c1"
                    priority = 5
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for c in range (6):
            if c2[c] == "p1":
                count += 1
            if count < 4 and c2[c] != "p1":
                if c2[c] == "free" and count == 3 and priority < 5:
                    close = "c2"
                    priority = 5
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for c in range (6):
            if c3[c] == "p1":
                count += 1
            if count < 4 and c3[c] != "p1":
                if c3[c] == "free" and count == 3 and priority < 5:
                    close = "c3"
                    priority = 5
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for c in range (6):
            if c4[c] == "p1":
                count += 1
            if count < 4 and c4[c] != "p1":
                if c4[c] == "free" and count == 3 and priority < 5:
                    close = "c4"
                    priority = 5
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for c in range (6):
            if c5[c] == "p1":
                count += 1
            if count < 4 and c5[c] != "p1":
                if c5[c] == "free" and count == 3 and priority < 5:
                    close = "c5"
                    priority = 5
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for c in range (6):
            if c6[c] == "p1":
                count += 1
            if count < 4 and c6[c] != "p1":
                if c6[c] == "free" and count == 3 and priority < 5:
                    close = "c6"
                    priority = 5
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for c in range (6):
            if c7[c] == "p1":
                count += 1
            if count < 4 and c7[c] != "p1":
                if c7[c] == "free" and count == 3 and priority < 5:
                    close = "c7"
                    priority = 5
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    #Player 2 Vertical
    if not gameOver:
        count2 = 0
        for c in range (6):
            if c1[c] == "p2":
                count2 += 1
            if count2 < 4 and c1[c] != "p2":
                if c1[c] == "free" and count2 == 3 and priority2 < 1:
                    close2 = "c1"
                    priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for c in range (6):
            if c2[c] == "p2":
                count2 += 1
            if count2 < 4 and c2[c] != "p2":
                if c2[c] == "free" and count2 == 3 and priority2 < 1:
                    close2 = "c2"
                    priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for c in range (6):
            if c3[c] == "p2":
                count2 += 1
            if count2 < 4 and c3[c] != "p2":
                if c3[c] == "free" and count2 == 3 and priority2 < 1:
                    close2 = "c3"
                    priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for c in range (6):
            if c4[c] == "p2":
                count2 += 1
            if count2 < 4 and c4[c] != "p2":
                if c4[c] == "free" and count2 == 3 and priority2 < 1:
                    close2 = "c4"
                    priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for c in range (6):
            if c5[c] == "p2":
                count2 += 1
            if count2 < 4 and c5[c] != "p2":
                if c5[c] == "free" and count2 == 3 and priority2 < 1:
                    close2 = "c5"
                    priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for c in range (6):
            if c6[c] == "p2":
                count2 += 1
            if count2 < 4 and c6[c] != "p2":
                if c6[c] == "free" and count2 == 3 and priority2 < 1:
                    close2 = "c6"
                    priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for c in range (6):
            if c7[c] == "p2":
                count2 += 1
            if count2 < 4 and c7[c] != "p2":
                if c7[c] == "free" and count2 == 3 and priority2 < 1:
                    close2 = "c7"
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
        count = 0
        for r in range (7):
            if r1[r] == "p1":
                count += 1
                if count == 1:
                    if r != 0 and r1[r - 1] == "free":
                        checkLeft = True
                        left = r - 1
                    else:
                        checkLeft = False
            if count < 4 and r1[r] != "p1":
                if r1[r] == "free" and count == 3 and priority < 4:
                    close = "c" + str (r + 1) + " r1"
                    if r2[r] == "free":
                        priority = 2
                    else:
                        priority = 4
                elif count == 3 and checkLeft and priority < 4:
                    close = "c" + str (left + 1) + " r1"
                    if r2[left] == "free":
                        priority = 2
                    else:
                        priority = 4
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for r in range (7):
            if r2[r] == "p1":
                count += 1
                if count == 1:
                    if r != 0 and r2[r - 1] == "free":
                        checkLeft = True
                        left = r - 1
                    else:
                        checkLeft = False
            if count < 4 and r2[r] != "p1":
                if r2[r] == "free" and count == 3 and priority < 4:
                    close = "c" + str (r + 1) + " r2"
                    if r3[r] == "free":
                        priority = 2
                    else:
                        priority = 4
                elif count == 3 and checkLeft and priority < 4:
                    close = "c" + str (left + 1) + " r2"
                    if r3[left] == "free":
                        priority = 2
                    else:
                        priority = 4
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for r in range (7):
            if r3[r] == "p1":
                count += 1
                if count == 1:
                    if r != 0 and r3[r - 1] == "free":
                        checkLeft = True
                        left = r - 1
                    else:
                        checkLeft = False
            if count < 4 and r3[r] != "p1":
                if r3[r] == "free" and count == 3 and priority < 4:
                    close = "c" + str (r + 1) + " r3"
                    if r4[r] == "free":
                        priority = 2
                    else:
                        priority = 4
                elif count == 3 and checkLeft and priority < 4:
                    close = "c" + str (left + 1) + " r3"
                    if r4[left] == "free":
                        priority = 2
                    else:
                        priority = 4
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for r in range (7):
            if r4[r] == "p1":
                count += 1
                if count == 1:
                    if r != 0 and r4[r - 1] == "free":
                        checkLeft = True
                        left = r - 1
                    else:
                        checkLeft = False
            if count < 4 and r4[r] != "p1":
                if r4[r] == "free" and count == 3 and priority < 4:
                    close = "c" + str (r + 1) + " r4"
                    if r5[r] == "free":
                        priority = 2
                    else:
                        priority = 4
                elif count == 3 and checkLeft and priority < 4:
                    close = "c" + str (left + 1) + " r4"
                    if r5[left] == "free":
                        priority = 2
                    else:
                        priority = 4
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for r in range (7):
            if r5[r] == "p1":
                count += 1
                if count == 1:
                    if r != 0 and r5[r - 1] == "free":
                        checkLeft = True
                        left = r - 1
                    else:
                        checkLeft = False
            if count < 4 and r5[r] != "p1":
                if r5[r] == "free" and count == 3 and priority < 4:
                    close = "c" + str (r + 1) + " r5"
                    if r6[r] == "free":
                        priority = 2
                    else:
                        priority = 4
                elif count == 3 and checkLeft and priority < 4:
                    close = "c" + str (left + 1) + " r5"
                    if r6[left] == "free":
                        priority = 2
                    else:
                        priority = 4
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for r in range (7):
            if r6[r] == "p1":
                count += 1
                if count == 1:
                    if r != 0 and r6[r - 1] == "free":
                        checkLeft = True
                        left = r - 1
                    else:
                        checkLeft = False
            if count < 4 and r6[r] != "p1":
                if r6[r] == "free" and count == 3 and priority < 4:
                    close = "c" + str (r + 1) + " r6"
                    priority = 4
                elif count == 3 and checkLeft and priority < 4:
                    close = "c" + str (left + 1) + " r6"
                    priority = 4
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    #Player 2 Horizontal
    if not gameOver:
        count2 = 0
        for r in range (7):
            if r1[r] == "p2":
                count2 += 1
                if count2 == 1:
                    if r != 0 and r1[r - 1] == "free":
                        checkLeft = True
                        left2 = r - 1
                    else:
                        checkLeft = False
            if count2 < 4 and r1[r] != "p2":
                if r1[r] == "free" and count == 3 and priority2 < 1:
                    close2 = "c" + str (r + 1) + " r1"
                    if r2[r] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                elif count == 3 and checkLeft and priority2 < 1:
                    close2 = "c" + str (left2 + 1) + " r1"
                    if r2[left2] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for r in range (7):
            if r2[r] == "p2":
                count2 += 1
                if count2 == 1:
                    if r != 0 and r2[r - 1] == "free":
                        checkLeft = True
                        left2 = r - 1
                    else:
                        checkLeft = False
            if count2 < 4 and r2[r] != "p2":
                if r2[r] == "free" and count == 3 and priority2 < 1:
                    close2 = "c" + str (r + 1) + " r2"
                    if r3[r] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                elif count == 3 and checkLeft and priority2 < 1:
                    close2 = "c" + str (left2 + 1) + " r2"
                    if r3[left2] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for r in range (7):
            if r3[r] == "p2":
                count2 += 1
                if count2 == 1:
                    if r != 0 and r3[r - 1] == "free":
                        checkLeft = True
                        left2 = r - 1
                    else:
                        checkLeft = False
            if count2 < 4 and r3[r] != "p2":
                if r3[r] == "free" and count == 3 and priority2 < 1:
                    close2 = "c" + str (r + 1) + " r3"
                    if r4[r] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                elif count == 3 and checkLeft and priority2 < 1:
                    close2 = "c" + str (left2 + 1) + " r3"
                    if r4[left2] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for r in range (7):
            if r4[r] == "p2":
                count2 += 1
                if count2 == 1:
                    if r != 0 and r4[r - 1] == "free":
                        checkLeft = True
                        left2 = r - 1
                    else:
                        checkLeft = False
            if count2 < 4 and r4[r] != "p2":
                if r4[r] == "free" and count == 3 and priority2 < 1:
                    close2 = "c" + str (r + 1) + " r4"
                    if r5[r] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                elif count == 3 and checkLeft and priority2 < 1:
                    close2 = "c" + str (left2 + 1) + " r4"
                    if r5[left2] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for r in range (7):
            if r5[r] == "p2":
                count2 += 1
                if count2 == 1:
                    if r != 0 and r5[r - 1] == "free":
                        checkLeft = True
                        left2 = r - 1
                    else:
                        checkLeft = False
            if count2 < 4 and r5[r] != "p2":
                if r5[r] == "free" and count == 3 and priority2 < 1:
                    close2 = "c" + str (r + 1) + " r5"
                    if r6[r] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                elif count == 3 and checkLeft and priority2 < 1:
                    close2 = "c" + str (left2 + 1) + " r5"
                    if r6[left2] == "free":
                        priority2 = 0
                    else:
                        priority2 = 1
                count2 = 0
            if count2 >= 4:
                winner = "p2"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count2 = 0
        for r in range (7):
            if r6[r] == "p2":
                count2 += 1
                if count2 == 1:
                    if r != 0 and r6[r - 1] == "free":
                        checkLeft = True
                        left2 = r - 1
                    else:
                        checkLeft = False
            if count2 < 4 and r6[r] != "p2":
                if r6[r] == "free" and count == 3 and priority2 < 1:
                    close2 = "c" + str (r + 1) + " r6"
                    priority2 = 1
                elif count == 3 and checkLeft and priority2 < 1:
                    close2 = "c" + str (left2 + 1) + " r6"
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
        count = 0
        for d in range (3):
            if c1[d] == "p1":
                count += 1
            if c2[d + 1] == "p1":
                count +=1
            if c3[d + 2] == "p1":
                count +=1
            if c4[d + 3] == "p1":
                count +=1
            if c4[d + 3] == "free" and count == 3 and priority < 3:
                close = "c4[" + str (d + 3) + "]"
                if c4[d + 2] == "free":
                    priority = 1
                else:
                    priority = 3
            elif c1[d] == "free" and count == 3 and priority < 3:
                close = "c1[" + str (d) + "]"
                if d == 0:
                    priority = 3
                else:
                    if c1[d - 1] == "free":
                        priority = 1
                    else:
                        priority = 3
            if count < 4:
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for d in range (3):
            if c2[d] == "p1":
                count += 1
            if c3[d + 1] == "p1":
                count +=1
            if c4[d + 2] == "p1":
                count +=1
            if c5[d + 3] == "p1":
                count +=1
            if c5[d + 3] == "free" and count == 3 and priority < 3:
                close = "c5[" + str (d + 3) + "]"
                if c5[d + 2] == "free":
                    priority = 1
                else:
                    priority = 3
            elif c2[d] == "free" and count == 3 and priority < 3:
                close = "c2[" + str (d) + "]"
                if d == 0:
                    priority = 3
                else:
                    if c2[d - 1] == "free":
                        priority = 1
                    else:
                        priority = 3
            if count < 4:
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for d in range (3):
            if c3[d] == "p1":
                count += 1
            if c4[d + 1] == "p1":
                count +=1
            if c5[d + 2] == "p1":
                count +=1
            if c6[d + 3] == "p1":
                count +=1
            if c6[d + 3] == "free" and count == 3 and priority < 3:
                close = "c6[" + str (d + 3) + "]"
                if c6[d + 2] == "free":
                    priority = 1
                else:
                    priority = 3
            elif c3[d] == "free" and count == 3 and priority < 3:
                close = "c3[" + str (d) + "]"
                if d == 0:
                    priority = 3
                else:
                    if c3[d - 1] == "free":
                        priority = 1
                    else:
                        priority = 3
            if count < 4:
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for d in range (3):
            if c4[d] == "p1":
                count += 1
            if c5[d + 1] == "p1":
                count +=1
            if c6[d + 2] == "p1":
                count +=1
            if c7[d + 3] == "p1":
                count +=1
            if c7[d + 3] == "free" and count == 3 and priority < 3:
                close = "c7[" + str (d + 3) + "]"
                if c7[d + 2] == "free":
                    priority = 1
                else:
                    priority = 3
            elif c4[d] == "free" and count == 3 and priority < 3:
                close = "c4[" + str (d) + "]"
                if d == 0:
                    priority = 3
                else:
                    if c4[d - 1] == "free":
                        priority = 1
                    else:
                        priority = 3
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
        count2 = 0
        for d in range (3):
            if c1[d] == "p2":
                count2 += 1
            if c2[d + 1] == "p2":
                count2 +=1
            if c3[d + 2] == "p2":
                count2 +=1
            if c4[d + 3] == "p2":
                count2 +=1
            if c4[d + 3] == "free" and count == 3 and priority2 < 1:
                close2 = "c4[" + str (d + 3) + "]"
                if c4[d + 2] == "free":
                    priority2 = 0
                else:
                    priority2 = 1
            elif c1[d] == "free" and count == 3 and priority2 < 1:
                close2 = "c1[" + str (d) + "]"
                if d == 0:
                    priority2 = 1
                else:
                    if c1[d - 1] == "free":
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
    if not gameOver:
        count2 = 0
        for d in range (3):
            if c2[d] == "p2":
                count2 += 1
            if c3[d + 1] == "p2":
                count2 +=1
            if c4[d + 2] == "p2":
                count2 +=1
            if c5[d + 3] == "p2":
                count2 +=1
            if c5[d + 3] == "free" and count == 3 and priority2 < 1:
                close2 = "c5[" + str (d + 3) + "]"
                if c5[d + 2] == "free":
                    priority2 = 0
                else:
                    priority2 = 1
            elif c2[d] == "free" and count == 3 and priority2 < 1:
                close2 = "c2[" + str (d) + "]"
                if d == 0:
                    priority2 = 1
                else:
                    if c2[d - 1] == "free":
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
    if not gameOver:
        count2 = 0
        for d in range (3):
            if c3[d] == "p2":
                count2 += 1
            if c4[d + 1] == "p2":
                count2 +=1
            if c5[d + 2] == "p2":
                count2 +=1
            if c6[d + 3] == "p2":
                count2 +=1
            if c6[d + 3] == "free" and count == 3 and priority2 < 1:
                close2 = "c6[" + str (d + 3) + "]"
                if c6[d + 2] == "free":
                    priority2 = 0
                else:
                    priority2 = 1
            elif c3[d] == "free" and count == 3 and priority2 < 1:
                close2 = "c3[" + str (d) + "]"
                if d == 0:
                    priority2 = 1
                else:
                    if c3[d - 1] == "free":
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
    if not gameOver:
        count2 = 0
        for d in range (3):
            if c4[d] == "p2":
                count2 += 1
            if c5[d + 1] == "p2":
                count2 +=1
            if c6[d + 2] == "p2":
                count2 +=1
            if c7[d + 3] == "p2":
                count2 +=1
            if c7[d + 3] == "free" and count == 3 and priority2 < 1:
                close2 = "c7[" + str (d + 3) + "]"
                if c7[d + 2] == "free":
                    priority2 = 0
                else:
                    priority2 = 1
            elif c4[d] == "free" and count == 3 and priority2 < 1:
                close2 = "c4[" + str (d) + "]"
                if d == 0:
                    priority2 = 1
                else:
                    if c4[d - 1] == "free":
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
        count = 0
        for d in range (3):
            if c7[d] == "p1":
                count += 1
            if c6[d + 1] == "p1":
                count +=1
            if c5[d + 2] == "p1":
                count +=1
            if c4[d + 3] == "p1":
                count +=1
            if c4[d + 3] == "free" and count == 3 and priority < 3:
                close = "c4[" + str (d + 3) + "]"
                if c4[d + 2] == "free":
                    priority = 1
                else:
                    priority = 3
            elif c7[d] == "free" and count == 3 and priority < 3:
                close = "c7[" + str (d) + "]"
                if d == 0:
                    priority = 3
                else:
                    if c7[d - 1] == "free":
                        priority = 1
                    else:
                        priority = 3
            if count < 4:
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for d in range (3):
            if c6[d] == "p1":
                count += 1
            if c5[d + 1] == "p1":
                count +=1
            if c4[d + 2] == "p1":
                count +=1
            if c3[d + 3] == "p1":
                count +=1
            if c3[d + 3] == "free" and count == 3 and priority < 3:
                close = "c3[" + str (d + 3) + "]"
                if c3[d + 2] == "free":
                    priority = 1
                else:
                    priority = 3
            elif c6[d] == "free" and count == 3 and priority < 3:
                close = "c6[" + str (d) + "]"
                if d == 0:
                    priority = 3
                else:
                    if c6[d - 1] == "free":
                        priority = 1
                    else:
                        priority = 3
            if count < 4:
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for d in range (3):
            if c5[d] == "p1":
                count += 1
            if c4[d + 1] == "p1":
                count +=1
            if c3[d + 2] == "p1":
                count +=1
            if c2[d + 3] == "p1":
                count +=1
            if c2[d + 3] == "free" and count == 3 and priority < 3:
                close = "c2[" + str (d + 3) + "]"
                if c2[d + 2] == "free":
                    priority = 1
                else:
                    priority = 3
            elif c5[d] == "free" and count == 3 and priority < 3:
                close = "c5[" + str (d) + "]"
                if d == 0:
                    priority = 3
                else:
                    if c5[d - 1] == "free":
                        priority = 1
                    else:
                        priority = 3
            if count < 4:
                count = 0
            if count >= 4:
                winner = "p1"
                gameOver = True
            else:
                gameOver = False
                winner = "none"
    if not gameOver:
        count = 0
        for d in range (3):
            if c4[d] == "p1":
                count += 1
            if c3[d + 1] == "p1":
                count +=1
            if c2[d + 2] == "p1":
                count +=1
            if c1[d + 3] == "p1":
                count +=1
            if c1[d + 3] == "free" and count == 3 and priority < 3:
                close = "c1[" + str (d + 3) + "]"
                if c1[d + 2] == "free":
                    priority = 1
                else:
                    priority = 3
            elif c4[d] == "free" and count == 3 and priority < 3:
                close = "c4[" + str (d) + "]"
                if d == 0:
                    priority = 3
                else:
                    if c4[d - 1] == "free":
                        priority = 1
                    else:
                        priority = 3
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
        count2 = 0
        for d in range (3):
            if c7[d] == "p2":
                count2 += 1
            if c6[d + 1] == "p2":
                count2 +=1
            if c5[d + 2] == "p2":
                count2 +=1
            if c4[d + 3] == "p2":
                count2 +=1
            if c4[d + 3] == "free" and count == 3 and priority2 < 1:
                close2 = "c4[" + str (d + 3) + "]"
                if c4[d + 2] == "free":
                    priority2 = 0
                else:
                    priority2 = 1
            elif c7[d] == "free" and count == 3 and priority2 < 1:
                close2 = "c7[" + str (d) + "]"
                if d == 0:
                    priority2 = 1
                else:
                    if c7[d - 1] == "free":
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
    if not gameOver:
        count2 = 0
        for d in range (3):
            if c6[d] == "p2":
                count2 += 1
            if c5[d + 1] == "p2":
                count2 +=1
            if c4[d + 2] == "p2":
                count2 +=1
            if c3[d + 3] == "p2":
                count2 +=1
            if c3[d + 3] == "free" and count == 3 and priority2 < 1:
                close2 = "c3[" + str (d + 3) + "]"
                if c3[d + 2] == "free":
                    priority2 = 0
                else:
                    priority2 = 1
            elif c6[d] == "free" and count == 3 and priority2 < 1:
                close2 = "c6[" + str (d) + "]"
                if d == 0:
                    priority2 = 1
                else:
                    if c6[d - 1] == "free":
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
    if not gameOver:
        count2 = 0
        for d in range (3):
            if c5[d] == "p2":
                count2 += 1
            if c4[d + 1] == "p2":
                count2 +=1
            if c3[d + 2] == "p2":
                count2 +=1
            if c2[d + 3] == "p2":
                count2 +=1
            if c2[d + 3] == "free" and count == 3 and priority2 < 1:
                close2 = "c2[" + str (d + 3) + "]"
                if c2[d + 2] == "free":
                    priority2 = 0
                else:
                    priority2 = 1
            elif c5[d] == "free" and count == 3 and priority2 < 1:
                close2 = "c5[" + str (d) + "]"
                if d == 0:
                    priority2 = 1
                else:
                    if c5[d - 1] == "free":
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
    if not gameOver:
        count2 = 0
        for d in range (3):
            if c4[d] == "p2":
                count2 += 1
            if c3[d + 1] == "p2":
                count2 +=1
            if c2[d + 2] == "p2":
                count2 +=1
            if c1[d + 3] == "p2":
                count2 +=1
            if c1[d + 3] == "free" and count == 3 and priority2 < 1:
                close2 = "c1[" + str (d + 3) + "]"
                if c1[d + 2] == "free":
                    priority2 = 0
                else:
                    priority2 = 1
            elif c4[d] == "free" and count == 3 and priority2 < 1:
                close2 = "c4[" + str (d) + "]"
                if d == 0:
                    priority2 = 1
                else:
                    if c4[d - 1] == "free":
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
            if r1[space] == "free":
                gameOver = False
                winner = "none"
                break
            gameOver = True
            winner = "none"
    return gameOver,winner,close,priority,close2,priority2

#Main
again = "Y"

while again.upper() == "Y":

    if sys.platform.startswith('win32'):
        os.system('cls')
    else:
        os.system('clear')

    c1 = ["free","free","free","free","free","free"]
    c2 = ["free","free","free","free","free","free"]
    c3 = ["free","free","free","free","free","free"]
    c4 = ["free","free","free","free","free","free"]
    c5 = ["free","free","free","free","free","free"]
    c6 = ["free","free","free","free","free","free"]
    c7 = ["free","free","free","free","free","free"]

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
            r1,r2,r3,r4,r5,r6 = updateBoard()
            gameOver,winner,close,priority,close2,priority2 = checkGameOver(r1,r2,r3,r4,r5,r6)
            if gameOver:
                break
            time.sleep (0.5)
            comp = random.randint (1,7)
            if dif == "norm":
                comp = normMode(r1,comp,close,priority,close2,priority2)
            else:
                comp = validColumn(comp)
            r1,r2,r3,r4,r5,r6 = updateBoard()
            gameOver,winner,close,priority,close2,priority2 = checkGameOver(r1,r2,r3,r4,r5,r6)
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
            r1,r2,r3,r4,r5,r6 = updateBoard()
            gameOver,winner,close,priority,close2,priority2 = checkGameOver(r1,r2,r3,r4,r5,r6)
            if gameOver:
                break
            player = 2
            choice2 = input (bcolors.GREEN + "\nPlayer 2 column: " + bcolors.ENDC)
            choice2 = validChoice(choice2,player)
            r1,r2,r3,r4,r5,r6 = updateBoard()
            gameOver,winner,close,priority,close2,priority2 = checkGameOver(r1,r2,r3,r4,r5,r6)
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
