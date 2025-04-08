import smtplib

# Email details
sender_email = "jsaswati35@gmail.com"
rec_email = "saswatijn@gmail.com"
password = input("Enter your email password or app password: ")

# Always include a subject and a blank line after the header
message = """\
Subject: Python Email Test

Hey, this was sent using Python!
"""

try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("Login success")

    # Send email
    server.sendmail(sender_email, rec_email, message)
    print(f"Email has been sent to {rec_email}")

    server.quit()

except Exception as e:
    print(f"Failed to send email: {e}")
