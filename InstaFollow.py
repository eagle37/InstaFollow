"""
Author: @new92
InstaBot: Program for increasing followers
Not for illegal purposes !
The author is not responsible for any illegal activities carried out using this program
User's data (such as: username, password) will not be stored or saved ! 
Will be used only to increase followers of the given account
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
    import geocoder
    from geopy.geocoders import Nominatim
except ImportError as imp:
    print("Error ! Please make sure you have installed all the modules !")
    print("Modules used: instagrapi, nmap, time, sniffer, locale, pyfiglet, platform, socket, requests, os, sys, logging, geocoder, from geopy.geocoder import Nominatim")
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

while option != "01" and option != "02":
    print("Invalid option !")
    option=input("[::] Please enter again: ")
if option == "01":
    try:
        print("The data will not be stored or saved")
        username=input("Please enter your username: ")
        time.sleep(1)
        password=input("Please enter your password: ")
        time.sleep(1)
        clnt=instagrapi.Client()
    except Exception as ex:
        print("Error !")
        print(ex)
    clnt.login(username,password)
    print("Please wait while the program is increasing your followers...")
    print("To end the process enter Ctrl + C")
    try:
        i = 1
        while i > 0:
            clnt.user_follow(173560420) #Cristiano Ronaldo
            time.sleep(3)
            clnt.user_follow(1436859892) #Cardi B
            time.sleep(3)
            clnt.user_follow(18428658) #Kim Kardashian
            time.sleep(3)
            clnt.user_follow(7719696) #Ariana Grande
            time.sleep(3)
            clnt.user_follow(451573056) #Nicki Minaj
            time.sleep(3)
            clnt.user_follow(247944034) #Beyonce
            time.sleep(3)
            clnt.user_follow(407964088) #Katy Perry
            time.sleep(3)
            clnt.user_follow(460563723) #Selena Gomez
            time.sleep(3)
            clnt.user_follow(6860189) #Justin Bieber
            time.sleep(3)
            clnt.user_follow(427553890) #Lionel Messi
            time.sleep(3)
            clnt.user_follow(26669533) #Neymar Jr
            time.sleep(3)
            clnt.user_follow(4213518589) #Kylian Mbappe
            time.sleep(3)
            clnt.user_follow(1234301500) #Karim Benzema
            time.sleep(3)
            clnt.user_unfollow(173560420) #Cristiano Ronaldo
            time.sleep(3)
            clnt.user_unfollow(1436859892) #Cardi B
            time.sleep(3)
            clnt.user_unfollow(18428658) #Kim Kardashian
            time.sleep(3)
            clnt.user_unfollow(7719696) #Ariana Grande
            time.sleep(3)
            clnt.user_unfollow(451573056) #Nicki Minaj
            time.sleep(3)
            clnt.user_unfollow(247944034) #Beyonce
            time.sleep(3)
            clnt.user_unfollow(407964088) #Katy Perry
            time.sleep(3)
            clnt.user_unfollow(460563723) #Selena Gomez
            time.sleep(3)
            clnt.user_unfollow(6860189) #Justin Bieber 
            time.sleep(3)
            clnt.user_unfollow(427553890) #Lionel Messi
            time.sleep(3)
            clnt.user_unfollow(26669533) #Neymar Jr
            time.sleep(3)
            clnt.user_unfollow(4213518589) #Kylian Mbappe
            time.sleep(3)
            clnt.user_unfollow(1234301500) #Karim Benzema
            time.sleep(3)
    except KeyboardInterrupt as key:
        print("Program interrupted !")
        quit(0)
else:
    print("Exiting...")
    time.sleep(2)
    quit(0)