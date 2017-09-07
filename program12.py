#! /usr/bin/python3
import smtplib
server = smtplib.SMPT('smpt.gmail.com' ,587)
server.starttls()
server.login("avikannan13@gmail.com","kannan10")
message="how r u??"
server.sendmail("avikannan13@gmail.com","ashokmbl1999@gmail.com", message)
print("success")
server.quit()
