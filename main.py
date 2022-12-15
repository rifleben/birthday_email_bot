import datetime as dt
import smtplib
import random

my_email = "I PUT MY EMAIL HERE"
password = "DEDICATED PASS HERE"

today = (dt.datetime.now().month, dt.datetime.now().day)

datafile = pandas.read_csv("birthdays.csv")


birthdays = {(datarow["month"], datarow["day"]): datarow for (index, datarow) in datafile.iterrows()}

if today in birthdays:
    birthday_person = birthdays[today]
    random_num = random.randint(1, 3)
    file_path = f"letter_templates/letter_{random_num}.txt"
    
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")
