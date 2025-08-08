import smtplib
from email.mime.text import MIMEText

def send_email(to_email, condition):
    sender_email = ""
    sender_password = "your_app_password"

    subject = "Mental Health Screening Result"
    body = f"Based on your responses, the AI agent classified your condition as: {condition.upper()}.\nPlease consult a professional if needed."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email sent!")
    except Exception as e:
        print("Error:", e)
