from pynput import keyboard

def on_release(key):
    if key == keyboard.Key.up:
        print('swinia gora')
    elif key == keyboard.Key.down:
        print('swinia dol')
    elif key == keyboard.Key.left:
        print('swinia lewa')
    elif key == keyboard.Key.right:
        print('swinia prawa')
    elif key == keyboard.Key.esc:
        return False
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()