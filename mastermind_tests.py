from mastermind import Board
from bcolors import bcolors


def _assert_equal(ref,  o1, o2):
    print bcolors.HEADER + '-- ' + str(ref) + '. ' + '-'*65 + bcolors.ENDC
    print "  actual:", o1
    print "expected:", o2
    r = (o1 == o2)
    if r:
        print bcolors.OKGREEN + "OK" + bcolors.ENDC
    else:
        print bcolors.WARNING + "FAIL" + bcolors.ENDC

def run_tests():
    board = Board()
    _assert_equal(0, board._make_color_count(["RED", "YELLOW", "RED", "ORANGE"]), {"RED": 2, "YELLOW": 1, "ORANGE": 1})
    _assert_equal(1, board._make_color_count(["RED", "YELLOW", "GREEN", "ORANGE"]), {"RED": 1, "YELLOW": 1, "GREEN": 1, "ORANGE": 1})
    _assert_equal(2, board._make_color_count(["RED", "RED", "RED"]), {"RED": 3})
    _assert_equal(3, board._make_color_count(["RED"]), {"RED": 1})

    board.goal = ["RED", "YELLOW", "GREEN", "ORANGE"]
    board.goal_color_count = {"RED": 1, "YELLOW": 1, "GREEN": 1, "ORANGE": 1}
    _assert_equal(4, board.check(["RED", "YELLOW", "GREEN", "ORANGE"]), ["CORRECT_PLACE", "CORRECT_PLACE", "CORRECT_PLACE", "CORRECT_PLACE"])
    _assert_equal(5, board.check(["RED", "YELLOW", "NOPE", "NO"]), ["CORRECT_PLACE", "CORRECT_PLACE"])
    _assert_equal(6, board.check(["NOPE", "NO", "RED", "YELLOW"]), ["CORRECT_COLOR", "CORRECT_COLOR"])
    _assert_equal(7, board.check(["RED", "GREEN", "YELLOW", "ORANGE"]), ["CORRECT_PLACE", "CORRECT_PLACE", "CORRECT_COLOR", "CORRECT_COLOR"])

    board.goal = ["RED", "YELLOW", "RED", "YELLOW"]
    board.goal_color_count = {"RED": 2, "YELLOW": 2}
    _assert_equal(8, board.check(["RED", "YELLOW", "RED", "YELLOW"]), ["CORRECT_PLACE", "CORRECT_PLACE", "CORRECT_PLACE", "CORRECT_PLACE"])
    _assert_equal(9, board.check(["GREEN", "YELLOW", "RED", "ORANGE"]), ["CORRECT_PLACE", "CORRECT_PLACE"])
    _assert_equal(10,board.check(["RED", "YELLOW", "YELLOW", "YELLOW"]), ["CORRECT_PLACE", "CORRECT_PLACE", "CORRECT_PLACE"])
    _assert_equal(11,board.check(["RED", "YELLOW", "YELLOW", "RED"]), ["CORRECT_PLACE", "CORRECT_PLACE", "CORRECT_COLOR", "CORRECT_COLOR"])
    _assert_equal(12,board.check(["YELLOW", "RED", "YELLOW", "RED"]), ["CORRECT_COLOR", "CORRECT_COLOR", "CORRECT_COLOR", "CORRECT_COLOR"])
    _assert_equal(13,board.check(["YELLOW", "GREEN", "YELLOW", "RED"]), ["CORRECT_COLOR", "CORRECT_COLOR", "CORRECT_COLOR"])
    _assert_equal(14,board.check(["BLACK", "BLUE", "YELLOW", "RED"]), ["CORRECT_COLOR", "CORRECT_COLOR"])

    board.goal = ["RED", "WHITE", "RED", "BLACK"]
    board.goal_color_count = {"RED": 2, "WHITE": 1, "BLACK": 1}
    _assert_equal(15, board.check(["BLACK", "BLACK", "WHITE", "WHITE"]), ["CORRECT_COLOR", "CORRECT_COLOR"])


if __name__ == "__main__":
    run_tests()
