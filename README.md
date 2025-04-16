# QR-Transact

A simple Flask web application for QR-based payment collection. Users can scan a QR code, upload payment transaction screenshots, and receive a transaction receipt via email. The application integrates with Google Drive for QR image hosting and supports in-memory image handling.

---

## Features

- 🔳 Displays QR code from a Google Drive file ID  
- 📷 Accepts transaction screenshot uploads  
- 📧 Sends styled email receipts with optional image attachments  
- 🧼 No file persistence – uses in-memory image handling  
- 🔗 Redirects user back to the originating site after submission  

---

## Tech Stack

- **Backend**: Flask (Python)  
- **Frontend**: Tailwind CSS  
- **Email**: SMTP with Gmail  
- **Hosting QR Code**: Google Drive (thumbnail and download link support)  

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Randomboiii03/QR-Transact.git
   cd QR-Transact
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Rename the `.env.example` file to `.env`:
   ```env
   EMAIL_ADDRESS=your.email@example.com
   EMAIL_PASSWORD=your_app_password
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Usage URL**
   Open the app at:

   ```
   http://127.0.0.1:5000/?qrcode=DRIVE_FILE_ID&origin=https://yourwebsite.com
   ```

---

## Example Google Drive QR Link

- `qrcode` = Google Drive File ID of the QR image  
- `origin` = URL to return after successful form submission  

Example:
```
http://127.0.0.1:5000/?qrcode=1AbCdEfGhIjKlMnOpQrStUvWxYz123456&origin=https://example.com
```
