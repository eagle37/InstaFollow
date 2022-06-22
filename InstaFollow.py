"""
Author: @new92
InstaFollow: Program for increasing followers
Not for illegal purposes !
The author is not responsible for any illegal activities carried out using this program
User's data (such as: username, password) will not be stored or saved ! 
Will be used only to increase followers of the given account
The author has no responsibility for any damages caused in the accounts
"""

#Imports
try:
    import instagrapi
    import nmap 
    import time
    import sniffer
    import locale
    import pyfiglet
    import platform
    import socket
    import requests
    import os
    import logging
    import sys
    import crypto
    import cryptography
    import geocoder
    import instaloader
    import getpass
    from getpass import getpass
    from geopy.geocoders import Nominatim
except ImportError as imp:
    print("Error ! Please make sure you have installed all the modules !")
    time.sleep(1)
    print("Please enter the command: pip3 install InstaRequirements.txt")
    time.sleep(1)
    print("And execute again the program")
    time.sleep(1)
    print(imp)
#End of Imports

#Logo
instafollow=pyfiglet.figlet_format("InstaFollow")
print(instafollow)

#Main program
print("[+] Github: @new92")
print("\n")
print("[01] Increase Followers")
print("[02] Exit")
print("\n")
option=input("[::] Choose an option: ")

while option != "01" and option != "02" and option != "1" and option != "2":
    print("Invalid option !")
    option=input("[::] Please enter again: ")
if option == "01" or option == "1":
    try:
        print("The data will not be stored or saved")
        time.sleep(2)
        username=input("Please enter your username: ")
        username=username.lower()
        username=username.strip()
        time.sleep(1)
        password=input("Please enter your password: ")
        password=password.strip()
        time.sleep(1)
        clnt=instagrapi.Client()
    except Exception as ex:
        print("Error !")
        print(ex)
    try:
        clnt.login(username,password)
    except Exception as e:
        print("Error !")
        print(e)
    print("Please wait while the program is increasing your followers...")
    time.sleep(2)
    print("This process might take some time...")
    time.sleep(2)
    print("To end the process enter Ctrl + C")
    i = 1
    while i > 0:
        try:
            clnt.user_follow(173560420) #Cristiano Ronaldo
            clnt.user_follow(1436859892) #Cardi B
            clnt.user_follow(18428658) #Kim Kardashian
            clnt.user_follow(7719696) #Ariana Grande
            clnt.user_follow(451573056) #Nicki Minaj
            clnt.user_follow(247944034) #Beyonce
            clnt.user_follow(407964088) #Katy Perry
            clnt.user_follow(460563723) #Selena Gomez
            clnt.user_follow(6860189) #Justin Bieber
            clnt.user_follow(427553890) #Lionel Messi
            clnt.user_follow(26669533) #Neymar Jr
            clnt.user_follow(4213518589) #Kylian Mbappe
            clnt.user_follow(1234301500) #Karim Benzema
            clnt.user_follow(12331195) #Dua Lipa
            clnt.user_follow(28527810) #Billie Eilish
            clnt.user_follow(12281817) #Kylie Jenner
            clnt.user_follow(208560325) #Khloe Kardashian
            clnt.user_follow(145821237) #Kourtney Kardashian
            clnt.user_follow(305701719) #Jennifer Lopez
            clnt.user_follow(217867189) #Shakira
            clnt.user_unfollow(173560420) #Cristiano Ronaldo
            clnt.user_unfollow(1436859892) #Cardi B
            clnt.user_unfollow(18428658) #Kim Kardashian
            clnt.user_unfollow(7719696) #Ariana Grande
            clnt.user_unfollow(451573056) #Nicki Minaj
            clnt.user_unfollow(247944034) #Beyonce
            clnt.user_unfollow(407964088) #Katy Perry
            clnt.user_unfollow(460563723) #Selena Gomez
            clnt.user_unfollow(6860189) #Justin Bieber
            clnt.user_unfollow(427553890) #Lionel Messi
            clnt.user_unfollow(26669533) #Neymar Jr
            clnt.user_unfollow(4213518589) #Kylian Mbappe
            clnt.user_unfollow(1234301500) #Karim Benzema
            clnt.user_unfollow(12331195) #Dua Lipa
            clnt.user_unfollow(28527810) #Billie Eilish
            clnt.user_unfollow(12281817) #Kylie Jenner
            clnt.user_unfollow(208560325) #Khloe Kardashian
            clnt.user_unfollow(145821237) #Kourtney Kardashian
            clnt.user_unfollow(305701719) #Jennifer Lopez
            clnt.user_unfollow(217867189) #Shakira
        except Exception as ex:
            print("Error !")
            print(ex)
            quit(0)
else:
    print("Exiting...")
    time.sleep(2)
    quit(0)
#End of the Program
