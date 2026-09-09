import os
import re
from flask import Flask, render_template, request, send_file, redirect, url_for
import qrcode

# Initialize the Flask application
app = Flask(__name__)

# Configuration: Define the folder to store generated QR codes
STATIC_FOLDER = 'static'
QR_CODE_DIR = os.path.join(STATIC_FOLDER, 'qrcodes')
app.config['UPLOAD_FOLDER'] = QR_CODE_DIR

# Ensure the directory for storing QR codes exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def validate_linkedin_url(url):
    """
    Validates if the provided URL is a standard LinkedIn profile or company URL.
    Returns True if valid, False otherwise.
    """
    # Regex to match LinkedIn profile (e.g., /in/username) or company (e.g., /company/company-name) pages.
    # It checks for http/https, optional www, the domain, and the specific paths.
    linkedin_pattern = re.compile(r'^https?://(www\.)?linkedin\.com/(in|company)/[\w-]+/?$')
    return re.match(linkedin_pattern, url) is not None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        linkedin_url = request.form.get('linkedin_url')

        # Step 1: Validate the URL
        if not linkedin_url or not validate_linkedin_url(linkedin_url):
            error_message = "Invalid URL. Please provide a valid LinkedIn profile or company page link."
            # If invalid, re-render the home page with an error message
            return render_template('index.html', error=error_message)

        # Step 2: If valid, generate the QR code
        img = qrcode.make(linkedin_url)
        qr_code_filename = "linkedin_profile_qr.png"
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], qr_code_filename)
        img.save(save_path)

        # Step 3: Redirect to the new QR display page
        return redirect(url_for('qr_display'))
    
    # For a GET request, just show the home page without any error
    return render_template('index.html', error=None)

@app.route('/qr-code')
def qr_display():
    """
    This route displays the page with the generated QR code.
    """
    return render_template('qr_display.html')

# This block is kept for direct execution (e.g., `python main.py`)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
