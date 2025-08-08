from flask import Flask, request, render_template, jsonify
import pickle
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env

EMAIL = "dewangcdt123@gmail.com"
PASSWORD = "ixvb gbwt cvrt fnzn"

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    name = request.form['name']
    email = request.form['email']
    sleep = int(request.form['sleep'])
    appetite = int(request.form['appetite'])
    mood = int(request.form['mood'])
    suicidal_thoughts = int(request.form['suicidal_thoughts'])

    symptoms = [[sleep, appetite, mood, suicidal_thoughts]]
    prediction = model.predict(symptoms)[0]

    # Create advice based on the prediction
    prediction = prediction.strip().capitalize()

    if prediction == "Emergency":
        advice = (
            "Your symptoms indicate a critical mental health condition. "
            "We strongly urge you to seek help from a licensed mental health professional immediately. "
            "If you're in danger or need urgent support, contact your nearest mental health helpline."
        )
    elif prediction == "Moderate":
        advice = (
            "Your symptoms suggest moderate mental health challenges. "
            "It is recommended to schedule a consultation with a therapist or counselor soon."
        )
    else:
        advice = (
            "Your symptoms currently indicate a stable mental health condition. "
            "Continue maintaining a healthy routine, stay connected with loved ones, and practice self-care."
        )

    # Format email content
    subject = "Your Mental Health Screening Report"
    body = f"""
Dear {name},

Thank you for completing the mental health screening.

🧠 **Screening Result**: {prediction}

📋 **Our Advice**:
{advice}

Please remember that this is an AI-based assessment and not a substitute for a medical diagnosis. 
For any concerns, it is best to consult a qualified mental health professional.

Take care and stay safe,
Mental Wellness AI Team
"""

    # Send the email
    send_email(email, subject, body)

    return jsonify({"message": "Email sent successfully check your Gmail", "prediction": prediction})


def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['From'] = EMAIL
    msg['To'] = to
    msg['Subject'] = subject

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, to, msg.as_string())
    server.quit()


if __name__ == '__main__':
    app.run(debug=True)
