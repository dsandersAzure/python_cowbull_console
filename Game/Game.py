import json
import os
import requests
from time import sleep


class Game:
    welcome_msg = "Welcome to the CowBull game. The objective of this game is to guess " \
                   "a set of four digits (numbers between 0 and 9) by entering a sequence " \
                   "of numbers. Each time you try to guess, you will see an analysis of " \
                   "your guesses: * is a bull (the right number in the right place), - (" \
                   "the right number in the wrong place), x is a miss, and any of the other " \
                   "symbols followed with + means that the number occurs more than once."

    def __init__(self):
        self.host_url = os.getenv("cowbull_host", "localhost")
        self.host_port = os.getenv("cowbull_port", 5000)
        self.host_ver = os.getenv("cowbull_version", "v0_1")
        self.game_url = "http://{}:{}/{}/game".format(self.host_url, self.host_port, self.host_ver)

    def instructions(self):
        print()
        print(self.welcome_msg)
        print()

    def want_to_play(self):
        while True:
            answer = input("Do you want to play? (Yes/No) ")
            if answer.lower() in ['yes', 'y', 'no', 'n']:
                break
        if answer.lower() in ["yes", "y"]:
            return True
        else:
            return False

    def check_server_ready(self):
        return_status = False
        try_count = 0

        while try_count < 5:
            try:
                r = requests.post(url=self.game_url)
                return_status = True
                break
            except requests.ConnectionError as ce:
                print("Connectiong failed. Re-trying in {} seconds...".format(2 * (try_count + 1)))
                sleep(2 * (try_count + 1))
                pass
            except Exception as e:
                print()
                print("An unexpected error occurred! {}".format(repr(e)))
                break
            try_count += 1

        return return_status
