def noOfWays(x, y, dest_x, dest_y):
    if x > dest_x or y > dest_y:
        return 0
    if x == dest_x and y == dest_y:
        return 1
    leftAns = noOfWays(x + 1, y, dest_x, dest_y)
    rightAns = noOfWays(x, y + 1, dest_x, dest_y)
    return leftAns + rightAns



