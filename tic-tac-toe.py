from pynput import keyboard
from sys import exit
import time


# lists
board = [" " , " " , " " ,
         " " , " " , " " ,
         " " , " " , " " ]

# variables
ex = 'X'
Oo = "O"
player = 'X'
level = "*"
kursor = '#'
has = 4
board[has] = kursor
close = ''
exOo =''
noenter = ""
win = '$'


def interface():                                       #Interface Board

    global board
    global level
    global player
    global kursor
    global noenter


    # console and instructions
    print()
    print(level*100)
    print()
    print('{}{}'.format(('Player ' + player + ' on Game').center(16), "Control".rjust(64)))
    print()
    print(" {} | {} | {} {}".format(board[0].center(3), board[1].center(3), board[2].center(3),'Move      ↑'.rjust(65)))
    print("{}{}".format(level * 17,'Keyboard  ← ↓ →'.rjust(67)))
    print(" {} | {} | {} {}".format(board[3].center(3), board[4].center(3), board[5].center(3),noenter.rjust(35)))
    print("{}{}".format(level * 17,'ENTER to Confirm'.rjust(68)))
    print(" {} | {} | {} ".format(board[6].center(3), board[7].center(3), board[8].center(3)))
    print()
    print(level * 100)


def on_release(key):                         # definition of istructions and reaction for Keyboard
    global board
    global kursor
    global has
    global close
    global ex
    global Oo
    global player
    global exOo
    global noenter

    if key == keyboard.Key.up:  #reaction for Key.up Press
        noenter = ''
        if has == 0:
            has = 6
        elif has == 1:
            has = 7
        elif has == 2:
            has = 8
        else:
            has = has - 3
        exOo = board[has]
        board[has] = kursor
        interface()
        board[has] = exOo


    elif key == keyboard.Key.down:              #reaction for Key.down Press
        noenter = ''
        if has == 8:
            has = 2
        elif has == 7:
            has = 1
        elif has == 6:
            has = 0
        else:
            has = has +3
        exOo = board[has]
        board[has] = kursor
        interface()
        board[has] = exOo

    elif key == keyboard.Key.left:      #reaction for Key.left Press
        noenter = ''
        if has == 0:
            has = 2
        elif has == 3:
            has = 5
        elif has == 6:
            has = 8
        else:
            has = has - 1
        exOo = board[has]
        board[has] = kursor
        interface()
        board[has] = exOo


    elif key == keyboard.Key.right:      #reaction for Key.right Press
        noenter = ''
        if has == 8:
            has = 6
        elif has == 5:
            has = 3
        elif has == 2:
            has = 0
        else:
            has = has + 1
        exOo = board[has]

        board[has] = kursor
        interface()
        board[has] = exOo


    elif key == keyboard.Key.esc:            # esc - exit program
        close = 1


    elif key == keyboard.Key.enter:         # enter to confirm move
        if board[has] == ex or board[has] == Oo:
            player2 = board[has]
            board[has] = kursor
            noenter = 'Find Empty Items!'
            interface()
            board[has] = player2

        else:
            board[has] = player
            check_winerX()
            check_winerO()
            check_draw()
            has = board.index(" ")
            board[has] = kursor
            swith_player()
            interface()
            board[has] = " "
    return False



def swith_player():
    global ex
    global Oo
    global player

    if player == ex:                     # change Player
        player = Oo
    elif player == Oo:
        player = ex


def check_winerX():                      # check Winner X player
    global ex
    global noenter
    global player
    global board
    global win
    global close

    if (board[0] == ex  and board[1] == ex and board[2] == ex) or (board[3] == ex  and board[4] == ex and board[5] == ex) or (board[6] == ex  and board[7] == ex and board[8] == ex):
        noenter = ('GRATULATIONS ! Player ' + ex + ' Wins !')
        interface()
        close = 1
        time.sleep(7)
    elif (board[0] == ex  and board[3] == ex and board[6] == ex) or (board[1] == ex  and board[4] == ex and board[7] == ex) or (board[2] == ex  and board[5] == ex and board[8] == ex):
        noenter = ('GRATULATIONS ! Player ' + ex + ' Wins !')
        interface()
        close = 1
        time.sleep(7)
    elif (board[0] == ex  and board[4] == ex and board[8] == ex) or (board[2] == ex  and board[4] == ex and board[6] == ex):
        noenter = ('GRATULATIONS ! Player ' + ex + ' Wins !')
        interface()
        close = 1
        time.sleep(7)


def check_winerO():                             # check Winner O player
    global Oo
    global noenter
    global player
    global board
    global win
    global close

    if (board[0] == Oo  and board[1] == Oo and board[2] == Oo) or (board[3] == Oo  and board[4] == Oo and board[5] == Oo) or (board[6] == Oo  and board[7] == Oo and board[8] == Oo):
        noenter = ('GRATULATIONS ! Player ' + Oo + ' Wins !')
        interface()
        close = 1
        time.sleep(5)
    elif (board[0] == Oo  and board[3] == Oo and board[6] == Oo) or (board[1] == Oo  and board[4] == Oo and board[7] == Oo) or (board[2] == Oo  and board[5] == Oo and board[8] == Oo):
        noenter = ('GRATULATIONS ! Player ' + Oo + ' Wins !')
        interface()
        close = 1
        time.sleep(7)
    elif (board[0] == Oo  and board[4] == Oo and board[8] == Oo) or (board[2] == Oo  and board[4] == Oo and board[6] == Oo):
        noenter = ('GRATULATIONS ! Player ' + Oo + ' Wins !')
        interface()
        close = 1
        time.sleep(5)

def check_draw():                                      # check Draw
    global noenter
    global close

    if " " not in board:
        noenter = ("It's Draw")
        interface()
        close = 1
        time.sleep(5)


interface()
board[has] = " "
while True:                                                             #loop until full
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()
    if close == 1:                                                      #close program
        exit()







