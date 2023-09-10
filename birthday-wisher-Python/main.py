# Please update the CSV file "birthdays.csv" with your contact's list information

import pandas
import random
import smtplib
import datetime as dt

# insert your own email and password below
USERNAME = "example@gmail.com"
PASSWORD = "password123"

data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient="records")
now = dt.datetime.now()

for records in data:
    if records["month"] == now.month and records["day"] == now.weekday():
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            l = letter.read()
            l = l.replace("[NAME]", records["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(USERNAME, PASSWORD)
            connection.sendmail(
                from_addr=USERNAME,
                to_addrs=USERNAME,
                msg=f"Subject:Happy Birthday\n\n{l}")
