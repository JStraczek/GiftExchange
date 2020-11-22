# -*- coding: utf-8 -*-
import smtplib, ssl
import requests
import random
import copy

class Receiver:
    def __init__(self, details):
        self.name = details[0].strip()
        self.surname = details[1].strip()
        self.email = details[2].strip()
        self.tip = details[3].strip()

class Santa:
    sender_email = input("Type your email and press enter: ")
    password = input("Type your password and press enter: ")

    # forbidden_pairs = []
    forbidden_pairs = [ # Add pairs that you don't want to be rolled

        {"John Smith", "Jan Nowak"}, 
        {"May Hew", "January West"}

        ]

    def get_receiver_list(self):
        self.receivers = []
        #DOWNLOADING FROM SHEETS
        r = requests.get("INSERT HERE OR IT WON'T WORK") # put your api spreadsheets link here
        
        if r.status_code == 200:
            # SUCCESS 
            data = r.json()
        else:
            # ERROR
            data=None

        for el in data['data']:
            self.receivers.append(Receiver(list(el.values())))
        

    def forbidden_pair(self, p1, p2):
        if p1 == p2:
             return True
        else if self.forbidden_pairs:
            pair = {f'{p1.name} {p1.surname}', f'{p2.name} {p2.surname}'}

            for el in self.forbidden_pairs:
                if pair.difference(el) == set():
                    return True

        return False

    def check_if_valid(self, receivers, shuffled_receivers):
        for i, j in zip(receivers, shuffled_receivers):
            if(self.forbidden_pair(i, j)):
                return False
        return True

    def get_pairings(self):
        shuffled_receivers = copy.copy(self.receivers)
        random.shuffle(shuffled_receivers)
        while self.check_if_valid(self.receivers, shuffled_receivers) == False:
            random.shuffle(shuffled_receivers)
        
        return zip(self.receivers, shuffled_receivers)


    def send_out_emails(self):
        # SENDING
        port = 465  # For SSL
        context = ssl.create_default_context()

        # Create a secure SSL context
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(self.sender_email, self.password)
            id = [i for i in range(1, 15)]
            random.shuffle(id)

            for gift_giver, gift_receiver in self.get_pairings():
                receiver_email = gift_giver.email
                message = f"""\
                Swiety Mikolaj\n\n

                Czesc {gift_giver.name} {gift_giver.surname},
                to juz dzisiaj, osoba, ktorej kupisz prezent to: {gift_receiver.name} {gift_receiver.surname}
                ta osoba chce dostać: {gift_receiver.tip}
                id: {id.pop()}
                Wesolych swiat ! ;)))
                Swiety Mikolaj
                """.encode('utf-8')

                server.sendmail(self.sender_email, receiver_email, message)
    
    def christmas_time(self):
        self.get_receiver_list()
        self.send_out_emails()
