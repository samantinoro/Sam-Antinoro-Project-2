# tic-tac-toe GUI
from tkinter import *
import logic

class Gui:
    squares = [ [0,0,0],
                [0,0,0],
                [0,0,0]]
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
            game_box.delete("1.0",)


    def plr_start(self):
        self.gamestart = True
        self.player = 1

        self.button_yes.forget()
        self.button_no.forget()
        self.label_game.forget()
        #logic.boarding(1, self.squares, self.turn)



    def cpu_start(self):
        self.gamestart = True
        self.player = 2

        self.button_yes.forget()
        self.button_no.forget()
        self.label_game.forget()
        #logic.boarding(2, self.squares, self.turn)



    def square_clicked(self, event):
        if self.gamestart and not self.gameover:
            self.click_square = event.widget
            row, col = self.click_square.grid_info()["row"], self.click_square.grid_info()["column"]
            self.squares[row][col] = self.player
            self.click_square = event.widget.config(bg='blue')


    def get_box_status(self, row, column):
        index = row * 3 + column
        box = self.game_boxes[index]

        status = box.get('1.0', 'end')
        return status


