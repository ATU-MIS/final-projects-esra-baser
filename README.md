Markdown

# Smart Price Tracker 📉

**Smart Price Tracker** is a web-based prototype application designed to help users save money by automating price monitoring on e-commerce platforms (specifically Amazon). When a product's price drops below a user-defined target, the system sends an instant email notification.

## 🚀 Features

* **Product Tracking:** Add products via Amazon URL.
* **Price Monitoring:** Real-time web scraping to fetch current prices.
* **Target Alerts:** Set a "Target Price" and receive email alerts if the condition is met.
* **Email Notifications:** Automated SMTP-based email system.
* **User Interface:** Clean and responsive web interface built with Flask & Jinja2.

## 📂 Project Structure

This repository is organized into documentation and source code:

```text
├── Smart Price Tracker System/   # 📂 SOURCE CODE FOLDER
│   ├── templates/                # HTML templates (index.html)
│   ├── app.py                    # Main Flask application
│   ├── scraper.py                # Web scraping logic
│   ├── .env.examle               # Example credentials file
│   └── requirements.txt          # Project dependencies
│
├── Class Diagram.png             # System Class Diagram
├── Use Case Diagram.png          # System Use Case Diagram
├── sequence diagram.png          # System Sequence Diagram
├── Req_A_Esra Başer.doc          # Software Requirements Specification (SRS)
├── USABILITY TEST REPORT.docx    # Usability Test Results
├── Use case scenario.docx        # Detailed Use Case Scenarios
└── README.md                     # Project Documentation
⚙️ Installation & Setup
To run the application, please follow these steps:

Clone the Repository

Bash

git clone [https://github.com/yourusername/smart-price-tracker.git](https://github.com/yourusername/smart-price-tracker.git)
Navigate to the Code Directory The source code is located in the Smart Price Tracker System folder.

Bash

cd "Smart Price Tracker System"
Install Dependencies Ensure you have Python installed. Then run:

Bash

pip install -r requirements.txt
(Required libraries: flask, beautifulsoup4, requests, python-dotenv)

Configure Environment Variables

Rename the file .env.examle to .env.

Open .env and enter your email credentials:

Plaintext

EMAIL_ADRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SMTP_ADRESS=smtp.gmail.com
> Note: For Gmail, please use an "App Password" instead of your regular password.

Run the Application

Bash

python app.py
Access the App Open your browser and go to: http://127.0.0.1:5000

📄 Documentation & Diagrams
All project documentation and UML diagrams are available in the root directory of this repository:

Requirements Specification: Req_A_Esra Başer.doc

Usability Test Report: USABILITY TEST REPORT.docx

Use Case Scenarios: Use case scenario.docx

System Diagrams:

Class Diagram

Use Case Diagram

Sequence Diagram

⚠️ Disclaimer
This project is a prototype developed for a Software Engineering course. It is intended for educational purposes only.

👥 Author
Esra Başer - Developer & Tester
