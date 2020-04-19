from bcolors import bcolors
import getopt, sys
from mastermind import Board


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
