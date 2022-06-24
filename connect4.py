from sys import platform
from os import system
from random import choice, shuffle
from time import sleep
from optparse import OptionParser


class Colours:
    def __init__(self):
        self.end = '\033[0m'
        self.bold = '\033[;1m'
        self.red = '\033[91m' if not high_con else '\033[31m'
        self.yellow = '\033[93m' if not high_con else '\033[36m'
        self.grey = '\033[90m'
        self.white = '\033[38;2;255;255;255m'
        self.green = '\033[92m'
        self.blink = '\033[;;5m'

    def colour_test(self):
        print(f"{self.red}Red text{self.end} {self.bold}Bold text{self.end} {self.yellow}Yellow text{self.end} "
              f"{self.grey}Grey text{self.end} {self.white}White text{self.end} {self.green}Green text{self.end} "
              f"{self.blink}Blink text{self.end} {self.end}Normal text")
        input(self.yellow + "Press enter to continue..." + self.end)


class Connect4:

    def __init__(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]

    def title(self):
        print(c.white + c.bold + r"""
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
        player_num = input(c.green + "\nChoice: " + c.end)
        if player_num in ["1", "2"]:
            use_bot = True if player_num == "1" else False
        else:
            print(c.red + "\nInvalid choice!\n" + c.end)
            sleep(0.5)
            return self.title()
        return use_bot

    def diff_select(self):
        print(c.yellow + '''
    Choose a Difficulty:
    1) Easy
    2) Normal
    3) Hard
    ''' + c.end + '--------------------------------------------------------------')
        diff = input(c.green + "\nChoice: " + c.end)
        if diff in ["1", "2", "3"]:
            return diff
        else:
            print(c.red + "\nInvalid choice!\n" + c.end)
            sleep(0.5)
            return self.diff_select()

    def colour_select(self):
        colour2 = "Yellow" if not high_con else "Cyan"
        print(c.yellow + f'''
            Choose a Colour:
            1) Red
            2) {colour2}
            NOTE: Red moves first
            ''' + c.end + '--------------------------------------------------------------')
        player_colour = input(c.green + "\nChoice: " + c.end)
        if player_colour in ["1", "2"]:
            return player_colour
        else:
            print(c.red + "\nInvalid choice!\n" + c.end)
            sleep(0.5)
            return self.colour_select()

    def print_board(self):
        char = "◉" if not use_ascii else "■"
        over, cells = self.check_game_over(cells=True)
        print("")
        print(c.grey + "       |  " + c.end, end="")
        for count, row in enumerate(self.board):
            for space in range(7):
                if over and (count, space) in cells:
                    print(c.blink, end="")
                if row[space] == 0:
                    print(c.white + f"{char}  " + c.end, end="")
                elif row[space] == 1:
                    print(c.red + f"{char}  " + c.end, end="")
                elif row[space] == 2:
                    print(c.yellow + f"{char}  " + c.end, end="")
            print(c.grey + "|" + c.end)
            if count != 5:
                print(c.grey + "       |  " + c.end, end="")
        print(c.grey + "     | ------------------------- |" + c.end)
        print(c.grey + "     |    " + c.white + c.bold + "1  2  3  4  5  6  7    " + c.end + c.grey + "|" + c.end)

    def player(self, board=None):
        if board is None:
            board = self.board
        max_count = 0
        min_count = 0
        for row in board:
            for cell in row:
                if cell == 1:
                    max_count += 1
                if cell == 2:
                    min_count += 1
        return 2 if max_count > min_count else 1

    def valid_choice(self, column):
        return column in [str(i + 1) for i in range(7)] and self.board[0][int(column) - 1] == 0

    def move(self, player_action):
        current_player = self.player()
        for row in reversed(self.board):
            if row[player_action - 1] == 0:
                row[player_action - 1] = current_player
                break

    @staticmethod
    def get_counts(cell, max_count, min_count):
        if cell == 1:
            max_count += 1
            min_count = 0
        if cell == 2:
            max_count = 0
            min_count += 1
        if cell == 0:
            max_count = 0
            min_count = 0
        return max_count, min_count

    def check_game_over(self, board=None, utility=False, cells=False):
        if board is None:
            board = self.board
        over = False
        win_player = None
        factors = {"max_count": [0, 0], "min_count": [0, 0]}
        # Checks for a horizontal win
        for row in range(6):
            max_count = 0
            min_count = 0
            for col in range(7):
                max_count, min_count = self.get_counts(board[row][col], max_count, min_count)
                if max_count == 4 or min_count == 4:
                    over = True
                    win_player = 1 if max_count == 4 else 2
                    if cells:
                        return over, [(row, col - cell) for cell in range(4)]
                    return over, win_player
            if utility:
                if max_count >= 2:
                    factors["max_count"][max_count - 2] += 1
                if min_count >= 2:
                    factors["min_count"][min_count - 2] += 1
        # Checks for a vertical win
        for col in range(7):
            max_count = 0
            min_count = 0
            for row in range(6):
                max_count, min_count = self.get_counts(board[row][col], max_count, min_count)
                if max_count == 4 or min_count == 4:
                    over = True
                    win_player = 1 if max_count == 4 else 2
                    if cells:
                        return over, [(row - cell, col) for cell in range(4)]
                    return over, win_player
            if utility:
                if max_count >= 2:
                    factors["max_count"][max_count - 2] += 1
                if min_count >= 2:
                    factors["min_count"][min_count - 2] += 1
        # Checks for a diagonal win
        cols = [n for n in range(7)]
        for side in range(2):
            searched = []
            for i in range(13):
                r = [row if row <= 5 else row - 6 for row in range(i)]
                max_count = 0
                min_count = 0
                way = cols if side == 0 else reversed(cols)
                for row, col in zip(reversed(r), way):
                    if (row, col) in searched:
                        continue
                    searched.append((row, col))
                    max_count, min_count = self.get_counts(board[row][col], max_count, min_count)
                    if max_count == 4 or min_count == 4:
                        over = True
                        win_player = 1 if max_count == 4 else 2
                        if cells:
                            if side == 0:
                                return over, [(row + cell, col - cell) for cell in range(4)]
                            return over, [(row + cell, col + cell) for cell in range(4)]
                        return over, win_player
                if utility:
                    if max_count >= 2:
                        factors["max_count"][max_count - 2] += 1
                    if min_count >= 2:
                        factors["min_count"][min_count - 2] += 1
        # Checks for a full board (draw)
        free = [cell for cell in board[0] if cell == 0]
        if len(free) == 0:
            over = True
        # Returns the dictionary of factors used to calculate the utility of a given board
        if utility:
            return over, win_player, factors
        if cells:
            return over, []
        return over, win_player

    @staticmethod
    def winners(win_player):
        if win_player == 1:
            print(c.white + c.bold + c.bold + r"""
 __          __ _                                _____   _                              __
 \ \        / /(_)                          _   |  __ \ | |                            /_ |
  \ \  /\  / /  _  _ __   _ __    ___  _ __(_)  | |__) || |  __ _  _   _   ___  _ __    | |
   \ \/  \/ /  | || '_ \ | '_ \  / _ \| '__|    |  ___/ | | / _` || | | | / _ \| '__|   | |
    \  /\  /   | || | | || | | ||  __/| |   _   | |     | || (_| || |_| ||  __/| |      | |
     \/  \/    |_||_| |_||_| |_| \___||_|  (_)  |_|     |_| \__,_| \__, | \___||_|      |_|
                                                                    __/ |
                                                                   |___/                   """ + c.end)
        elif win_player == 2:
            print(c.white + c.bold + c.bold + r"""
 __          __ _                                _____   _                              ___
 \ \        / /(_)                          _   |  __ \ | |                            |__  \
  \ \  /\  / /  _  _ __   _ __    ___  _ __(_)  | |__) || |  __ _  _   _   ___  _ __      ) |
   \ \/  \/ /  | || '_ \ | '_ \  / _ \| '__|    |  ___/ | | / _` || | | | / _ \| '__|    / /
    \  /\  /   | || | | || | | ||  __/| |   _   | |     | || (_| || |_| ||  __/| |      / /_
     \/  \/    |_||_| |_||_| |_| \___||_|  (_)  |_|     |_| \__,_| \__, | \___||_|     |____|
                                                                    __/ |
                                                                   |___/                     """ + c.end)
        else:
            print(c.white + c.bold + c.bold + r"""
_____
|  __ \
| |  | | _ __  __ _ __      __
| |  | || '__|/ _` |\ \ /\ / /
| |__| || |  | (_| | \ V  V /
|_____/ |_|   \__,_|  \_/\_/
                           """ + c.end)


class Bot:

    def __init__(self, game):
        self.game = game

    @staticmethod
    def get_actions(board):
        actions = {n for n in range(1, 8)}
        for cell in range(len(board[0])):
            if board[0][cell] != 0:
                actions.remove(cell + 1)
        return actions

    def result(self, board, action_taken):
        for row in reversed(board):
            if row[action_taken - 1] == 0:
                row[action_taken - 1] = self.game.player(board)
                break
        return board

    def move(self, diff, board):
        board_copy = [[cell for cell in row] for row in board]
        if diff == "1":
            actions = self.get_actions(board_copy)
            bot_action = choice(list(actions))
            sleep(0.5)
        elif diff == "2":
            depth = 4
            bot_action = self.minimax(board_copy, depth, -float("inf"), float("inf"), self.game.player(board) == 1)[0]
            sleep(0.3)
        else:
            depth = 6
            bot_action = self.minimax(board_copy, depth, -float("inf"), float("inf"), self.game.player(board) == 1)[0]
            sleep(0.2)
        return bot_action

    def minimax(self, board, depth, alpha, beta, max_player):
        over, win_player = self.game.check_game_over(board)
        if over:
            return None, float("inf") if win_player == 1 else -float("inf") if win_player == 2 else 0
        if depth == 0:
            return None, self.evaluation(board)
        if max_player:
            val = -float("inf")
            col = choice(list(self.get_actions(board)))
            moves = list(self.get_actions(board))
            shuffle(moves)
            for move in moves:
                board_copy = [[cell for cell in row] for row in board]
                new_val = self.minimax(self.result(board_copy, move), depth - 1, alpha, beta, False)[1]
                if new_val > val:
                    val = new_val
                    col = move
                alpha = max(alpha, val)
                if alpha >= beta:
                    break
            return col, val
        else:
            val = float("inf")
            col = choice(list(self.get_actions(board)))
            moves = list(self.get_actions(board))
            shuffle(moves)
            for move in moves:
                board_copy = [[cell for cell in row] for row in board]
                new_val = self.minimax(self.result(board_copy, move), depth - 1, alpha, beta, True)[1]
                if new_val < val:
                    val = new_val
                    col = move
                beta = min(beta, val)
                if alpha >= beta:
                    break
            return col, val

    def evaluation(self, board):
        over, win_player, factors = self.game.check_game_over(board, utility=True)
        if over:
            return float("inf") if win_player == 1 else -float("inf") if win_player == 2 else 0
        return ((factors["max_count"][1] * 10) + factors["max_count"][0]) -\
               ((factors["min_count"][1] * 10) + factors["min_count"][0])


def clear():
    if platform.startswith('win32'):
        system('cls')
    else:
        system('clear')


def main():
    playing = True
    while playing:
        clear()
        game = Connect4()
        ai = game.title()
        player_colour = difficulty = action = winner = bot = None
        if ai:
            difficulty = game.diff_select()
            player_colour = game.colour_select()
            bot = Bot(game)
        game_over = False
        while not game_over:
            game.print_board()
            player = game.player()
            if ai and (int(player_colour) != player):
                action = bot.move(difficulty, game.board)
            else:
                valid = False
                while not valid:
                    action = input(c.green + f"\nPlayer {player} column: " + c.end)
                    valid = game.valid_choice(action)
                    if not valid:
                        print(c.red + "Invalid choice!\n" + c.end)
                        sleep(0.5)
            game.move(int(action))
            game_over, winner = game.check_game_over()
            clear()
            if game_over:
                clear()
                game.print_board()
        game.winners(winner)
        valid = False
        while not valid:
            again = input(c.green + "\nWant to play again? (Y/N): " + c.end)
            if again.upper() in ["Y", "N"]:
                if again.upper() == "N":
                    playing = False
                break
            print(c.red + "\nInvalid choice!\n" + c.end)
            sleep(0.5)


if __name__ == "__main__":
    try:
        parser = OptionParser()
        parser.add_option('-a', '--ascii', default=False, action='store_true', dest='use_ascii',
                          help='This changes the game piece into a blocky ascii character.'
                               'Use this option if the game piece is an invalid character.')
        parser.add_option('--hc', '--high-contrast', default=False, action='store_true', dest='high_con',
                          help='This changes the yellow player colour into more visible colour (cyan).'
                               'Use this option if the game pieces are difficult to see')
        (options, argument) = parser.parse_args()
        use_ascii = options.use_ascii
        high_con = options.high_con
        c = Colours()
        # c.colour_test()
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...\n")
