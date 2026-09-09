# Linkedin-QR-Code-Generator

LinkedIn QR Code Generator
Welcome, developer! In this project, you will build a web application using Flask that generates a QR code for a user's LinkedIn profile. The final application will allow a user to input their LinkedIn profile URL, generate a corresponding QR code, and download it.

Environment and Setup

For this project, your environment is already prepared.

The necessary Python libraries (Flask, qrcode, Pillow) are pre-installed.
The User Interface (UI) templates are already provided for you in the templates/ directory. You do not need to write any HTML; you only need to focus on the backend logic in main.py.
The project is broken down into two components. We will tackle the first one now.

Project Breakdown

Component 1: URL Validation and QR Code Generation. You will implement the core logic to validate the user's input and generate a QR code from a valid URL.
Component 2: You will enhance the application by adding functionality to download the generated QR code and navigate back to the home page.
Note - If you're not familiar with Flask, you can quickly get up to speed using this beginner-friendly guide on CodeChef’s Flask Course. It's a great place to start and will help you understand the basics you'll need for this project.

Let's begin with Component 1.

Component 1: Validate Input and Generate the QR Code
Your Task

Your goal is to modify the provided main.py file to create the backend logic for our QR code generator. You must implement the following features:

Handle both GET and POST requests on the / route.
On form submission, check the LinkedIn URL. Make sure it's either a profile link (linkedin.com/in/...) or a company page (linkedin.com/company/...).
If the URL is invalid, simply reload the form page and make sure a meaningful error appears (Hint: the index.html template already supports an error variable).
If valid, generate the QR code image, save it as linkedin_profile_qr.png under the static/qrcodes/ folder.
Then redirect the user to /qr-code where they’ll see the result.
Don't forget: if the error message doesn't show up for invalid URLs, double-check what variable you’re passing into your template.

Click the Run button to view the app, then click the Submit button to check whether your code is correct.

