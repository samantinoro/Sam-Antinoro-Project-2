# logic for tic-tac-toe game. Modified from code I finished on February-20-2024
# new and improved tic-tac-toe
# and using just generally better code :)
def checkwin(sq, x):
    winner = ''

    if x == 1:
        winner = 1
    elif x == 2:
        winner = 2

    # have to check columns separately
    cnt = 0
    for column in range(3):
        cnt = 0
        for row in range(3):
            mem = sq[row][column]
            if mem == x:
                cnt += 1
            if cnt == 3:
                return 1, winner

    if [x, x, x] in sq:
        return 1, winner
    elif x == sq[0][0] == sq[1][1] == sq[2][2]:
        return 1, winner
    elif x == sq[0][2] == sq[1][1] == sq[2][0]:
        return 1, winner
    elif cnt == 3:
        return 1, winner
    else:
        return 0, 3


def gameover(sq):
    check = 0
    for row in sq:
        if 0 not in row:
            check += 1
    if check == 3:
        return 1, 3

    else:
        liste = [checkwin(sq, 1), checkwin(sq, 2)]
        for i in range(2):
            if 1 in liste[i]:
                return 1, liste[i][1]
        return 0, 0


def checkstrat(sq):
    # instant win / lose conditions
    klist = [2, 1]
    # horizs
    for k in klist:
        if sq[0][0] == 0:
            return 0, 0

        for i in range(3):
            # horiz
            if [0, k, k] == sq[i]:
                return i, 0
            elif [k, 0, k] == sq[i]:
                return i, 1
            elif [k, k, 0] == sq[i]:
                return i, 2

            # verts
            if sq[1][i] == sq[2][i] == k and sq[0][i] == 0:
                return 0, i
            elif sq[0][i] == sq[2][i] == k and sq[1][i] == 0:
                return 1, i
            elif sq[0][i] == sq[1][i] == k and sq[2][i] == 0:
                return 2, i
        #print('logic error not horiz or vert')

        # diag
        if sq[2][2] == sq[1][1] == k and sq[0][0] == 0:
            return 0, 0
        elif sq[2][0] == sq[1][1] == k and sq[0][2] == 0:
            return 0, 2
        elif sq[0][2] == sq[1][1] == k and sq[2][0] == 0:
            return 2, 0
        elif sq[0][0] == sq[1][1] == k and sq[2][2] == 0:
            return 2, 2
        #print('logic error not in diag')

    # first move
    if sq[0][0] == 0:
        return 0, 0
    elif sq[0][0] != 0 and sq[1][1] == 0 and sq[2][2] != 1:
        return 1, 1
    elif sq[0][0] == 2:
        if sq[2][2] == 0:
            return 2, 2
        elif sq[1][1] == 1 and sq[2][2] == 0:
            return 2, 2
    elif sq[0][0] == 1 and sq[2][2] == 1 and sq[1][0] == 0:
        return 1, 0
    #print('logic error not in first move')

    for i in range(3):
        for k in range(3):
            if sq[i][k] == 0:
                #print('logic error in random select')
                return i, k



def playermove(sq, row, col, player):
    sq[row][col] = player
    return sq

