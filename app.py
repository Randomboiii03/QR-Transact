from flask import Flask, render_template, request
from functions import set_links, send_receipt_email
from werkzeug.utils import secure_filename
import io


app = Flask(__name__)

@app.route('/')
def index():
    qrcode = request.args.get('qrcode', '')
    origin_url = request.args.get('origin', '')

    if not qrcode or not origin_url:
        return render_template('404.html'), 404

    links = set_links(qrcode)
    return render_template('index.html', image_url=links['preview_url'], download_url=links['download_url'], origin_url=origin_url)


@app.route('/result', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    txn_number = request.form.get('txn_number', '')
    origin_url = request.form.get('origin_url', '')

    txn_image = request.files.get('txn_image')
    image_stream = None
    image_filename = None

    if txn_image and txn_image.filename:
        image_filename = secure_filename(txn_image.filename)
        image_stream = io.BytesIO(txn_image.read())  # Keep image in memory

    # Pass in-memory image stream to email function
    status = send_receipt_email(
        email=email,
        name=name,
        number=number,
        txn_number=txn_number,
        image_stream=image_stream,
        image_filename=image_filename
    )

    # Redirect back with original QR code link
    if status:
        return render_template('success.html', email=email, origin_url=origin_url)
    else:
        return render_template('404.html'), 404
    

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('404.html'), 500