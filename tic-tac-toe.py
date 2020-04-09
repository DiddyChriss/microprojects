from pynput import keyboard


fullX = ['X','X','X','X','X','X','X','X','X']
fullO = ['O','O',' bvhgcfchgvhgvghvO','O','O','O','O','O','O']
board = [" " , " " , " " ,

         " " , " " , " " ,
         " " , " " , " " ]

turple = (-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8)


player = ''
level = "*"
kursor = '#'
has = 4
board[has] = kursor


def interface():           #Interface Board

    global board
    global level
    global player
    global kursor

    # console and instructions
    print()
    print(level*100)
    print()
    print('{}{}'.format((player+' on Game').center(16), "Control".rjust(44)))
    print()
    print(" {} | {} | {} {}".format(board[0].center(3), board[1].center(3), board[2].center(3),'Move      ↑'.rjust(45)))
    print("{}{}".format(level * 17,'Keyboard  ← ↓ →'.rjust(47)))
    print(" {} | {} | {} ".format(board[3].center(3), board[4].center(3), board[5].center(3)))
    print("{}{}".format(level * 17,'ENTER to Confirm'.rjust(48)))
    print(" {} | {} | {} ".format(board[6].center(3), board[7].center(3), board[8].center(3)))
    print()
    print(level * 100)

# definition of istructions and reaction for Keyboard
def on_release(key):
    global board
    global kursor
    global has
    global turple
    if key == keyboard.Key.up:          #reaction for Key.up Press
        has = has - 3
        if has not in turple:
            has = 4
        else:
            board[has] = kursor
            interface()
            board[has] = " "
        return False
    elif key == keyboard.Key.down:      #reaction for Key.down Press
        has = has + 3
        if has not in turple:
            has = 4
        else:
            board[has] = kursor
            interface()
            board[has] = " "
        return False
    elif key == keyboard.Key.left:      #reaction for Key.left Press
        has = has - 1
        if has not in turple:
            has = 4
        else:
            board[has] = kursor
            interface()
            board[has] = " "
        return False
    elif key == keyboard.Key.right:      #reaction for Key.right Press
        has = has + 1
        if has not in turple:
            has = 4
        else:
            board[has] = kursor
            interface()
            board[has] = " "
        return False

interface()
board[has] = " "
while True:                          #loop until full

    with keyboard.Listener(
        on_release=on_release) as listener:
        listener.join()
    if board == fullX or board == fullO :
        break




