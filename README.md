# 🛒 Amazon Price Tracker

A Python automation project that monitors the price of an Amazon product and sends an email notification when the price drops below a specified target.

## 🚀 Features

* Scrapes the latest product price from Amazon.
* Extracts the product title and current price.
* Compares the current price against a predefined target.
* Sends an email alert automatically when the product goes on sale.
* Uses environment variables to securely store email credentials.

## 🛠️ Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* SMTP
* python-dotenv

## 📂 Project Structure

```text
.
├── main.py
├── .env.example
├── .gitignore
└── README.md
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/shriabhishek251/amazon-price-tracker.git
```

Install dependencies:

```bash
pip install requests beautifulsoup4 python-dotenv
```

Create a `.env` file using `.env.example`.

Example:

```text
SMTP_ADDRESS=smtp.gmail.com
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_google_app_password
```

Run the script:

```bash
python main.py
```

## 📚 What I Learned

* Web scraping using BeautifulSoup.
* Sending HTTP requests with custom headers.
* Parsing HTML to extract product information.
* Sending emails using SMTP.
* Managing secrets securely using environment variables.
* Automating repetitive tasks with Python.

## ⚠️ Notes

* Amazon frequently changes its webpage structure, so selectors may need updating in the future.
* A Google App Password is required for Gmail SMTP authentication.
* Never commit your `.env` file to GitHub.

## Author
Abhishek Kumar