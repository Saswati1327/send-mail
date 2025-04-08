import tkinter as tk
from tkinter import messagebox, filedialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Function to send the email
def send_email():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    receiver_email = receiver_email_entry.get()
    email_text = email_text_entry.get("1.0", tk.END)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Test Email with Attachment"

    # Attach the body of the email
    msg.attach(MIMEText(email_text, 'plain'))

    # Attach the file if one is selected
    if attachment_path:
        try:
            # Open the file to be sent
            with open(attachment_path, "rb") as attachment_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment_file.read())

            # Encode the file in base64
            encoders.encode_base64(part)

            # Add the header to the attachment
            part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')

            # Attach the file to the email
            msg.attach(part)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to attach file: {str(e)}")
            return

    # Try sending the email
    try:
        # Establish connection with SMTP server (Gmail in this case)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the sender email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)  # Send email
        server.quit()

        # Show success message
        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")


# Function to attach a file
def attach_file():
    global attachment_path
    attachment_path = filedialog.askopenfilename(title="Select a File to Attach")
    if attachment_path:
        attach_button.config(text=f"Attached: {attachment_path.split('/')[-1]}")  # Show file name

# Create the main window
root = tk.Tk()
root.title("Email Sender with Attachment")

# Initialize attachment_path variable
attachment_path = ""

# Create and place widgets on the window
sender_email_label = tk.Label(root, text="Sender Email:")
sender_email_label.grid(row=0, column=0, padx=10, pady=5)
sender_email_entry = tk.Entry(root, width=40)
sender_email_entry.grid(row=0, column=1, padx=10, pady=5)

sender_password_label = tk.Label(root, text="Sender Password:")
sender_password_label.grid(row=1, column=0, padx=10, pady=5)
sender_password_entry = tk.Entry(root, width=40, show="*")
sender_password_entry.grid(row=1, column=1, padx=10, pady=5)

receiver_email_label = tk.Label(root, text="Receiver Email:")
receiver_email_label.grid(row=2, column=0, padx=10, pady=5)
receiver_email_entry = tk.Entry(root, width=40)
receiver_email_entry.grid(row=2, column=1, padx=10, pady=5)

email_text_label = tk.Label(root, text="Email Text:")
email_text_label.grid(row=3, column=0, padx=10, pady=5)
email_text_entry = tk.Text(root, width=40, height=10)
email_text_entry.grid(row=3, column=1, padx=10, pady=5)

# Attach file button
attach_button = tk.Button(root, text="Attach File", command=attach_file)
attach_button.grid(row=4, columnspan=2, pady=10)

# Send button
send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=5, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()