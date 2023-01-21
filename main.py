import threading
import socket
import sys
from time import sleep
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")
btn_text1 = tk.StringVar()
btn_text2 = tk.StringVar()
btn_text3 = tk.StringVar()
btn_text4 = tk.StringVar()
btn_text5 = tk.StringVar()
btn_text6 = tk.StringVar()
btn_text7 = tk.StringVar()
btn_text8 = tk.StringVar()
btn_text9 = tk.StringVar()
single_player_mode = False
no_winner = True
value = tk.IntVar()
counter = 0
moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# BUTTONS
def update_text(num):
    try:
        if counter % 2 == 0:
            char = 'X'
        else:
            char = 'O'

        if num == "1":
            btn_text1.set(char)
            b1['state'] = DISABLED
        elif num == "2":
            btn_text2.set(char)
            b2['state'] = DISABLED
        elif num == "3":
            btn_text3.set(char)
            b3['state'] = DISABLED
        elif num == "4":
            btn_text4.set(char)
            b4['state'] = DISABLED
        elif num == "5":
            btn_text5.set(char)
            b5['state'] = DISABLED
        elif num == "6":
            btn_text6.set(char)
            b6['state'] = DISABLED
        elif num == "7":
            btn_text7.set(char)
            b7['state'] = DISABLED
        elif num == "8":
            btn_text8.set(char)
            b8['state'] = DISABLED
        elif num == "9":
            btn_text9.set(char)
            b9['state'] = DISABLED
        checkIfWon()
    except Exception as e:
        print(f"Error '{e}' occurred. Arguments {e.args}.")


# def wasClicked(b):
#     b['state'] = DISABLED


def finished(b, bb, bbb, char):
    try:
        global no_winner
        no_winner = False
        b.config(bg="red")
        bb.config(bg="red")
        bbb.config(bg="red")
        messagebox.showinfo('Game Over', char + " Won!")
        sleep(0.5)
        messagebox.showinfo('New Game', "CLEARING FIELDS!")
        resetGame()
    except Exception as e:
        print(f"Error '{e}' occurred. Arguments {e.args}.")


def checkIfWon():
    # X WINS
    if btn_text1.get() == "X" and btn_text2.get() == "X" and btn_text3.get() == "X":
        finished(b1, b2, b3, 'X')

    elif btn_text4.get() == "X" and btn_text5.get() == "X" and btn_text6.get() == "X":
        finished(b4, b5, b6, 'X')

    elif btn_text7.get() == "X" and btn_text8.get() == "X" and btn_text9.get() == "X":
        finished(b7, b8, b9, 'X')

    elif btn_text1.get() == "X" and btn_text4.get() == "X" and btn_text7.get() == "X":
        finished(b1, b4, b7, 'X')

    elif btn_text2.get() == "X" and btn_text5.get() == "X" and btn_text8.get() == "X":
        finished(b2, b5, b8, 'X')

    elif btn_text3.get() == "X" and btn_text6.get() == "X" and btn_text9.get() == "X":
        finished(b3, b6, b9, 'X')

    elif btn_text1.get() == 'X' and btn_text5.get() == 'X' and btn_text9.get() == 'X':
        finished(b1, b5, b9, 'X')

    elif btn_text3.get() == 'X' and btn_text5.get() == 'X' and btn_text7.get() == 'X':
        finished(b3, b5, b7, 'X')

    # O WINS

    if btn_text1.get() == "O" and btn_text2.get() == "O" and btn_text3.get() == "O":
        finished(b1, b2, b3, 'O')

    elif btn_text4.get() == "O" and btn_text5.get() == "O" and btn_text6.get() == "O":
        finished(b4, b5, b6, 'O')

    elif btn_text7.get() == "O" and btn_text8.get() == "O" and btn_text9.get() == "O":
        finished(b7, b8, b9, 'O')

    elif btn_text1.get() == "O" and btn_text4.get() == "O" and btn_text7.get() == "O":
        finished(b1, b4, b7, 'O')

    elif btn_text2.get() == "O" and btn_text5.get() == "O" and btn_text8.get() == "O":
        finished(b2, b5, b8, 'O')

    elif btn_text3.get() == "O" and btn_text6.get() == "O" and btn_text9.get() == "O":
        finished(b3, b6, b9, 'O')

    elif btn_text1.get() == 'O' and btn_text5.get() == 'O' and btn_text9.get() == 'O':
        finished(b1, b5, b9, 'O')

    elif btn_text3.get() == 'O' and btn_text5.get() == 'O' and btn_text7.get() == 'O':
        finished(b3, b5, b7, 'O')

    elif (b1['state'] == DISABLED and b2['state'] == DISABLED and b3['state'] == DISABLED and b4[
        'state'] == DISABLED and
          b5[
              'state'] == DISABLED and b6['state'] == DISABLED and b7['state'] == DISABLED and b8[
              'state'] == DISABLED and b9[
              'state'] == DISABLED and no_winner):
        messagebox.showinfo('Game Over', "TIE!")


b1 = Button(root, textvariable=btn_text1, font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: [value.set(1)])
b2 = Button(root, textvariable=btn_text2, font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: [value.set(2)])
b3 = Button(root, textvariable=btn_text3, font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: [value.set(3)])
b4 = Button(root, textvariable=btn_text4, font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: [value.set(4)])
b5 = Button(root, textvariable=btn_text5, font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: [value.set(5)])
b6 = Button(root, textvariable=btn_text6, font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: [value.set(6)])
b7 = Button(root, textvariable=btn_text7, font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: [value.set(7)])
b8 = Button(root, textvariable=btn_text8, font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: [value.set(8)])
b9 = Button(root, textvariable=btn_text9, font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: [value.set(9)])

b10 = Button(root, text="RESET GAME", font=("Helvetica", 10), height=2, width=10, command=lambda: resetGame())
b11 = Button(root, text="QUIT", font=("Helvetica", 10), height=2, width=10, command=lambda: quitGame())
b12 = Button(root, text="PLAY PC", font=("Helvetica", 10), height=2, width=10, command=lambda: playComputer())
b13 = Button(root, text="2 PLAYERS", font=("Helvetica", 10), height=2, width=10, state=DISABLED,
             command=lambda: playMulti())


def playComputer():
    try:
        b13['state'] = NORMAL
        b12['state'] = DISABLED
        resetGame()
        messagebox.showinfo("You're playing a computer.", "You start!")
        global single_player_mode
        single_player_mode = True
    except Exception as e:
        print(f"Error '{e}' occurred. Arguments {e.args}.")


def playMulti():
    try:
        global single_player_mode
        single_player_mode = False
        b12['state'] = NORMAL
        b13['state'] = DISABLED
        resetGame()
        messagebox.showinfo("Multiplayer mode.", "2 player mode!")
    except Exception as e:
        print(f"Error '{e}' occurred. Arguments {e.args}.")


def quitGame():
    try:
        root.destroy()
        sys.exit()
    except Exception as e:
        print(f"Error '{e}' occurred. Arguments {e.args}.")


def resetGame():
    try:
        global moves
        moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        b1.config(bg="white")
        b2.config(bg="white")
        b3.config(bg="white")
        b4.config(bg="white")
        b5.config(bg="white")
        b6.config(bg="white")
        b7.config(bg="white")
        b8.config(bg="white")
        b9.config(bg="white")
        btn_text1.set('')
        btn_text2.set('')
        btn_text3.set('')
        btn_text4.set('')
        btn_text5.set('')
        btn_text6.set('')
        btn_text7.set('')
        btn_text8.set('')
        btn_text9.set('')
        b1['state'] = NORMAL
        b2['state'] = NORMAL
        b3['state'] = NORMAL
        b4['state'] = NORMAL
        b5['state'] = NORMAL
        b6['state'] = NORMAL
        b7['state'] = NORMAL
        b8['state'] = NORMAL
        b9['state'] = NORMAL
    except Exception as e:
        print(f"Error '{e}' occurred. Arguments {e.args}.")


# GRID
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

b12.grid(row=3, column=2)
b10.grid(row=3, column=1)
b11.grid(row=3, column=0)
b13.grid(row=4, column=1)


def server_func():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 3333))
        server_socket.listen(1)
        connection, addr = server_socket.accept()
        while True:
            global moves
            data = connection.recv(1024).decode()
            if not data:
                break
            if not single_player_mode:
                update_text(data)
            elif single_player_mode:
                if int(data) in moves:
                    update_text(data)
                    moves.remove(int(data))
                    random_val = random.choice(moves)
                    moves.remove(random_val)
                    update_text(str(random_val))
                    checkIfWon()

    except Exception as e:
        print(f"Error '{e}' occurred. Arguments {e.args}.")


def client_func():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 3333))
        while True:
            root.wait_variable(value)
            client_socket.send(str(value.get()).encode())
    except Exception as e:
        print(f"Error '{e}' occurred. Arguments {e.args}.")


t1 = threading.Thread(target=server_func)
t2 = threading.Thread(target=client_func)
t1.start()
t2.start()

root.mainloop()
