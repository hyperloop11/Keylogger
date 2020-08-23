# Keylogger
A keylogger is a malicious piece of software that records keystrokes on a computer and sends them to other parties via the internet. A major disadvantage of keyloggers over other malware (in terms of security) is that they go undetected by most anti-virus softwares.

This keylogger records keystrokes for a specified amount of time in a temporary file (.tmp) and sends them to a predefined email as an attachment. After that, it deletes the file from the target machine and creates a new file, repeating the process till the program is stopped.

# Requirements
1. An active internet connection for both the sending and receiving computers.
2. Python 3
3. Pynput library

# Usage
1. Change the value of from_add and to_add on line 29 and 30.
2. Add password of from_add on line 52.
3. Change the amount of listening time on line 80. It is currently set to 10 seconds.

Lastly, I hope this piece of software is used for educational purposes only.
