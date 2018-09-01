import smtplib

fromaddr = 'user_me@gmail.com'
toaddrs  = 'user_you@gmail.com'
msg = 'Why,Oh why!'
username = 'user_me@gmail.com'
password = 'pwd'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
