import os
import smtplib
from flask import Flask, render_template, request
from scraper import check_price
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


def send_email(message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(os.environ["EMAIL_ADRESS"], os.environ["EMAIL_PASSWORD"])
            msg = f"Subject:Fiyat Alarmi!\n\n{message}".encode("utf-8")
            connection.sendmail(
                from_addr=os.environ["EMAIL_ADRESS"],
                to_addrs=os.environ["EMAIL_ADRESS"],
                msg=msg
            )
    except Exception as e:
        print(f"Email hatası: {e}")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        target_price = request.form.get("target_price")

        result_data = check_price(url, target_price)

        if result_data["success"]:
            # Eğer indirim varsa e-posta gönder
            if "İndirim!" in result_data["message"]:
                send_email(result_data["message"])
            return render_template("index.html", result=result_data["message"])
        else:
            return render_template("index.html", error=result_data["message"])

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)