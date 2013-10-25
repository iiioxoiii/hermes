#Script d enviament de mail amb la grafica adjunta
#ATENCIO. Cal canviar els parametres referents al compte de correu.

# Import smtplib for the actual sending function
import smtplib

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime.application

# Import time for title file
import time
import datetime
import os


# Replace name of file
filename = 'exemple.eps'
newfilename = 'h1' + datetime.datetime.now().strftime("%d%m%y%H%M") + '.eps'
os.rename(filename, newfilename)

# Create a text/plain message
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'H1-Lectures ' + datetime.datetime.now().strftime("%d%m%y%H%M")

#Posar el correu electronic des de d'on s'envia entre cometes simples
msg['From'] = 'olakease@olake.ase'
#Posar el correu electronic on s'envien les dades entre cometes simples
msg['To'] = 'olakease@olake.ase'

# The main body is just another attachment
body = email.mime.Text.MIMEText("""Hello, how are you? I am fine.
This is H1 last report""")
msg.attach(body)

# File  attachment
filename = newfilename
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

# send via Gmail server
# NOTE: my ISP, Centurylink, seems to be automatically rewriting
# port 25 packets to be port 587 and it is trashing port 587 packets.
# So, I use the default port 25, but I authenticate. 
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
# Posat el user i el pass entre cometes simples
s.login('ristomegide','soydios001')

#Posar el lloc des de on s'envia a on va
s.sendmail('olakease@olake.ase',['olakease@olake.ase'], msg.as_string())
s.quit()
