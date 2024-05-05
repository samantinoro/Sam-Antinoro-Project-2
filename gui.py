# tic-tac-toe GUI
from tkinter import *
from logic import TTTLogic


class Gui:
    gamestart = False
    pvp = False

    def __init__(self, window):
        self.Logic = TTTLogic()
        self.click_square = None

        self.window = window
        self.frame_shape = Frame(self.window)
        self.frame_shape.pack()

        # title page
        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, font=('Ariel', 11), text='Tic Tac Toe')
        self.label_title.pack(anchor='center', pady=100)
        self.button_start = Button(self.frame_title, text='Play!', command=self.load_game)
        self.button_sett = Button(self.frame_title, text='Settings', command=self.load_sett)
        self.button_start.pack(side='left')
        self.button_sett.pack(side='right')
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

        # Setup label and buttons for game options (multi purpose)
        self.frame_options = Frame(self.window)
        self.label_options = Label(self.frame_options, font=('Ariel', 11))
        self.button_left = Button(self.frame_options)
        self.button_right = Button(self.frame_options)

        self.label_options.pack(side='top')
        self.button_left.pack(side='left')
        self.button_right.pack(side='right')
        self.frame_options.pack(side='top', pady=10)

        self.frame_game.pack_forget()
        self.frame_options.pack_forget()

        # Set up End + Stats Screen
        self.frame_end = Frame(self.window)
        self.label_end = Label(self.frame_end, font=('Ariel', 12), text='GAME OVER')
        self.label_result = Label(self.frame_end, font=('Ariel', 12), text='The winner is...')
        self.label_replay = Label(self.frame_end, font=('Ariel', 12), text='Would you like to play again?')
        self.button_replay = Button(self.frame_end, text='YES!', command=self.load_game)
        self.frame_end.pack(anchor='n')
        self.frame_end.pack_forget()

    def load_sett(self):
        print('test')

    def load_game(self):
        self.Logic.set_vars()

        self.frame_title.pack_forget()
        self.frame_end.pack_forget()
        self.frame_game.pack_forget()

        self.frame_game.pack()
        for game_box in self.game_boxes:
            game_box.config(bg='white')

        self.label_options.config(text='Which game mode would you like to play?')
        self.button_left.config(text='Player vs Player', command=self.pvp_mode)
        self.button_right.config(text='Player vs Computer', command=self.cpu_mode)
        self.frame_options.pack()

    def pvp_mode(self):
        self.pvp = True
        self.frame_options.pack_forget()
        self.plr_start()

    def cpu_mode(self):
        self.pvp = False

        self.label_options.config(text='Would you like to go first?')
        self.button_left.config(text='Yes', command=self.plr_start)
        self.button_right.config(text='No', command=self.cpu_start)
        self.frame_options.pack()

    def plr_start(self):
        self.frame_options.pack_forget()

        self.Logic.player = 1
        self.gamestart = True

    def cpu_start(self):
        self.frame_options.pack_forget()

        self.Logic.player = 2
        self.gamestart = True
        self.Logic.playermove(0, 0)
        self.update_screen(0, 0)

    def square_clicked(self, event):
        try:
            if self.gamestart and not self.Logic.game_end:
                self.change_square(event)

                if not self.pvp:
                    row, col = self.Logic.checkstrat()
                    self.Logic.playermove(row, col)
                    self.update_screen(row, col)

                self.Logic.tempwin = self.Logic.gameover()
                if self.Logic.tempwin[0] == 1:
                    raise TypeError

        except TypeError:
            self.end_game()

    def change_square(self, event):
        self.click_square = event.widget
        row, col = self.click_square.grid_info()["row"], self.click_square.grid_info()["column"]
        self.Logic.playermove(row, col)
        self.update_screen(row, col)

    def update_screen(self, row, col):
        status = self.Logic.sq[row][col]
        if status == 1:
            bg_color = 'blue'
        elif status == 2:
            bg_color = 'red'
        else:
            bg_color = 'white'
        self.game_boxes[row * 3 + col].configure(bg=bg_color)

    def end_game(self):
        if self.Logic.tempwin[1] == 1:
            winner = 'Player 1'
        elif self.Logic.tempwin[1] == 2:
            winner = 'Player 2'
        else:
            winner = 'NOBODY'

        self.label_options.config(text=f'{winner} WINS')
        self.button_left.config(text='See Stats', command=self.end_screen)
        self.label_options.pack()
        self.button_right.forget()
        self.button_left.pack(side='top',anchor='n')
        self.frame_options.pack()


    def end_screen(self):
        self.label_options.config(text=f'Game Stats:\nWinner: {self.Logic.tempwin}\nTurn Count = {self.Logic.turn}')
        self.button_left.config(text='Yes', command=self.plr_start)
        self.button_right.config(text='No', command=self.cpu_start)
        self.frame_options.pack()



