import smtplib
from email.mime.text import MIMEText

# Email details
from_email = "je"  # The spoofed sender's email address
to_email = "aa"       # Replace with the TA's actual email
subject = "[Action Required] Secure Your University Portal Account"
body = """
Dear TA,

We have detected unusual activity on your University Portal account that requires immediate attention. To protect your account and ensure uninterrupted access, we kindly ask you to verify your credentials by completing a quick security check.

**Action Required**: Please click the link below to verify your account information:
👉 http://127.0.0.1:8080/login.html

Failure to verify your account within 24 hours will result in a temporary suspension of your account as part of our security protocol.

If you have any questions or require assistance, please contact IT Support at support@university.edu.

Thank you,
University IT Services
"""

# Create the email
msg = MIMEText(body, "plain")
msg["Subject"] = subject
msg["From"] = from_email
msg["To"] = to_email

# SMTP server configuration
smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
smtp_port = 587                 # Replace with your SMTP server port
smtp_username = "jeff"  # Replace with your email
smtp_password = "A"  # Replace with your password

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Upgrade connection to secure
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
    print("Phishing email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
