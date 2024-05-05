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

        self.frame_pvpbutt = Frame(self.window)
        self.label_pvp = Label(self.frame_pvpbutt, font=('Ariel', 11), text='Which gamemode would you like to play?')
        self.button_pvpyes = Button(self.frame_pvpbutt, text='Player vs Player', command=self.pvp_mode)
        self.button_cpuyes = Button(self.frame_pvpbutt, text='Player vs Computer', command=self.cpu_mode)

        self.label_pvp.pack(side='top')
        self.button_pvpyes.pack(side='left')
        self.button_cpuyes.pack(side='right')
        self.frame_pvpbutt.pack(side='top', pady=10)

        self.frame_cpubutt = Frame(self.window)
        self.label_game = Label(self.frame_cpubutt, font=('Ariel', 11), text='Would you like to go first?')
        self.button_yes = Button(self.frame_cpubutt, text='Yes', command=self.plr_start)
        self.button_no = Button(self.frame_cpubutt, text='No', command=self.cpu_start)

        self.label_game.pack(side='top', pady=10)
        self.button_yes.pack(side='left')
        self.button_no.pack(side='right')
        self.frame_pvpbutt.pack(anchor='n')
        self.frame_cpubutt.pack(anchor='n')

        self.frame_game.pack_forget()
        self.frame_pvpbutt.pack_forget()
        self.frame_cpubutt.pack_forget()

        # end screen
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
        self.frame_title.pack_forget()
        self.frame_end.pack_forget()
        self.frame_game.pack_forget()
        self.frame_cpubutt.forget()

        self.frame_game.pack()
        for game_box in self.game_boxes:
            game_box.config(bg='white')

        self.Logic.set_vars()
        self.frame_pvpbutt.pack()

    def pvp_mode(self):
        self.pvp = True
        self.frame_pvpbutt.pack_forget()
        self.plr_start()

    def cpu_mode(self):
        self.pvp = False
        self.frame_pvpbutt.pack_forget()
        self.frame_cpubutt.pack()

    def plr_start(self):
        self.button_yes.pack_forget()
        self.button_no.pack_forget()
        self.label_game.pack_forget()

        self.Logic.player = 1
        self.gamestart = True

    def cpu_start(self):
        self.button_yes.pack_forget()
        self.button_no.pack_forget()
        self.label_game.pack_forget()

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
                self.Logic.check_over()

        except TypeError:
            self.Logic.check_over()

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
