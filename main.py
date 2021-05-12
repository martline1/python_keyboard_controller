import os
import time
from pynput.keyboard import Key, Controller

# Clears the screen
def clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def loading():
    for x in range(3):
        print("Printing in {}".format(3 - x))
        time.sleep(1)

def typeWords(keyboard):
    clear()

    sentence = input("Enter word you want to re-create: ")

    loading()

    keyboard.type(sentence)

def typeChars(pressKey):
    clear()

    keys = input("Enter the keys you want to re-create: ")

    loading()

    for c in keys:
        pressKey(c)
        time.sleep(0.5)

def main():
    keyboard = Controller()

    def pressKey(key):
        keyboard.press(key)
        keyboard.release(key)

    while True:
        clear()

        print("Python controller:\n\n")

        print("1) Words")
        print("2) Individual keys")
        print("3) Exit\n\n")

        selection = input("> ")

        if selection == "1":
            typeWords(keyboard)
        elif selection == "2":
            typeChars(pressKey)
        elif selection == "3":
            break
        else:
            continue

if __name__ == "__main__":
    main()
