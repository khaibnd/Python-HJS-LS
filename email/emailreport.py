import smtplib

from email.message import EmailMessage

message = EmailMessage()
message.set_content('Message test content')
message['Subject'] = 'Test mail!'
message['From'] = 'me@whatever.com'
message['To'] = 'buingocduykhai@gmail.com'

smtp_server = smtplib.SMTP('aspmx.l.google.com:25')
smtp_server.send_message(message)
smtp_server.quit()