from datetime import datetime
import locale
import smtplib
import random

MY_EMAIL = "martynas.rusakas@gmail.com"
PASSWORD = "password..."
now = datetime.now()
if now.strftime('%A') == "Sunday":
    with open("quotes.txt") as f:
        quotes = f.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="martynas.rusakas@gmail.com",
            msg=f"Subject: Quote \n\n{random.choice(quotes)}"
        )
