# tic-tac-toe GUI
from tkinter import *
from logic import TTTLogic


class Gui:
    # Variables related to running GUI checks
    gamestart: bool = False
    pvp: bool = False
    valid_move: bool = False
    colors: list = ['#FF0000', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF', '#FF00FF', '#FFFFFF']
    col_name: list = ['Red', 'Yellow', 'Green', 'Cyan', 'Blue', 'Pink', 'White']

    # define instance variables, GUI elements, and GUI Methods
    def __init__(self, window) -> None:
        self.color_p1: str = self.colors[4]
        self.color_p2: str = self.colors[0]

        self.Logic = TTTLogic()
        self.click_square = Widget

        self.window = window
        self.frame_shape = Frame(self.window)
        self.frame_shape.pack()

        # title page
        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, font=('Ariel', 15), text='Tic Tac Toe')
        self.label_title.pack(anchor='center', pady=100)
        self.button_start = Button(self.frame_title, text='Play!', command=self.load_game)
        self.button_sett = Button(self.frame_title, text='Settings', command=self.load_sett)
        self.button_start.pack(side='left', anchor='w')
        self.button_sett.pack(side='right', anchor='e')
        self.frame_title.pack()

        # playing page
        self.frame_game = Frame(self.window)
        self.game_boxes = []
        for i in range(3):
            for j in range(3):
                self.game_box = Text(self.frame_game, height=5, width=10, state='disabled')
                self.game_box.grid(row=i, column=j, padx=0, pady=0)
                self.game_box.bind("<Button-1>", self.square_clicked)
                self.game_boxes.append(self.game_box)
        self.frame_game.pack(anchor='n', pady=10)

        # Setup label and buttons for game options (multipurpose)
        self.frame_options = Frame(self.window)
        self.label_options = Label(self.frame_options, font=('Ariel', 12))
        self.button_left = Button(self.frame_options)
        self.button_right = Button(self.frame_options)

        self.label_options.pack(side='top', pady=10)
        self.button_left.pack(side='left')
        self.button_right.pack(side='right')
        self.frame_options.pack(side='top', pady=10)

        self.frame_game.pack_forget()
        self.frame_options.pack_forget()

        # settings screen options
        self.frame_sett = Frame(self.window)
        self.label_sett = Label(self.frame_sett, font=('Ariel', 12), text='Select your colors')
        self.slider_p1 = Scale(self.frame_sett, label='Player 1 Color', from_=0, to=len(self.colors)-2)
        self.slider_p1.config(orient=HORIZONTAL, showvalue=False, command=self.choose_p1)
        self.label_col1 = Label(self.frame_sett, font=('Ariel', 11), text='')
        self.slider_p2 = Scale(self.frame_sett, label='Player 2 Color', from_=0, to=len(self.colors)-2)
        self.slider_p2.config(orient=HORIZONTAL, showvalue=False, command=self.choose_p2)
        self.label_col2 = Label(self.frame_sett, font=('Ariel', 11), text='')
        self.label_sett_err = Label(self.frame_sett, font=('Ariel', 11))
        self.butt_exit = Button(self.frame_sett, text='Exit', command=self.start_screen)

        self.label_sett.pack(side='top', pady=20)
        self.slider_p1.pack()
        self.label_col1.pack()
        self.slider_p2.pack()
        self.label_col2.pack()
        self.label_sett_err.pack()
        self.label_sett_err.forget()
        self.butt_exit.pack()
        self.frame_sett.pack_forget()

    '''
    Packs title Screen Elements and makes other frames invisible
    :return: Returns nothing
    '''
    def start_screen(self) -> None:
        self.frame_options.forget()
        self.frame_sett.forget()
        self.frame_title.pack()

    '''
    Loads settings frame / menu elements, packs options label for more information
    :return: Returns nothing
    '''
    def load_sett(self) -> None:
        p1: int = self.colors.index(self.color_p1)
        p2: int = self.colors.index(self.color_p2)

        self.slider_p1.set(p1)
        self.slider_p2.set(p2)
        self.label_col1.config(text=f'{self.col_name[p1]}')
        self.label_col2.config(text=f'{self.col_name[p2]}')

        self.frame_options.forget()
        self.frame_title.forget()
        self.frame_sett.pack()
        self.button_right.forget()

        temp_text1: str = f'Current score:\nPlayer 1: {self.Logic.win_count[0]} points\n'
        temp_text2: str = f'Player 2: {self.Logic.win_count[1]} points'
        self.label_options.config(text=temp_text1 + temp_text2)
        self.button_left.config(text='Reset Score?', command=self.set_score)
        self.button_left.pack(anchor='center', side='top')
        self.frame_options.pack()

    '''
    Resets cross-game score variable value via settings menu
    :return: Returns nothing
    '''
    def set_score(self) -> None:
        self.Logic.reset_score()
        temp_text1: str = f'Current score:\nPlayer 1: {self.Logic.win_count[0]} points\n'
        temp_text2: str = f'Player 2: {self.Logic.win_count[1]} points'
        self.label_options.config(text=temp_text1 + temp_text2)

    '''
    Changes Player 1 color value to user selection from scale
    :return: Returns nothing
    '''
    def choose_p1(self, cval) -> None:
        cval: int = int(cval)
        self.label_col1.config(text=self.col_name[cval])
        if self.colors[cval] != self.color_p2:
            self.color_p1: str = self.colors[cval]
            self.label_sett_err.forget()
            self.butt_exit.pack(pady=20)
        else:
            self.label_sett_err.config(text='Colors must be different')
            self.label_sett_err.pack(pady=20)
            self.butt_exit.forget()

    '''
    Changes Player 2 color value to user selection from scale
    :return: Returns nothing
    '''
    def choose_p2(self, cval) -> None:
        cval: int = int(cval)
        self.label_col2.config(text=self.col_name[cval])
        if self.colors[cval] != self.color_p1:
            self.color_p2: str = self.colors[cval]
            self.label_sett_err.forget()
            self.butt_exit.pack(pady=20)
        else:
            self.label_sett_err.config(text='Colors must be different')
            self.label_sett_err.pack(pady=20)
            self.butt_exit.forget()

    '''
    Loads game GUI frame and elements - game mode buttons, game grid
    :return: Returns nothing
    '''
    def load_game(self) -> None:
        self.Logic.set_vars()
        self.frame_title.forget()
        self.frame_sett.forget()
        self.frame_game.forget()
        self.frame_options.forget()

        self.frame_game.pack()
        for game_box in self.game_boxes:
            game_box.config(bg='#FFFFFF')

        self.label_options.config(text='Which game mode would you like to play?')
        self.button_left.config(text='Player vs Player', command=self.pvp_mode)
        self.button_right.config(text='Player vs Computer', command=self.cpu_mode)
        self.button_left.pack(side='left')
        self.button_right.pack(side='right')
        self.frame_options.pack()

    '''
    Sets game mode to Player vs Player, starts game with player 1, disappears frame
    :return: Returns nothing
    '''
    def pvp_mode(self) -> None:
        self.pvp: bool = True
        self.frame_options.pack_forget()
        self.plr_start()

    '''
    Sets game to Player vs CPU, sets buttons to ask who's going first
    :return: Returns nothing
    '''
    def cpu_mode(self) -> None:
        self.pvp: bool = False

        self.label_options.config(text='Would you like to go first?')
        self.button_left.config(text='Yes', command=self.plr_start)
        self.button_right.config(text='No', command=self.cpu_start)
        self.frame_options.pack()

    '''
    Method for when Player 1 starts, sets game to start
    :return: Returns nothing
    '''
    def plr_start(self) -> None:
        self.frame_options.pack_forget()
        self.Logic.player = 1
        self.gamestart: bool = True

    '''
    Method for when the Computer starts, sets game to start, selects cpu's first move
    :return: Returns nothing
    '''
    def cpu_start(self) -> None:
        self.frame_options.pack_forget()
        self.Logic.player = 2
        self.gamestart: bool = True
        self.Logic.playermove(0, 0)
        self.update_screen(0, 0)

    '''
    Method for when a grid square is clicked, logic methods change square values
    :event: Tkinter event handling. This method goes when event -- grid square is clicked
    :return: Returns nothing
    '''
    def square_clicked(self, event: Event) -> None:
        try:
            # Makes sure the game is still going
            if self.gamestart and not self.Logic.game_end:
                self.change_square(event)

                # Ensures player 2 can only move if the player made a valid move
                while self.valid_move:
                    # If the game isn't in PVP, selects computer's move
                    if not self.pvp:
                        row, col = self.Logic.checkstrat()
                        self.Logic.playermove(row, col)
                        self.update_screen(row, col)
                    self.valid_move: bool = False

                # Check for a winner, defer to check end method
                if self.Logic.gameover()[0] == 1:
                    raise TypeError
        # Also catches if all the squares are filled up
        except TypeError:
            self.end_game()

    '''
    Method for selecting / changing square on a player's move, ensures valid move
    :return: Returns nothing
    '''
    def change_square(self, event: Event) -> None:
        self.click_square: Widget = event.widget
        row, col = self.click_square.grid_info()["row"], self.click_square.grid_info()["column"]
        # if statement makes sure the square hasn't already been selected, then player can move
        if self.Logic.sq[row][col] == 0:
            self.Logic.playermove(row, col)
            self.update_screen(row, col)
            self.valid_move: bool = True
            if self.Logic.gameover()[0] == 1:
                raise TypeError

    '''
    Function to update the visuals of the grid once a move has been made.
    :return: Returns nothing 
    '''
    def update_screen(self, row: int, col: int) -> None:
        status: int = self.Logic.sq[row][col]
        if status == 1:
            bg_color = self.color_p1
        elif status == 2:
            bg_color = self.color_p2
        else:
            bg_color = self.colors[-1]
        self.game_boxes[row * 3 + col].configure(bg=bg_color)

    '''
    Method to halt GUI upon end of the game and allow option to see end screen
    :return: Returns nothing
    '''
    def end_game(self) -> None:
        self.gamestart: bool = False
        self.label_options.config(text=f'{self.Logic.final_winner} WINS')
        self.button_left.config(text='See Stats', command=self.end_screen)
        self.label_options.pack()
        self.button_right.forget()
        self.button_left.pack(side='top', anchor='n')
        self.frame_options.pack()

    '''
    Makes Game frame invisible and packs End Screen and related Option frame element
    :return: Returns nothing
    '''
    def end_screen(self) -> None:
        self.frame_game.forget()
        temp_text1: str = f'Turns = {self.Logic.turn}\n\n'
        temp_text2: str = f'Score:\nPlayer 1: {self.Logic.win_count[0]} points\n'
        temp_text3: str = f'Player 2: {self.Logic.win_count[1]} points'
        self.label_options.config(text=temp_text1 + temp_text2 + temp_text3 + '\n\nRestart?')
        self.button_left.config(text='Yes', command=self.start_screen)
        self.frame_options.pack(anchor='center', pady=100)
