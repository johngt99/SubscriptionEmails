import os
import smtplib
import imghdr
from email.message import EmailMessage

from executable import to
# from weekly import toW, freqW
# from monthly import toM, freqM

# if freqW == 'weekly':
#     to = toW
# elif freqM == 'monthly':
#     to = toM

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')



msg = EmailMessage()
msg['Subject'] = 'Content About Cars'
msg['From'] = EMAIL_ADDRESS
msg['To'] = to
msg.set_content('This is a plain text email...')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;"> CARS </h1>
    </body>
</html>
""", subtype = 'html')


files = ['images\cars.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)