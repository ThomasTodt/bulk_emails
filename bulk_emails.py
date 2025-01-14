
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import csv
import getpass
import time
import sys
import logging

# Configure the logging
logging.basicConfig(filename="error.log", level=logging.ERROR, format="%(message)s")

def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        
        # Set up the SMTP server
        smtp_server = "smtp-mail.outlook.com"
        smtp_port = 587

        # Create a MIMEText object to represent the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = Header(subject, 'utf-8')

        # Attach the body of the email to the message
        msg.attach(MIMEText(body, 'html'))

        # Start the SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the SMTP session
        server.quit()

        return True
    
    except smtplib.SMTPException as e:
        print(f"Error sending email to {receiver_email}: {e}")
        return False

if __name__ == "__main__":

    # Example usage
    sender_email = input("Sender Email: ")
    sender_password = getpass.getpass("Password: ")
    auto_dear = input("Do you want to use autodear? y/n: ").strip().lower()

    with open('email_subject.txt', 'r', encoding='utf-8') as subj_file:
        subject = subj_file.read().rstrip()

    with open('email_body.html', 'r', encoding='utf-8') as body_file:
        body_template = body_file.read()

    with open('email_list.csv', 'r') as lista_emails:
        total_emails = sum(1 for line in lista_emails) - 1

    with open('email_list.csv', 'r') as lista_emails:
        reader = csv.reader(lista_emails, delimiter=',')
        
        emails_sent = 0

        sys.stdout.write(f"\r{emails_sent} emails sent from {total_emails} total")
        sys.stdout.flush()
        
        for row in reader:

            receiver_name = row[0]
            receiver_email = row[1]

            if auto_dear == 'y':
                # Personalize the email body with "Dear <Name>"
                body = body_template.replace("Dear", f"Dear {receiver_name}")

            else:
                body = body_template
            
            try:
                if not send_email(sender_email, sender_password, receiver_email, subject, body):
                    raise Exception("Email sending failed")  # Simulate a failure

                emails_sent += 1
                sys.stdout.write(f"\r{emails_sent} emails sent from {total_emails} total")
                sys.stdout.flush()

            except Exception as e:
                # Log the error details to error.log
                logging.error(f"{receiver_name},{receiver_email}")

            time.sleep(2)

print()
