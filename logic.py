# logic for tic-tac-toe game. Modified from code I finished on February-20-2024
# new and improved tic-tac-toe
# and using just generally better code :)
def checkwin(sq, x):
    winner = ''

    if x == 1:
        winner = 'Player'
    elif x == 2:
        winner = 'CPU'

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
        return 0, 0


def gameover(sq):
    check = 0
    for row in sq:
        if 0 not in row:
            check += 1
    if check == 3:
        return 1, 'Nobody'

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
        for i in range(3):
            # horiz
            if [0, k, k] == sq[i]:
                return converting(sq, i, 0, 2)
            elif [k, 0, k] == sq[i]:
                return converting(sq, i, 1, 2)
            elif [k, k, 0] == sq[i]:
                return converting(sq, i, 2, 2)

            # verts
            if sq[1][i] == sq[2][i] == k and sq[0][i] == 0:
                return converting(sq, 0, i, 2)
            elif sq[0][i] == sq[2][i] == k and sq[1][i] == 0:
                return converting(sq, 1, i, 2)
            elif sq[0][i] == sq[1][i] == k and sq[2][i] == 0:
                return converting(sq, 2, i, 2)

        # diag
        if sq[2][2] == sq[1][1] == k and sq[0][0] == 0:
            return converting(sq, 0, 0, 2)
        elif sq[2][0] == sq[1][1] == k and sq[0][2] == 0:
            return converting(sq, 0, 2, 2)
        elif sq[0][2] == sq[1][1] == k and sq[2][0] == 0:
            return converting(sq, 2, 0, 2)
        elif sq[0][0] == sq[1][1] == k and sq[0][2] == 0:
            return converting(sq, 0, 2, 2)

    # first move
    if sq[0][0] == 0:
        return converting(sq, 0, 0, 2)
    elif sq[0][0] != 0 and sq[1][1] == 0 and sq[2][2] != 1:
        return converting(sq, 1, 1, 2)
    elif sq[0][0] == 2:
        if sq[2][2] == 0:
            return converting(sq, 2, 2, 2)
        elif sq[1][1] == 1 and sq[2][2] == 0:
            return converting(sq, 2, 2, 2)
    elif sq[0][0] == 1 and sq[2][2] == 1 and sq[1][0] == 0:
        return converting(sq, 1, 0, 2)

    for i in range(3):
        for k in range(3):
            if sq[i][k] == 0:
                return converting(sq, i, k, 2)


def playerinput():
    while True:
        usr_input = input('Where would you like to go?: ').strip().upper()

        if len(usr_input) == 2 and usr_input[0] in ['A', 'B', 'C'] and usr_input[1] in ['1', '2', '3']:
            usr_move = usr_input
            break

    if usr_move[0].upper() == 'A':
        usr_move = '0' + str(int(usr_move[1]) - 1)
    elif usr_move[0].upper() == 'B':
        usr_move = '1' + str(int(usr_move[1]) - 1)
    elif usr_move[0].upper() == 'C':
        usr_move = '2' + str(int(usr_move[1]) - 1)

    return usr_move


def converting(sq, x, y, whosturn):
    if sq[x][y] == 0:
        sq[x][y] = whosturn
    else:
        usr_move = playerinput()
        converting(sq, int(usr_move[0]), int(usr_move[1]), whosturn)
    # print(sq)
    return sq


def playermove(sq, whosturn):
    if whosturn == 1:
        usr_move = playerinput()
        sq = converting(sq, int(usr_move[0]), int(usr_move[1]), whosturn)

    elif whosturn == 2:
        if sq[0][0] == 0:
            sq[0][0] = whosturn
            return sq
        else:
            return checkstrat(sq)

    return sq


def printscreen(squares, display):
    for i in display[0][3]:
        print(i, end='')
    print('')

    for row in range(3):
        for column in range(3):
            mem = squares[row][column]
            print(display[mem][row][column], end='')
        print('')


def swap(pfirst):
    if pfirst == 1:
        pfirst = 2
    elif pfirst == 2:
        pfirst = 1
    return pfirst


def boarding(pfirst, sq, dp, turncount):
    while gameover(sq)[0] == 0:
        printscreen(sq, dp)
        sq = playermove(sq, pfirst)
        pfirst = swap(pfirst)
        # print(f'Player turn: {pfirst}')
        turncount += 1

    printscreen(sq, dp)
    print(f'{(gameover(sq))[1]} won')
    choice = ''
    while choice.upper().strip() != 'Y' and choice.upper().strip() != 'N':
        choice = input('Would you like to play again? Y/N: ')
    if choice.upper().strip() == 'Y':
        main()
    else:
        print('Thank you for playing!')


def choose():
    select = ''
    result = 0
    while select != 'Y' and select != 'N':
        select = str(input('Would you like to go first? (Y/N): ')).upper().strip()
    if select == 'Y':
        result = 1
    elif select == 'N':
        result = 2
    return result


def startup():
    squares = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

    display = [[["A     |", "   |", "   "],
                ["B     |", "   |", "   "],
                ["C     |", "   |", "   "],
                ["    1  ", " 2  ", " 3 "]],

               [["A   X |", " X |", " X "],
                ["B   X |", " X |", " x "],
                ["C   X |", " X |", " X "]],

               [["A   O |", " O |", " O "],
                ["B   O |", " O |", " O "],
                ["C   O |", " O |", " O "]]]

    pfirst = choose()
    boarding(pfirst, squares, display, 0)


def main():
    startup()


if __name__ == '__main__':
    main()
