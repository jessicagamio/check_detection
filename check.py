"""Given a chessboard with one K and one Q, see if the K can attack the Q.

This function is given coordinates for the king and queen on a chessboard.
These coordinates are given as a letter A-H for the columns and 1-8 for the
row (see below for example):

Queens can move in any direction: horizontally, vertically, or diagonally,
as far as possible.

This function returns True if the king is in the line of attack of the queen.

For example, these boards show the king under attack:

8    . . . . . . . .      . . . . . . . .      . . . . . . . .    8
7    . . . . . . . .      . . . . . . . .      . K . . . . . .    7
6    . . . K . . . Q      . . . . K . . .      . . . . . . . .    6
5    . . . . . . . .      . . . . . . . .      . . . Q . . . .    5
4    . . . . . . . .      . . . . Q . . .      . . . . . . . .    4
3    . . . . . . . .      . . . . . . . .      . . . . . . . .    3
2    . . . . . . . .      . . . . . . . .      . . . . . . . .    2
1    . . . . . . . .      . . . . . . . .      . . . . . . . .    1
     A B C D E F G H      A B C D E F G H      A B C D E F G H

     K=D6, Q=H6           K=E6, Q=E4           K=B7, Q=D5

>>> check("D6", "H6")
True

>>> check("E6", "E4")
True

>>> check("B7", "D5")
True

>>> check("A1", "H8")
True

>>> check("A8", "H1")
True

>>> check("D6", "H7")
False

>>> check("E6", "F4")
False
"""


def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":
    """

    # Make dictionary of column letter to column number
    col_dict = {
                'A':1,
                'B':2,
                'C':3,
                'D':4,
                'E':5,
                'F':6,
                'G':7,
                'H':8
                    }

    # obtain the row and col locations from the king and queen
    k_col = king[0]
    k_row = int(king[1])

    q_col = queen[0]
    q_row = int(queen[1])

    # if king in same row or column as queen. king is under attack
    if k_col == q_col or k_row == q_row:
        return True

    # if king not in same row or column as queen.
    # check for a diagnal attack
    else:
        king_col_num = int(col_dict[k_col])
        queen_col_num = int(col_dict.get(q_col))


        # if king_col_num < queen_col_num:
        #     vertical_spaces = king_col_num - queen_col_num
        # else:
        #     vertical_spaces = queen_col_num - king_col_num

        # if k_row < q_row:
        #     horizontal_spaces = k_row - q_row
        # else:
        #     horizontal_spaces = q_row - k_row


        # use absolute value to get the number of spaces
        vertical_spaces = abs(king_col_num - queen_col_num)
        horizontal_spaces = abs(k_row - q_row)

        # if spaces vertical and horizontal equal they are diagnol
        if vertical_spaces == horizontal_spaces:
            return True
            
    return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EXCELLENT GAME!\n")

