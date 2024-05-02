# tic-tac-toe GUI
from tkinter import *
import logic

class Gui:
    squares = [ [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    turn = 0
    gameover = False
    player = 0
    gamestart = False
    def __init__(self,window):
        self.window = window
        self.frame_shape = Frame(self.window)
        self.frame_shape.pack()

        #title page
        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, font=('Ariel', 11), text='Tic Tac Toe')
        self.label_title.pack(anchor='center', pady=100)
        self.button_title = Button(self.frame_title, text='Play!', command=self.load_game)
        self.button_title.pack(anchor='s')
        self.frame_title.pack()

        #playing page
        self.frame_game = Frame(self.window)

        self.game_boxes = []
        for i in range(3):
            for j in range(3):
                self.game_box = Text(self.frame_game, height=5, width=10, state='disabled')
                self.game_box.grid(row=i, column=j, padx=0, pady=0)
                self.game_box.bind("<Button-1>", self.square_clicked)
                self.game_boxes.append(self.game_box)

        self.frame_game.pack(anchor='n', pady=10)

        self.frame_buttons = Frame(self.window)
        self.label_game = Label(self.frame_buttons, font=('Ariel', 11), text = 'Would you like to go first?')
        self.button_yes = Button(self.frame_buttons, text='Yes', command=self.plr_start)
        self.button_no = Button(self.frame_buttons, text='No', command=self.cpu_start)

        self.label_game.pack(side = 'top', pady=10)
        self.button_yes.pack(side = 'left')
        self.button_no.pack(side = 'right')
        self.frame_buttons.pack(anchor='n')

        #self.frame_replay = Frame(self.window)
        #self.button_replay = Button(self.frame_replay, text='Again', command=self.load_game)
        #self.button_replay.pack(side='bottom')


        self.frame_game.pack_forget()
        self.frame_buttons.pack_forget()
        #self.frame_replay.pack_forget()

        #print(self.get_box_status(1,2))

        #end screen


    def load_game(self):
        self.gameover = False
        self.frame_title.pack_forget()
        self.frame_game.pack()
        self.frame_buttons.pack()
        for game_box in self.game_boxes:
            game_box.config(bg='white')


    def plr_start(self):
        self.button_yes.forget()
        self.button_no.forget()
        self.label_game.forget()

        self.gamestart = True
        self.player = 1

    def cpu_start(self):
        self.button_yes.forget()
        self.button_no.forget()
        self.label_game.forget()

        self.gamestart = True
        self.squares[0][0] = 2
        self.update_screen(0, 0)
        self.player = 1


    def select_square(self, row, col):
        self.squares = logic.playermove(self.squares, self.player, (row,col))
        print(self.squares)



    def square_clicked(self, event):
        if self.gamestart and not self.gameover:
            if self.player == 1:
                self.click_square = event.widget
                row, col = self.click_square.grid_info()["row"], self.click_square.grid_info()["column"]
                self.select_square(row,col)
                self.update_screen(row,col)

                row, col = logic.checkstrat(self.squares)[0], logic.checkstrat(self.squares)[1]
                self.squares[row][col] = 2
                self.update_screen(row, col)

    def update_screen(self, row, col):
        status = self.squares[row][col]
        if status == 1:
            bg_color = 'blue'
        elif status == 2:
            bg_color = 'red'
        else:
            bg_color = 'white'

        self.game_boxes[row * 3 + col].configure(bg=bg_color)


    def get_box_status(self, row, col):
        index = row * 3 + col
        box = self.game_boxes[index]
        status = box.cget()
        return status


