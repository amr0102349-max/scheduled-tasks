# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas
import random
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")
now = dt.datetime.now()
today = (now.month , now.day)

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
dict_of_birthday ={(data_row["month"] , data_row["day"]) : data_row for (index , data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv

if today in dict_of_birthday :
   name_of_person = dict_of_birthday[today]
   letters = f"letter_templates/letter_{random.randint(1,3)}.txt"
   with open (letters) as letter_file :
      contents =  letter_file.read()
      contents = contents.replace("[NAME]" , name_of_person ["name"])

   with smtplib.SMTP("smtp.gmail.com" , 587) as connection :
       connection.starttls()
       connection.login(user = MY_EMAIL , password = PASSWORD)
       connection.sendmail(from_addr= MY_EMAIL  ,
                           to_addrs= name_of_person ["email"],
                           msg = f"subject : Happy birthday\n\n {contents}")
       print("Done")
else :
   print("no one ")

