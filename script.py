# -*- coding: utf-8 -*-
import smtplib, ssl
import requests

class Receiver:
        def __init__(self, details):
            self.name = details[0]
            self.surname = details[1]
            self.email = details[2]
            self.tip = details[3]

def get_receiver_list():

    #DOWNLOADING FROM SHEETS
    r = requests.get("https://api.apispreadsheets.com/data/3399/")

    if r.status_code == 200:
        # SUCCESS 
        data = r.json()
    else:
        # ERROR
        data=None

    receivers = []
    for el in data['data']:
        receivers.append(Receiver(list(el.values())))
    
    return receivers

receivers = get_receiver_list()

# SENDING

sender_email = input("Type your email and press enter: ")
password = input("Type your password and press enter: ")
port = 465  # For SSL
context = ssl.create_default_context()

# Create a secure SSL context

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    # receivers=[Receiver(['jakub', 'straczek', 'kubastr98@gmail.com', 'costam'])]
    for person in receivers:
        receiver_email = person.email
        message = f""" 
        Prezentodawansko\n\n

        Czesc {person.name} {person.surname},
        to tylko testowy mail, wylosowana osobe dostaniesz kiedy indziej JD,
        Oto podpowiedz jaka otrzyma mikolaj/mikolajowa w sprawie Twojego prezentu: {person.tip}
        Wesolych swiat :))))) 
        """.encode('utf-8')

        server.sendmail(sender_email, receiver_email, message)