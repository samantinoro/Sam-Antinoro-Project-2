# tic-tac-toe GUI
from tkinter import *
from logic import TTTLogic


class Gui:
    gamestart = False
    pvp = False
    colors = ['#FF0000', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF', '#FF00FF']
    col_name = ['Red', 'Yellow', 'Green', 'Cyan', 'Blue', 'Pink']

    def __init__(self, window):
        self.color_p1 = self.colors[4]
        self.color_p2 = self.colors[0]

        self.Logic = TTTLogic()
        self.click_square = None

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

        self.label_options.pack(side='top',pady=10)
        self.button_left.pack(side='left')
        self.button_right.pack(side='right')
        self.frame_options.pack(side='top', pady=10)

        self.frame_game.pack_forget()
        self.frame_options.pack_forget()

        # settings screen options
        self.frame_sett = Frame(self.window)
        self.label_sett = Label(self.frame_sett, font=('Ariel', 12), text='Select your colors')
        self.slider_p1 = Scale(self.frame_sett, label='Player 1 Color', from_=0, to=5)
        self.slider_p1.config(orient=HORIZONTAL, showvalue=False, command=self.choose_p1)
        self.label_col1 = Label(self.frame_sett, font=('Ariel', 11), text='')
        self.slider_p2 = Scale(self.frame_sett, label='Player 2 Color', from_=0, to=5)
        self.slider_p2.config(orient=HORIZONTAL, showvalue=False, command=self.choose_p2)
        self.label_col2 = Label(self.frame_sett, font=('Ariel', 11), text='')
        self.label_sett_err = Label(self.frame_sett, font=('Ariel', 11))
        self.butt_exit = Button(self.frame_sett, text='Exit', command=self.start_screen)

        self.label_sett.pack(side='top', pady=20)
        self.slider_p1.pack(side='top')
        self.label_col1.pack(side='top')
        self.slider_p2.pack(side='top')
        self.label_col2.pack(side='top')
        self.label_sett_err.pack(side='top')
        self.label_sett_err.forget()
        self.butt_exit.pack(side='top', pady=20)
        self.frame_sett.pack_forget()

    def start_screen(self):
        self.frame_options.forget()
        self.frame_sett.forget()
        self.frame_title.pack()

    def load_sett(self):
        p1 = self.colors.index(self.color_p1)
        p2 = self.colors.index(self.color_p2)

        self.slider_p1.set(p1)
        self.slider_p2.set(p2)
        self.label_col1.config(text=f'{self.col_name[p1]}')
        self.label_col2.config(text=f'{self.col_name[p2]}')

        self.frame_options.forget()
        self.frame_title.forget()
        self.frame_sett.pack()

        self.button_left.forget()
        self.button_right.forget()

        temp_text1 = f'Current score:\nPlayer 1: {self.Logic.win_count[0]} points\n'
        temp_text2 = f'Player 2: {self.Logic.win_count[1]} points'
        self.label_options.config(text=temp_text1 + temp_text2)
        self.frame_options.pack()

    def choose_p1(self, cval):
        cval = int(cval)
        self.label_col1.config(text=self.col_name[cval])
        if self.colors[cval] != self.color_p2:
            self.color_p1 = self.colors[cval]
            self.label_sett_err.forget()
            self.butt_exit.pack(pady=20)
        else:
            self.label_sett_err.config(text='Colors must be different')
            self.label_sett_err.pack(pady=20)
            self.butt_exit.forget()

    def choose_p2(self, cval):
        cval = int(cval)
        self.label_col2.config(text=self.col_name[cval])
        if self.colors[cval] != self.color_p1:
            self.color_p2 = self.colors[cval]
            self.label_sett_err.forget()
            self.butt_exit.pack(pady=20)
        else:
            self.label_sett_err.config(text='Colors must be different')
            self.label_sett_err.pack(pady=20)
            self.butt_exit.forget()

    def load_game(self):
        self.Logic.set_vars()
        self.frame_title.forget()
        self.frame_sett.forget()
        self.frame_game.forget()
        self.frame_options.forget()

        self.frame_game.pack()
        for game_box in self.game_boxes:
            game_box.config(bg='white')

        self.label_options.config(text='Which game mode would you like to play?')
        self.button_left.config(text='Player vs Player', command=self.pvp_mode)
        self.button_right.config(text='Player vs Computer', command=self.cpu_mode)
        self.button_left.pack(side='left')
        self.button_right.pack(side='right')
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

                self.Logic.temp_win = self.Logic.gameover()
                if self.Logic.temp_win[0] == 1:
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
            bg_color = self.color_p1
        elif status == 2:
            bg_color = self.color_p2
        else:
            bg_color = '#FFFFFF'
        self.game_boxes[row * 3 + col].configure(bg=bg_color)

    def end_game(self):
        if self.Logic.temp_win[1] == 1:
            self.Logic.win_count[0] += 1
            self.Logic.final_winner = 'Player 1'
        elif self.Logic.temp_win[1] == 2:
            self.Logic.win_count[1] += 1
            self.Logic.final_winner = 'Player 2'
        else:
            self.Logic.final_winner = 'NOBODY'

        self.gamestart = False
        self.label_options.config(text=f'{self.Logic.final_winner} WINS')
        self.button_left.config(text='See Stats', command=self.end_screen)
        self.label_options.pack()
        self.button_right.forget()
        self.button_left.pack(side='top', anchor='n')
        self.frame_options.pack()

    def end_screen(self):
        self.frame_game.forget()
        temp_text1 = f'Turns = {self.Logic.turn}\n\n'
        temp_text2 = f'Score:\nPlayer 1: {self.Logic.win_count[0]} points\n'
        temp_text3 = f'Player 2: {self.Logic.win_count[1]} points'
        self.label_options.config(text=temp_text1 + temp_text2 + temp_text3 + '\nRestart?\n')
        self.button_left.config(text='Yes', command=self.start_screen)
        self.frame_options.pack(anchor='center', pady=100)
