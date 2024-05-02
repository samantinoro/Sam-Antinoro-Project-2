# projet 2 main file.

from gui import *
def main():
    window = Tk()
    window.title('Tic Tac Toe')
    window.geometry('325x400')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
