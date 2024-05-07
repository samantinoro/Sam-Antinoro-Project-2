# logic for tic-tac-toe game. Modified from code I finished on February-20-2024
# handles all logic relating to input in the game.
# game start handled by gui.py to avoid assigning variables in logic.py in gui.py

class TTTLogic:
    # Set up initial variable states upon game startup, returns nothing
    def __init__(self) -> None:
        self.sq: list = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]
        self.win_count: list = [0, 0]
        self.turn: int = 0
        self.player: int = 0
        self.game_end: bool = False
        self.temp_win: list = [0, 0]
        self.final_winner: str = ''

    # Resets all single-game related variables, returns nothing
    def set_vars(self) -> None:
        self.sq = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
        self.turn: int = 0
        self.player: int = 0
        self.game_end: bool = False
        self.temp_win: list = [0, 0]

    # Resets cross-game turn count variable, returns nothing
    def reset_score(self) -> None:
        self.win_count = [0, 0]

    '''
    Sets player move to square from GUI input, increases turn count, switches player status to allow next move
    :row: Part of the 2D list of available / taken squares, taken from user selection on grid
    :col: Second part of 2D list of available / taken squares, taken, from user selection on grid
    :return: Returns nothing
    '''
    def playermove(self, row, col) -> None:
        self.turn += 1
        self.sq[row][col]: int = self.player
        self.player: int = 3 - self.player

    '''
    Decides which move the computer picks based on current game values / square statuses
    :return: Returns row and column for grid square selection in GUI
    '''
    def checkstrat(self) -> tuple:
        # instant win / lose conditions
        klist: list = [2, 1]
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

    '''
    Checks whether the game is over via returns from self.gameover
    :return: Returns numeric winner value (p1=1, p2=2, draw=3)
    '''
    def check_over(self) -> int:
        if self.gameover()[0] == 1:
            self.game_end: bool = True
            if self.gameover()[1] == 1:
                return 1
            elif self.gameover()[1] == 2:
                return 2
            elif self.gameover()[1] == 3:
                return 3

    '''
    Checks whether the game is ended based on square statuses and checkwin method
    :return: Tuple containing integer for ongoing / ended status (No=0,Yes=1) and winning player int (p1=1, p2=2, tie=3)
    '''
    def gameover(self) -> tuple:
        check: int = 0
        winners: list = ['PLAYER 1', 'PLAYER 2', 'NOBODY']

        for row in self.sq:
            if 0 not in row:
                check += 1
        if check == 3:
            self.game_end: bool = True
            self.final_winner: str = winners[2]
            return 1, 3
        else:
            winner_check: list = [self.checkwin(1), self.checkwin(2)]
            for i in range(2):
                if 1 in winner_check[i]:
                    self.game_end: bool = True
                    self.win_count[i] += 1
                    self.final_winner: str = winners[i]
                    return 1, winner_check[i][1]
            return 0, 0

    '''
    Method to check whether either player has met a winning condition (3 in a row) or if all squares are filled (draw)
    :return: Return tuple containing if win condition met (No=0, Yes=1) and winner value (1=p1, 2=p2, 3=None)
    '''
    def checkwin(self, winner: int) -> tuple:
        # check columns separately
        for column in range(3):
            cnt: int = 0
            for row in range(3):
                mem: int = self.sq[row][column]
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
        else:
            return 0, 3
