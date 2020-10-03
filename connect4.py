from sys import platform
from os import system
from random import choice, choices, shuffle
from time import sleep
from optparse import OptionParser
# import dill
from sys import exit

class colours():
    def __init__ (self):
        self.end       = '\033[0m'
        self.bold      = '\033[1m'
        self.red       = '\033[91m'
        self.yellow    = '\033[93m'
        self.grey      = '\033[90m'
        self.white     = '\033[38;2;255;255;255m'
        self.green     = '\033[92m'

    def colourTest(self):
        print (f"{self.bold}Bold{self.end} {self.red}Red{self.end} {self.yellow}Yellow{self.end} {self.grey}Grey{self.end} {self.white}White{self.end} {self.green}Green{self.end} {self.end}Normal")


class connect4():
    def __init__ (self):
        self.board = [["free" for col in range (7)] for row in range (6)]

    def title(self):
        print (c.white + c.bold + """
  _____                                  _     _  _
 / ____|                                | |   | || |
| |      ___   _ __   _ __    ___   ___ | |_  | || |_
| |     / _ \ | '_ \ | '_ \  / _ \ / __|| __| |__   _|
| |____| (_) || | | || | | ||  __/| (__ | |_     | |
 \_____|\___/ |_| |_||_| |_| \___| \___| \__|    |_|  """ + c.end)
        print(c.yellow + '''
Choose a Game Mode:
1) 1 player (against computer)
2) 2 players (1v1)
''' + c.end + '--------------------------------------------------------------')
        players = input (c.green + "\nChoice: " + c.end)
        return players

    def printBoard(self):
        char = "◉" if not ascii else "■"
        count = 0
        print ("")
        if not ascii:
            print (c.grey + "       |  " + c.end,end = "")
        else:
            print (c.grey + "       |  " + c.end,end = "")
        for row in self.board:
            count += 1
            for space in range (len (row)):
                if row[space] == "free":
                    print (c.white + c.bold + f"{char}  " + c.end,end = "")
                elif row[space] == "p1":
                    print (c.red + f"{char}  " + c.end,end = "")
                elif row[space] == "p2":
                    print (c.yellow + f"{char}  " + c.end,end = "")
            print (c.grey + "|" + c.end)
            if count != 6:
                if not ascii:
                    print (c.grey + "       |  " + c.end,end = "")
                else:
                    print (c.grey + "       |  " + c.end,end = "")
        if not ascii:
            print (c.grey + "     | ----------------------------- |" + c.end)
            print (c.grey + "     |   " + c.end +  c.white + c.bold + "1   2   3   4   5   6   7   " + c.end + c.grey + "|" + c.end)
        else:
            print (c.grey + "     | ------------------------- |" + c.end)
            print (c.grey + "     |    " + c.end +  c.white + c.bold + "1  2  3  4  5  6  7    " + c.end + c.grey + "|" + c.end)

    def player(self, board = None):
        if board is None:
            board = self.board
        count1 = 0
        count2 = 0
        for row in board:
            for cell in row:
                if cell == "p1": count1 += 1
                if cell == "p2": count2 += 1
        return 2 if count1 > count2 else 1

    def validChoice(self, column):
        valid = False
        message = False
        try:
            column = int (column)
        except ValueError:
            message = True
        else:
            if 1 <= column <= 7:
                if self.board[0][column - 1] == "free":
                    valid = True
                else:
                    message = True
            else:
                message = True
        if message:
            print (c.red + "\nInvalid choice!\n" + c.end)
            sleep(0.5)
            valid = False
        return valid

    def move(self, action):
        player = self.player()
        player = "p1" if player == 1 else "p2"
        for row in reversed(self.board):
            if row[action - 1] == "free":
                row[action - 1] = player
                break

    def checkGameOver(self, board = None, close = False):
        if board == None:
            board = self.board
        gameOver = False
        winner = None
        if close:
            close1 = {}
            close2 = {}
        # Checks for a horizontal win
        for row in range (len (board)):
            count1 = 0
            count2 = 0
            for col in range (len (board[row])):
                cell = board[row][col]
                if cell == "p1":
                    count2 = 0
                    count1 += 1
                if cell == "p2":
                    count1 = 0
                    count2 += 1
                if cell == "free":
                    count1 = 0
                    count2 = 0
                if close and count1 in (2, 3):
                    close1[(row, col + 1)] = count1
                if close and count2 in (2, 3):
                    close2[(row, col + 1)] = count2
                if count1 >= 4:
                    gameOver = True
                    winner = "p1"
                    return gameOver, winner
                elif count2 >= 4:
                    gameOver = True
                    winner = "p2"
                    return gameOver, winner
        # Checks for a vertical win
        if not gameOver:
            for col in range (len (board[0])):
                count1 = 0
                count2 = 0
                for row in range (len (board)):
                    cell = board[row][col]
                    if cell == "p1":
                        count2 = 0
                        count1 += 1
                    if cell == "p2":
                        count1 = 0
                        count2 += 1
                    if cell == "free":
                        count1 = 0
                        count2 = 0
                    if close and count1 in (2, 3):
                        close1[(row + 1, col)] = count1
                    if close and count2 in (2, 3):
                        close2[(row + 1, col)] = count2
                    if count1 >= 4:
                        gameOver = True
                        winner = "p1"
                        return gameOver, winner
                    elif count2 >= 4:
                        gameOver = True
                        winner = "p2"
                        return gameOver, winner
        # Checks for a diagonal win
        if not gameOver:
            cols = [n for n in range (len (board[0]))]
            for time in range (2):
                searched = []
                for c in range (13):
                    r = [row if row <= 5 else row - 6 for row in range (c)]
                    count1 = 0
                    count2 = 0
                    way = cols if time == 0 else reversed(cols)
                    for row, col in zip (reversed(r), way):
                        cell = board[row][col]
                        if (row, col) in searched:
                            continue
                        searched.append((row, col))
                        if cell == "p1":
                            count2 = 0
                            count1 += 1
                        if cell == "p2":
                            count1 = 0
                            count2 += 1
                        if cell == "free":
                            count1 = 0
                            count2 = 0
                        if close and count1 in (2, 3):
                            if time == 0:
                                close1[(row - 1, col + 1)] = count1
                            else:
                                close1[(row - 1, col - 1)] = count1
                        if close and count2 in (2, 3):
                            if time == 0:
                                close2[(row - 1, col + 1)] = count2
                            else:
                                close2[(row - 1, col - 1)] = count2
                        if count1 >= 4:
                            gameOver = True
                            winner = "p1"
                            return gameOver, winner
                        elif count2 >= 4:
                            gameOver = True
                            winner = "p2"
                            return gameOver, winner
        # Checks for a full board
        if not gameOver:
            free = [cell for cell in board[0] if cell == "free"]
            if len(free) == 0:
                gameOver = True
                winner = None
        # Returns the dictionaries of cells that would benefit each player
        if close:
            return close1, close2
        return gameOver, winner

    def winners(self, winner):
        if winner == "p1": print (c.white + c.bold + c.bold + """
 __          __ _                                _____   _                              __
 \ \        / /(_)                          _   |  __ \ | |                            /_ |
  \ \  /\  / /  _  _ __   _ __    ___  _ __(_)  | |__) || |  __ _  _   _   ___  _ __    | |
   \ \/  \/ /  | || '_ \ | '_ \  / _ \| '__|    |  ___/ | | / _` || | | | / _ \| '__|   | |
    \  /\  /   | || | | || | | ||  __/| |   _   | |     | || (_| || |_| ||  __/| |      | |
     \/  \/    |_||_| |_||_| |_| \___||_|  (_)  |_|     |_| \__,_| \__, | \___||_|      |_|
                                                                    __/ |
                                                                   |___/                   """ + c.end)
        elif winner == "p2": print (c.white + c.bold + c.bold + """
 __          __ _                                _____   _                              ___
 \ \        / /(_)                          _   |  __ \ | |                            |__  \\
  \ \  /\  / /  _  _ __   _ __    ___  _ __(_)  | |__) || |  __ _  _   _   ___  _ __      ) |
   \ \/  \/ /  | || '_ \ | '_ \  / _ \| '__|    |  ___/ | | / _` || | | | / _ \| '__|    / /
    \  /\  /   | || | | || | | ||  __/| |   _   | |     | || (_| || |_| ||  __/| |      / /_
     \/  \/    |_||_| |_||_| |_| \___||_|  (_)  |_|     |_| \__,_| \__, | \___||_|     |____|
                                                                    __/ |
                                                                   |___/                     """ + c.end)
        else: print (c.white + c.bold + c.bold + """
_____
|  __ \\
| |  | | _ __  __ _ __      __
| |  | || '__|/ _` |\ \ /\ / /
| |__| || |  | (_| | \ V  V /
|_____/ |_|   \__,_|  \_/\_/
                           """ + c.end)


class bot():
    def getActions(self, board):
        actions = {n for n in range (1, 8)}
        for cell in range (len (board[0])):
            if board[0][cell] != "free":
                actions.remove(cell + 1)
        return actions

    def result(self, board, action):
        player = game.player(board)
        player = "p1" if player == 1 else "p2"
        for row in reversed(board):
            if row[action - 1] == "free":
                row[action - 1] = player
                break
        return board

    def utility(self, board):
        over, win = game.checkGameOver(board)
        if over:
            return 1 if win == "p1" else -1 if win == "p2" else 0

    def move(self, difficulty, board):
        boardCopy = [[cell for cell in row] for row in board]
        actions = self.getActions(boardCopy)
        if difficulty == "1":
            action = choice(list(actions))
            sleep(0.5)
        elif difficulty == "2":
            self.movesAhead = 1000
            self.count = 0
            action = self.minimax(boardCopy)
        return action

    def minimax(self, board):
        over, win = game.checkGameOver(board)
        if over: return None
        player = game.player(board)
        ai = "MAX" if player == 1 else "MIN" if player == 2 else None
        boardCopy = [[cell for cell in row] for row in board]
        if ai == "MAX":
            v = self.MaxValue(boardCopy)
            boardCopy = [[cell for cell in row] for row in board]
            acts = list(self.getActions(board))
            shuffle(acts)
            for action in acts:
                if self.MinValue(self.result(boardCopy, action)) == v:
                    return action
                boardCopy = [[cell for cell in row] for row in board]
            return choice(list(acts))
        elif ai == "MIN":
            v = self.MinValue(boardCopy)
            boardCopy = [[cell for cell in row] for row in board]
            acts = list(self.getActions(board))
            shuffle(acts)
            for action in acts:
                if self.MaxValue(self.result(boardCopy, action)) == v:
                    return action
                boardCopy = [[cell for cell in row] for row in board]
            return choice(list(acts))

    def MaxValue(self, board):
        over, win = game.checkGameOver(board)
        if over: return self.utility(board)
        boardCopy = [[cell for cell in row] for row in board]
        v = -2
        acts = list(self.getActions(board))
        shuffle(acts)
        for action in acts:
            self.count += 1
            if self.count >= self.movesAhead:
                min = self.evaluation(board)
                # print (f"Max moves {self.count} {self.movesAhead}")
            else:
                min = self.MinValue(self.result(board, action))
            v = max (v, min)
            over, win = game.checkGameOver(board)
            if over:
                board = [[cell for cell in row] for row in boardCopy]
                if v == 1: return v
        return v

    def MinValue(self, board):
        over, win = game.checkGameOver(board)
        if over: return self.utility(board)
        boardCopy = [[cell for cell in row] for row in board]
        v = 2
        acts = list(self.getActions(board))
        shuffle(acts)
        for action in acts:
            self.count += 1
            if self.count >= self.movesAhead:
                max = self.evaluation(board)
                # print (f"Max moves {self.count} {self.movesAhead}")
            else:
                max = self.MaxValue(self.result(board, action))
            v = min (v, max)
            over, win = game.checkGameOver(board)
            if over:
                board = [[cell for cell in row] for row in boardCopy]
                if v == -1: return v
        return v

    def evaluation(self, board):
        over, win = game.checkGameOver(board)
        if over: return self.utility(board)
        close1, close2 = game.checkGameOver(board, close = True)
        c1 = len(close1)
        c2 = len(close2)
        try:
            v = (c1 - c2)/(c1 + c2)
        except ZeroDivisionError:
            v = 0
        # from pprint import pprint
        # pprint (board)
        # print ("\nP1")
        # for key in close1:
        #     print (f"{key}: {close1[key]}")
        # print ("\nP2")
        # for key in close2:
        #     print (f"{key}: {close2[key]}")
        # exit()
        return v


def clear():
    if platform.startswith('win32'):
        system('cls')
    else:
        system('clear')


if __name__ == "__main__":
    try:
        c = colours()
        # There are 4,531,985,219,092 total possible games of connect 4
        bot = bot()
        # c.colourTest()
        parser = OptionParser()
        parser.add_option('-a', '--ascii', default = False, action = 'store_true', dest = 'ascii', help='This changes the game piece into a (less-fitting) ascii character. Use if the game piece is an invalid character')
        (options, argument) = parser.parse_args()
        ascii = options.ascii
        playing = True
        while playing:
            clear()
            game = connect4()
            valid = False
            while not valid:
                playerNum = game.title()
                if playerNum in ["1", "2"]:
                    valid = True
                    ai = True if playerNum == "1" else False
                else:
                    print (c.red + "\nInvalid choice!\n" + c.end)
                    sleep(0.5)
            playerColour = 0
            if ai:
                valid = False
                while not valid:
                    print(c.yellow + '''
            Choose a Difficulty:
            1) Easy
            2) Normal (In progress)
            3) Hard (In progress)
            ''' + c.end + '--------------------------------------------------------------')
                    difficulty = input (c.green + "\nChoice: " + c.end)
                    if difficulty in ["1", "2", "3"]:
                        valid = True
                        if difficulty in ["2", "3"]:
                            print (c.yellow + "\nThis difficulty is currently under development.\nThe legacy branch has working implementatiosn of \"Easy\" and \"Normal\" difficulties.\n" + c.end)
                            valid = False
                            continue
                    else:
                        print (c.red + "\nInvalid choice!\n" + c.end)
                        sleep(0.5)
                valid = False
                while not valid:
                    print(c.yellow + '''
                Choose a Colour:
                1) Red
                2) Yellow
                NOTE: Red moves first
                ''' + c.end + '--------------------------------------------------------------')
                    playerColour = input (c.green + "\nChoice: " + c.end)
                    if playerColour in ["1", "2"]:
                        valid = True
                    else:
                        print (c.red + "\nInvalid choice!\n" + c.end)
                        sleep(0.5)
            gameOver = False
            while not gameOver:
                game.printBoard()
                player = game.player()
                if ai and (int(playerColour) != player):
                    action = bot.move(difficulty, game.board)
                else:
                    valid = False
                    while not valid:
                        action = input (c.green + f"\nPlayer {player} column: " + c.end)
                        valid = game.validChoice (action)
                game.move(int(action))
                gameOver, winner = game.checkGameOver()
                if gameOver:
                    clear()
                    game.printBoard()
                    break
                clear()
            game.winners(winner)
            valid = False
            while not valid:
                again = input (c.green + "\nWant to play again? (Y/N): " + c.end)
                if again.upper() in ["Y", "N"]:
                    valid = True
                    if again.upper() == "N":
                        playing = False
                    break
                print (c.red + "\nInvalid choice!\n" + c.end)
                sleep(0.5)
    except KeyboardInterrupt:
        print ("\n\nExiting...\n")
        exit()
