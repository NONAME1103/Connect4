from sys import platform
from os import system
from random import choice, shuffle
from time import sleep
from optparse import OptionParser

class colours():
    def __init__ (self):
        self.end       = '\033[0m'
        self.bold      = '\033[;1m'
        self.red       = '\033[91m' if not highCon else '\033[31m'
        self.yellow    = '\033[93m' if not highCon else '\033[36m'
        self.grey      = '\033[90m'
        self.white     = '\033[38;2;255;255;255m'
        self.green     = '\033[92m'
        self.blink     = '\033[;;5m'

    def colourTest(self):
        print (f"{self.red}Lol red{self.end} {self.bold}Lol bold{self.end} {self.yellow}Lol yellow{self.end} {self.grey}Lol grey{self.end} {self.white}Lol white{self.end} {self.green}Lol green{self.end} {self.blink}Lol blink{self.end} {self.end}Oof normal")


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
        playerNum = input (c.green + "\nChoice: " + c.end)
        if playerNum in ["1", "2"]:
            ai = True if playerNum == "1" else False
        else:
            print (c.red + "\nInvalid choice!\n" + c.end)
            sleep(0.5)
            return self.title()
        return ai

    def diffSelect(self):
        print(c.yellow + '''
    Choose a Difficulty:
    1) Easy
    2) Normal
    3) Hard
    ''' + c.end + '--------------------------------------------------------------')
        difficulty = input (c.green + "\nChoice: " + c.end)
        if difficulty in ["1", "2", "3"]:
            return difficulty
        else:
            print (c.red + "\nInvalid choice!\n" + c.end)
            sleep(0.5)
            return self.diffSelect()

    def colourSelect(self):
        if not highCon:
            print(c.yellow + '''
            Choose a Colour:
            1) Red
            2) Yellow
            NOTE: Red moves first
            ''' + c.end + '--------------------------------------------------------------')
        else:
            print(c.yellow + '''
            Choose a Colour:
            1) Red
            2) Cyan
            NOTE: Red moves first
            ''' + c.end + '--------------------------------------------------------------')
        playerColour = input (c.green + "\nChoice: " + c.end)
        if playerColour in ["1", "2"]:
            return playerColour
        else:
            print (c.red + "\nInvalid choice!\n" + c.end)
            sleep(0.5)
            return self.colourSelect()

    def printBoard(self):
        char = "◉" if not ascii else "■"
        count = 0
        over, cells = self.checkGameOver(cells = True)
        print ("")
        if not ascii:
            print (c.grey + "       |  " + c.end, end = "")
        else:
            print (c.grey + "       |  " + c.end, end = "")
        for row in self.board:
            for space in range (len(row)):
                if over and (count, space) in cells:
                    print (c.blink, end = "")
                if row[space] == "free":
                    print (c.white + f"{char}  " + c.end, end = "")
                elif row[space] == "p1":
                    print (c.red + f"{char}  " + c.end, end = "")
                elif row[space] == "p2":
                    print (c.yellow + f"{char}  " + c.end, end = "")
            print (c.grey + "|" + c.end)
            count += 1
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

    def checkGameOver(self, board = None, close = False, cells = False):
        if board == None:
            board = self.board
        gameOver = False
        winner = None
        if close:
            max4s = 0
            max3s = 0
            max2s = 0
            min4s = 0
            min3s = 0
            min2s = 0
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
                if close and count1 == 2:
                    max2s += 1
                if close and count1 == 3:
                    max3s += 1
                if close and count1 == 4:
                    max4s += 1
                if close and count2 == 2:
                    min2s += 1
                if close and count2 == 3:
                    min3s += 1
                if close and count2 == 4:
                    min4s += 1
                if count1 >= 4:
                    gameOver = True
                    winner = "p1"
                    if cells:
                        return gameOver, [(row, col - c) for c in range (4)]
                    return gameOver, winner
                elif count2 >= 4:
                    gameOver = True
                    winner = "p2"
                    if cells:
                        return gameOver, [(row, col - c) for c in range (4)]
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
                    if close and count1 == 2:
                        max2s += 1
                    if close and count1 == 3:
                        max3s += 1
                    if close and count1 == 4:
                        max4s += 1
                    if close and count2 == 2:
                        min2s += 1
                    if close and count2 == 3:
                        min3s += 1
                    if close and count2 == 4:
                        min4s += 1
                    if count1 >= 4:
                        gameOver = True
                        winner = "p1"
                        if cells:
                            return gameOver, [(row - c, col) for c in range (4)]
                        return gameOver, winner
                    elif count2 >= 4:
                        gameOver = True
                        winner = "p2"
                        if cells:
                            return gameOver, [(row - c, col) for c in range (4)]
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
                        if close and count1 == 2:
                            max2s += 1
                        if close and count1 == 3:
                            max3s += 1
                        if close and count1 == 4:
                            max4s += 1
                        if close and count2 == 2:
                            min2s += 1
                        if close and count2 == 3:
                            min3s += 1
                        if close and count2 == 4:
                            min4s += 1
                        if count1 >= 4:
                            gameOver = True
                            winner = "p1"
                            if cells:
                                if time == 0:
                                    return gameOver, [(row + c, col - c) for c in range (4)]
                                return gameOver, [(row + c, col + c) for c in range (4)]
                            return gameOver, winner
                        elif count2 >= 4:
                            gameOver = True
                            winner = "p2"
                            if cells:
                                if time == 0:
                                    return gameOver, [(row + c, col - c) for c in range (4)]
                                return gameOver, [(row + c, col + c) for c in range (4)]
                            return gameOver, winner
        # Checks for a full board
        if not gameOver:
            free = [cell for cell in board[0] if cell == "free"]
            if len(free) == 0:
                gameOver = True
                winner = None
        # Returns the dictionaries of cells that would benefit each player
        if close:
            return max4s, max3s, max2s, min4s, min3s, min2s
        if cells:
            return gameOver, []
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
            return 10000 if win == "p1" else -10000 if win == "p2" else 0

    def move(self, difficulty, board):
        boardCopy = [[cell for cell in row] for row in board]
        actions = self.getActions(boardCopy)
        if difficulty == "1":
            action = choice(list(actions))
            sleep(0.5)
        elif difficulty == "2":
            player = game.player(board)
            depth = 4
            action = self.minimax(boardCopy, depth, -float("inf"), float("inf"), player == 1)[0]
            sleep(0.3)
        else:
            player = game.player(board)
            depth = 6
            action = self.minimax(boardCopy, depth, -float("inf"), float("inf"), player == 1)[0]
            sleep(0.2)
        return action

    def minimax(self, board, depth, alpha, beta, maxPlayer):
        over, winner = game.checkGameOver(board)
        if over:
            return None, self.utility(board)
        if depth == 0:
            return None, self.evaluation(board)
        if maxPlayer:
            val = -float("inf")
            col = choice(list(self.getActions(board)))
            moves = list(self.getActions(board))
            shuffle(moves)
            for move in moves:
                boardCopy = [[cell for cell in row] for row in board]
                newVal = self.minimax(self.result(boardCopy, move), depth - 1, alpha, beta, False)[1]
                if newVal > val:
                    val = newVal
                    col = move
                alpha = max(alpha, val)
                if alpha >= beta:
                    break
            return col, val
        else:
            val = float("inf")
            moves = list(self.getActions(board))
            shuffle(moves)
            for move in moves:
                boardCopy = [[cell for cell in row] for row in board]
                newVal = self.minimax(self.result(boardCopy, move), depth - 1, alpha, beta, True)[1]
                if newVal < val:
                    val = newVal
                    col = move
                beta = min(beta, val)
                if alpha >= beta:
                    break
            return col, val

    def evaluation(self, board):
        over, winner = game.checkGameOver(board)
        if over: return self.utility(board)
        max4s, max3s, max2s, min4s, min3s, min2s = game.checkGameOver(board, close = True)
        val = ((max4s * 100) + (max3s * 10) + max2s) - ((min4s * 100) + (min3s * 10) + min2s)
        return val


def clear():
    if platform.startswith('win32'):
        system('cls')
    else:
        system('clear')


if __name__ == "__main__":
    try:
        bot = bot()
        parser = OptionParser()
        parser.add_option('-a', '--ascii', default = False, action = 'store_true', dest = 'ascii', help='This changes the game piece into a (less-fitting) ascii character. Use if the game piece is an invalid character')
        parser.add_option('--hc', '--high-contrast', default = False, action = 'store_true', dest = 'highCon', help='This changes the player colours into (less-fitting) more visible colours. Use if the game pieces are difficult to see')
        (options, argument) = parser.parse_args()
        ascii = options.ascii
        highCon = options.highCon
        c = colours()
        playing = True
        while playing:
            clear()
            # c.colourTest()
            game = connect4()
            ai = game.title()
            if ai:
                difficulty = game.diffSelect()
                playerColour = game.colourSelect()
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
                clear()
                if gameOver:
                    clear()
                    game.printBoard()
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
