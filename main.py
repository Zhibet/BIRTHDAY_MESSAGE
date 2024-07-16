import random
import pandas as pd
import datetime
import os
import smtplib

# 1. Update the birthdays.csv
current_date = datetime.date.today()
current_day = current_date.day

df = pd.read_csv('birthdays.csv')
data = df.to_dict(orient='records')

folder = 'letter_templates'
letters = os.listdir(folder)
random_letter = random.choice(letters)
birth_day = None

for data_frame in data:
    birth_day = data_frame['day']
    person = data_frame['name']
    # 2. Check if today matches a birthday in the birthdays.csv
    if birth_day == current_day:
        with open(f'{folder}/{random_letter}','r') as file:
            letter_content = file.read()
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            official_letter = letter_content.replace("Dear [NAME]", f'Dear {person}')
            official_letter = official_letter.replace("Hey [NAME]", f'Dear {person}')
            print(official_letter)
            # 4. Send the letter generated in step 3 to that person's email address.
            destination_email = data_frame['email']
            sender_email = 'amadoubah12341@gmail.com'
            password = 'afszdravqjuijbyu'
            subject = f' Happy Birthday {person}'
            body = official_letter
            message = f'Subject: {subject}\n\n{body}'


            def send_email():
                try:
                    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                        connection.starttls()
                        connection.login(user=sender_email, password=password)
                        connection.sendmail(from_addr=sender_email, to_addrs=destination_email, msg=message)
                    print("Email sent successfully")
                except Exception as e:
                    print(f'Error: {e}')
            send_email()