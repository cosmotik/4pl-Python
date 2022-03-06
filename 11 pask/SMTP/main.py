import smtplib

MY_EMAIL = "martynas.rusakas@gmail.com"
PASSWORD = "Avax1234567"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="martynas.rusakas@gmail.com",
        msg="Subject:This is subject\n\nHello from python code!"
    )