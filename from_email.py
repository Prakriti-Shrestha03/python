import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#password: zjql zjom hmam amzq

sender_email="Pra0000kri@gmail.com"
receiver_email="rumancha12@gmail.com"
password="jql zjom hmam amzq"

message=MIMEMultipart()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="Test Email"

body="Hello, this is a test email sent from Python"
message.attach(MIMEText(body,"plain"))

try:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")
