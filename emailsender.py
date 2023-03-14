import smtplib
Emailreceiver = input ("Enter the recepient email address: ")
content = input ("Enter the message: ")

def sendEmail(Emailreceiver,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("your gmail address", 'youremailpassword!')
    server.sendmail("sender email", Emailreceiver, content)
    server.close()
sendEmail(Emailreceiver,content)