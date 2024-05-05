# logic for tic-tac-toe game. Modified from code I finished on February-20-2024
# new and improved tic-tac-toe
# and using just generally better code :)
class TTTLogic:

    def __init__(self):
        self.sq = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
        self.turn = 0
        self.player = 0
        self.win_count = [0, 0]
        self.game_end = False
        self.temp_win = [0, 0]
        self.final_winner = None

    def set_vars(self):
        self.sq = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
        self.turn = 0
        self.player = 0
        self.game_end = False
        self.temp_win = [0, 0]

    def playermove(self, row, col):
        self.turn += 1
        self.sq[row][col] = self.player
        self.player = 3 - self.player

    def checkstrat(self):
        # instant win / lose conditions
        klist = [2, 1]
        # horizs
        for k in klist:
            if self.sq[0][0] == 0:
                return 0, 0

            for i in range(3):
                # Horiz
                if [0, k, k] == self.sq[i]:
                    return i, 0
                elif [k, 0, k] == self.sq[i]:
                    return i, 1
                elif [k, k, 0] == self.sq[i]:
                    return i, 2

                # Verts
                if self.sq[1][i] == self.sq[2][i] == k and self.sq[0][i] == 0:
                    return 0, i
                elif self.sq[0][i] == self.sq[2][i] == k and self.sq[1][i] == 0:
                    return 1, i
                elif self.sq[0][i] == self.sq[1][i] == k and self.sq[2][i] == 0:
                    return 2, i
            # print('logic error not horiz or vert')

            # diag
            if self.sq[2][2] == self.sq[1][1] == k and self.sq[0][0] == 0:
                return 0, 0
            elif self.sq[2][0] == self.sq[1][1] == k and self.sq[0][2] == 0:
                return 0, 2
            elif self.sq[0][2] == self.sq[1][1] == k and self.sq[2][0] == 0:
                return 2, 0
            elif self.sq[0][0] == self.sq[1][1] == k and self.sq[2][2] == 0:
                return 2, 2
            # print('logic error not in diag')

        # first move
        if self.sq[0][0] == 0:
            return 0, 0
        elif self.sq[0][0] != 0 and self.sq[1][1] == 0 and self.sq[2][2] != 1:
            return 1, 1
        elif self.sq[0][0] == 2:
            if self.sq[2][2] == 0:
                return 2, 2
            elif self.sq[1][1] == 1 and self.sq[2][2] == 0:
                return 2, 2
        elif self.sq[0][0] == 1 and self.sq[2][2] == 1 and self.sq[1][0] == 0:
            return 1, 0
        # print('logic error not in first move')

        for i in range(3):
            for k in range(3):
                if self.sq[i][k] == 0:
                    # print('logic error in random select')
                    return i, k

    def check_over(self):
        if self.gameover()[0] == 1:
            self.game_end = True
            if self.gameover()[1] == 1:
                return 1
            elif self.gameover()[1] == 2:
                self.win_count[1] += 1
                return 2
            elif self.gameover()[1] == 3:
                return 3

            print(f'Player 1 Wins: {self.win_count[0]}, Player 2: {self.win_count[1]}')

    def gameover(self):
        check = 0
        for row in self.sq:
            if 0 not in row:
                check += 1
        if check == 3:
            self.game_end = True
            return 1, 3
        else:
            winner_check = [self.checkwin(1), self.checkwin(2)]
            for i in range(2):
                if 1 in winner_check[i]:
                    self.game_end = True
                    return 1, winner_check[i][1]
            return 0, 0

    def checkwin(self, winner):
        # check columns separately
        cnt = 0
        for column in range(3):
            cnt = 0
            for row in range(3):
                mem = self.sq[row][column]
                if mem == winner:
                    cnt += 1
                if cnt == 3:
                    return 1, winner

        if [winner, winner, winner] in self.sq:
            return 1, winner
        elif winner == self.sq[0][0] == self.sq[1][1] == self.sq[2][2]:
            return 1, winner
        elif winner == self.sq[0][2] == self.sq[1][1] == self.sq[2][0]:
            return 1, winner
        elif cnt == 3:
            return 1, winner
        else:
            return 0, 3
