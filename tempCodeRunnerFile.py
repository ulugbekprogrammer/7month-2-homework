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
s.sendmail("urakovulugbek571@gmail.com", "mamajonovibrokhimjon@gmail.com", message)
# terminating the session
s.quit()