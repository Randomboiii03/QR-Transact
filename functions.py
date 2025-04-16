import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def set_links(file_id: str) -> dict:
    return {
        "preview_url": f"https://drive.google.com/thumbnail?id={file_id}&sz=w1000",
        "download_url": f"https://drive.google.com/uc?export=download&id={file_id}"
    }

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_receipt_email(email, name, number, txn_number, image_stream=None, image_filename='transaction_image.jpg'):
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = os.getenv('EMAIL_ADDRESS')
        msg['To'] = email
        msg['Subject'] = 'Transaction Receipt'

        # HTML Body content
        body = f"""
        <html>
        <head>
            <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
            }}
            .container {{
                width: 100%;
                max-width: 600px;
                margin: 20px auto;
                background-color: #fff;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            h2 {{
                text-align: center;
                color: #333;
            }}
            .details {{
                margin: 20px 0;
            }}
            .details p {{
                font-size: 16px;
                margin: 10px 0;
                color: #555;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #777;
                margin-top: 20px;
            }}
            .highlight {{
                font-weight: bold;
                color: #333;
            }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Transaction Receipt</h2>
                <div class="details">
                    <p><span class="highlight">Name:</span> {name}</p>
                    <p><span class="highlight">Email:</span> {email}</p>
                    <p><span class="highlight">Number:</span> {number}</p>
                    <p><span class="highlight">Transaction Number:</span> {txn_number}</p>
                </div>
                <div class="footer">
                    <p>Thank you for your transaction. If you have any questions, feel free to contact us.</p>
                    <p>&copy; 2025 Your Company Name. All rights reserved.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Attach the HTML body as 'text/html'
        msg.attach(MIMEText(body, 'html'))

        # Attach Image if provided
        if image_stream and image_filename:
            image_stream.seek(0)  # Ensure the pointer is at the start of the stream
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(image_stream.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{image_filename}"')
            msg.attach(part)

        # Send the email using Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(os.getenv('EMAIL_ADDRESS'), os.getenv('EMAIL_PASSWORD'))
            server.send_message(msg)

        return True  # ✅ Email sent successfully

    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        return False  # ❌ Email sending failed
