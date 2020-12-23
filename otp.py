import random
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
#adding TLS security 
server.starttls()
#get your app password of gmail ----as directed in the video
password='*************'
server.login('mail',' password ')
#generate OTP using random.randint() function
otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello, Your OTP is '+str(otp)
sender=''  #write email id of sender
receiver='' #write email of receiver
#sendi
server.sendmail('mail','mail2',msg)
server.quit()