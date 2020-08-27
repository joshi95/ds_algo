def isSafe(x, y, chessboard, n):
    # check if not queen is present in right diagnol
    # check if no queen is present in vertical direction
    # check if no queen is present in left dianol
    # check if 

    _x = x - 1
    _y = y + 1
    while _x >= 0 and _y < n:
        if chessboard[_x][_y] == 'Q':
            return False
        _x -= 1
        _y += 1

    _x = x + 1
    _y = y - 1

    while _x < n and _y >= 0:
        if chessboard[_x][_y] == 'Q':
            return False
        _x += 1
        _y -= 1

    _x = x - 1
    _y = y - 1

    while _x >= 0 and _y >= 0:
        if chessboard[_x][_y] == 'Q':
            return False
        _x -= 1
        _y -= 1

    _x = x + 1
    _y = y + 1

    while _x < n and _y < n:
        if chessboard[_x][_y] == 'Q':
            return False
        _x += 1
        _y += 1

    _x = x - 1
    _y = y
    while _x >= 0:
        if chessboard[_x][_y] == 'Q':
            return False
        _x -= 1

    _x = x + 1
    _y = y
    while _x < n:
        if chessboard[_x][_y] == 'Q':
            return False
        _x += 1
    
    return True



def solve(chessboard, row, size_of_chessboard):
    if row == size_of_chessboard:
        print(chessboard)
        return

    for i in range(size_of_chessboard):
        if isSafe(row, i, chessboard, size_of_chessboard):
            chessboard[row][i] = 'Q'
            solve(chessboard, row + 1, size_of_chessboard)
            chessboard[row][i] = '.'


n = 4
chessboard = [['.' for _ in range(n)] for _ in range(n)]
solve(chessboard, 0, n)