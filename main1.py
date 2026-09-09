import os
import re
from flask import Flask, render_template, request, redirect, url_for, send_file
import qrcode

app = Flask(__name__)

STATIC_FOLDER = 'static'
QR_CODE_DIR = os.path.join(STATIC_FOLDER, 'qrcodes')
app.config['UPLOAD_FOLDER'] = QR_CODE_DIR

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Your can completed 'index' route from Module 1 should be here (Not required).
@app.route('/', methods=['GET', 'POST'])
def index():
    # This is a dummy function. Use your completed function from Module 1.
    if request.method == 'POST':
        return redirect(url_for('qr_display'))
    return render_template('index.html')

@app.route('/qr-code')
def qr_display():
    return render_template('qr_display.html')

# Create a new route for downloading the QR code file.
# This route must accept a 'filename' as a parameter.
@app.route('/download/<filename>')
def download_qr(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
