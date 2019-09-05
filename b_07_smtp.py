#! /usr/bin/env python3

"""
This part will use smtplib
to send a simple email
"""

import smtplib

from email.mime.text import MIMEText
from email.header import Header

sender="from@yu.com"
receivers=["yuecnu@hotmail.com"]

message=MIMEText('This is a test email...','plain','utf-8')
message['From']=Header("Xiangyong",'utf-8')
message['To']=Header("Felix", 'utf-8')

subject='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa g SMTP Example'
message['Subject']=Header(subject,'utf-8')

#ensure postfix service started 
try:
    smtpObj=smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("succeed")
except:
    print("error")




import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr

sender="from@yu.com"
receivers=["yuecnu@hotmail.com"]

msgRoot=MIMEMultipart('related')
msgRoot['From'] = formataddr(['felix', sender])
msgRoot['To']=formataddr(['yu',receivers[0]])
subject='This is an email with html format'
msgRoot['Subject']=Header(subject, 'utf-8')

msgAlternative=MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg="""
<p>Python test email...</p>
<p><a href="http://www.runoob.com">Python3</a></p>
<p>Images as below:</p>
<p><img src="cid:image1"></p>
"""

msgAlternative.attach(MIMEText(mail_msg,'html','utf-8'))

with open('fedora.jpg','rb') as fe:
    msgImage=MIMEImage(fe.read())

msgImage.add_header('Content_ID','<image1>')
msgRoot.attach(msgImage)

try:
    smtpObj=smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("Second succeed")
except:
    print("Second failed")
