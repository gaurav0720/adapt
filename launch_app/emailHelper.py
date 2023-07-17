import smtplib
from email.mime.text import MIMEText
from ssl import create_default_context

class EmailHelper:
    @staticmethod
    def send_uab_message(subject, msg, addresses, secure=False):
        try:
            # Prepare the email
            mail = MIMEText(msg, 'html')
            mail['Subject'] = subject
            mail['From'] = 'ADAPTMarketplace@uabmc.edu'
            mail['To'] = ', '.join(addresses)

            # Set up the SMTP server and send the email
            context = create_default_context()
            with smtplib.SMTP("hssmtp.hs.uab.edu", port=25) as server:
                server.starttls(context=context) if secure else None
                server.send_message(mail)
        except Exception as e:
            print(str(e))

    @staticmethod
    def send_uab_message_gmail(subject, msg, addresses, secure=False):
        try:
            # Prepare the email
            mail = MIMEText(msg, 'html')
            mail['Subject'] = subject
            mail['From'] = 'adaptmarketplace@gmail.com'
            mail['To'] = ', '.join(addresses)

            # Set up the SMTP server and send the email
            context = create_default_context()
            with smtplib.SMTP("smtp.gmail.com", port=587) as server:
                server.login("adaptmarketplace@gmail.com", "quyuhgrezsieoulu")
                server.starttls(context=context) if secure else None
                server.send_message(mail)
        except Exception as e:
            print(str(e))

    # @staticmethod
    # def send_uab_message(subject, msg, address):
    #     EmailHelper.send_uab_message(subject, msg, [address])

