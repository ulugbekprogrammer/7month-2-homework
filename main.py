import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("urakovulugbek571@gmail.com", "wxsi xeok fiag fsgy")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("urakovulugbek571@gmail.com", "shayxon1@gmail.com", message)
# terminating the session
s.quit()


import smtplib
 
# list of email_id to send the mail
li = ["shayxon1@gmail.com"]
 
for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("urakovulugbek571@gmail.com", "wxsi xeok fiag fsgy")
    message = "Message_you_need_to_send"
    s.sendmail("urakovulugbek571@gmail.com", dest, message)
    s.quit()