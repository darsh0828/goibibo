import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("test.001two@gmail.com", "Asdfgh_1")
server.sendmail("test.001two@gmail.com", "darshan326852@gmail.com", "hello, how are you?")
server.quit()