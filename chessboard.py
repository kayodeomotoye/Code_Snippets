WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    num_len = size // 2
    for line in range(size):
        if line % 2 == 0:
            print(f'{WHITE}{BLACK}' * num_len)
        else:
             print(f'{BLACK}{WHITE}'  * num_len)


create_chessboard(size=8)