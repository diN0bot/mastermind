from random import randint
import getopt, sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    GREY = '\033[37m'
    BROWN = '\033[38m'

    BACKGROUND_BLACK = '\033[40m'
    BACKGROUND_RED = '\033[41m'
    BACKGROUND_GREEN = '\033[42m'
    BACKGROUND_YELLOW = '\033[43m'
    BACKGROUND_BLUE = '\033[44m'
    BACKGROUND_PURPLE = '\033[45m'
    BACKGROUND_CYAN = '\033[46m'
    BACKGROUND_GREY = '\033[47m'

    DARK_GREY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_PURPLE = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'


class Board:
    CORRECT_COLOR = "CORRECT_COLOR"
    CORRECT_PLACE = "CORRECT_PLACE"
    COLORS = {
        0: bcolors.RED+bcolors.UNDERLINE+"R"+bcolors.ENDC+bcolors.RED+"ed"+bcolors.ENDC,
        1: bcolors.GREEN+bcolors.UNDERLINE+"G"+bcolors.ENDC+bcolors.GREEN+"reen"+bcolors.ENDC,
        2: bcolors.LIGHT_BLUE+"bl"+bcolors.UNDERLINE+"U"+bcolors.ENDC+bcolors.LIGHT_BLUE+"e"+bcolors.ENDC,
        3: bcolors.YELLOW+""+bcolors.UNDERLINE+"Y"+bcolors.ENDC+bcolors.YELLOW+"ellow"+bcolors.ENDC,
        4: bcolors.BACKGROUND_RED+bcolors.LIGHT_YELLOW+"brow"+bcolors.UNDERLINE+"N"+bcolors.ENDC,
        5: bcolors.BACKGROUND_YELLOW+bcolors.LIGHT_RED+bcolors.UNDERLINE+"O"+bcolors.ENDC+bcolors.BACKGROUND_YELLOW+bcolors.LIGHT_RED+"range"+bcolors.ENDC,
        6: bcolors.DARK_GREY+"bl"+bcolors.UNDERLINE+"A"+bcolors.ENDC+bcolors.DARK_GREY+"ck"+bcolors.ENDC,
        7: bcolors.WHITE+bcolors.UNDERLINE+"W"+bcolors.ENDC+bcolors.WHITE+"hite"+bcolors.ENDC,
    }
    COLOR_ABBREVIATIONS = {
        "R": COLORS[0], "RE": COLORS[0],
        "G": COLORS[1], "GR": COLORS[1],
        "U": COLORS[2],
        "Y": COLORS[3], "YE": COLORS[3],
        "N": COLORS[4], "BR": COLORS[4],
        "O": COLORS[5], "OR": COLORS[5],
        "A": COLORS[6],
        "W": COLORS[7], "WH": COLORS[7],
    }

    def __init__(self, num_goal=4, num_colors=8, max_moves=12):
        self.num_goal = num_goal or 4
        self.num_colors = num_colors and min(num_colors, 8) or 8
        self.max_moves = max_moves or 12
        self.moves_made = 0
        self.won = False

        self.goal = []
        for idx in range(0, self.num_goal):
            self.goal.append(self.COLORS[randint(0, self.num_colors-1)])
        self.goal_color_count = self._make_color_count(self.goal)

    def _make_color_count(self, row):
        color_count = {}
        for color in row:
            if color not in color_count:
                color_count[color] = 0
            color_count[color] += 1
        return color_count

    def check(self, guess):
        if len(guess) != self.num_goal:
            raise Exception("Bad guess")

        pegs = []
        guess_color_count = self._make_color_count(guess)
        for color, count in guess_color_count.items():
            if color in self.goal_color_count:
                if count > self.goal_color_count[color]:
                    guess_color_count[color] = self.goal_color_count[color]

        for idx in range(0, self.num_goal):
            if guess[idx] == self.goal[idx]:
                pegs.append(Board.CORRECT_PLACE)
                if guess[idx] in guess_color_count:
                    guess_color_count[guess[idx]] -= 1

        for color, count in guess_color_count.items():
            if count > 0 and color in self.goal_color_count:
                for c in range(0, count):
                    pegs.append(Board.CORRECT_COLOR)
        return pegs

    def _validate(self, raw_guess):
        guess = []
        for g in raw_guess.split(' '):
            g = g.strip().upper()
            if g == '':
                continue
            if g in Board.COLOR_ABBREVIATIONS:
                g = Board.COLOR_ABBREVIATIONS[g]
            try:
                int(g)
            except:
                pass
            else:
                if int(g) in Board.COLORS:
                    g = Board.COLORS[int(g)]
            if g not in Board.COLORS.values():
                raise Exception("BAD GUESS: unknown color " + g)
            guess.append(g)
        if len(guess) != self.num_goal:
            raise Exception("BAD GUESS: wrong number of balls")
        return guess

    def move(self):
        print "\n%s. >" % (self.max_moves - self.moves_made),
        raw_guess = raw_input()
        try:
            guess = self._validate(raw_guess)
        except Exception, e:
            print bcolors.WARNING + str(e) + bcolors.ENDC
            return

        self.moves_made += 1
        for g in guess:
            print g,

        pegs = board.check(guess)
        num_correct = 0
        for p in pegs:
            if p == Board.CORRECT_PLACE:
                print bcolors.OKGREEN + 'X' + bcolors.ENDC,
                num_correct += 1
            if p == Board.CORRECT_COLOR:
                print 'X',
        print

        if num_correct == board.num_goal:
            print bcolors.OKGREEN + "YOU WON !!"
            for g in board.goal:
                print g,
            print
            self.won = True


if __name__ == "__main__":
    raw_args = sys.argv[1:]
    options = "g:c:m:"
    long_options = ["num-goal=", "num-colors=", "max-moves="]

    try:
        num_goal = None
        num_colors = None
        max_moves = None
        arguments, values = getopt.getopt(raw_args, options, long_options)
        for arg, val in arguments:
            if arg in ("-g", "--num-goal"):
                num_goal = int(val)
            elif arg in ("-c", "--num-colors"):
                num_colors = int(val)
            elif arg in ("-m", "--max-moves"):
                max_moves = int(val)
    except:
        header = bcolors.LIGHT_PURPLE
        text = bcolors.LIGHT_YELLOW
        sep = bcolors.LIGHT_CYAN
        args = bcolors.LIGHT_GREEN
        msg = [
            header, "Optional command line arguments",
            '\n',
            args, "  -g",
            sep, ", ",
            args, "--num-goal= ",
            text, "number of balls to guess (default 4)",
            '\n',
            args, "  -c",
            sep, ", ",
            args, "--num-colors= ",
            text, "number of available colors (max 8)",
            '\n',
            args, "  -m",
            sep, ", ",
            args, "--max-moves= ",
            text, "maximum tries to guess secret (default 12)",
            '\n',
            bcolors.ENDC]
        print ''.join(msg)

    board = Board(num_goal=num_goal, num_colors=num_colors, max_moves=max_moves)
    for idx in range(0, board.num_colors):
        print Board.COLORS[idx],
    print "\n%s balls to guess in %s tries" % (board.num_goal, board.max_moves)
    print
    while not board.won and board.moves_made < board.max_moves:
        board.move()
