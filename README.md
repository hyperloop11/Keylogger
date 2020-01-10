# Keylogger
This programme can record keystrokes typed on target computer's keyboard and sends periodic emails with the file as attachment.
It stores the keystrokes in a text file in temporary folder and then deletes the file after sending the email.
This programme only works when there is active internet connection.
To use, install python3 and pynput library. Change 'from address' and 'to address' for sending email from lines 27 and 28.
Add password of email-id on line 50.
To change time after which emails are sent, change the args on line 84.
