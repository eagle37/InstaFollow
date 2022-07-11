"""
Author: @new92
InstaFollowV2: Is a program similar to Version 1 (V1) but I found a different way to make the same program with less
lines of code.
User's data (such as: username, password) will not be stored or saved ! 
Will be used only to increase the followers of the given account
"""

#Imports
try:
    import instagrapi
    import time
    import pyfiglet
    import platform
    import socket
    import requests
    import os
    import logging
    import instabot
    import instapy
    import sys
    import instaloader
    import getpass
    import urllib
    import http
    import platform
    from getpass import getpass
    from os import system
    from instagrapi import *
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(2)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")
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
    print("[!] Invalid option !")
    time.sleep(1)
    option=input("[::] Please enter again: ")
if option == "01" or option == "1":
    print("[+] The data will not be stored or saved")
    time.sleep(2)
    username=input("[+] Please enter your username: ")
    while username == " " or username == "" or len(username) <= 2 or len(username) > 30:
        print("[!] Invalid Username !")
        time.sleep(1)
        username=input("[+] Please enter again your username: ")
    username=username.lower()
    username=username.strip()
    time.sleep(1)
    password=input("[+] Please enter your password: ")
    while password == " " or password == "" or len(password) <= 0:
        print("[!] Invalid Password !")
        time.sleep(1)
        password=input("[+] Please enter again your password: ")
    password=password.strip()
    time.sleep(1)
    clnt=instagrapi.Client()
    try:
        login = clnt.login(username,password)
        if login == True:
            print("[!] Login Successful !")
            time.sleep(2)
            print("[+] Please wait while the program is increasing your followers...")
        else:
            print("[!] Login Unsuccessful !")
            time.sleep(2)
            print("[+] Please check the username and/or the password !")
    except Exception as e:
        print("[!] Unexpected Error !")
        time.sleep(1)
        print(e)
    time.sleep(2)
    print("[+] To end the process enter Ctrl + C")
    c = 1
    FOLLOW=['173560420','1436859892','18428658','7719696','451573056','247944034','407964088','460563723','6860189','427553890','26669533','4213518589','12331195','28527810','12281817','208560325','145821237','305701719','217867189','20824486','25025320','787132','260375673','290023231','1269788896','29394004','11830955','6380930','2094200507','9777455']
    UNFOLLOW=['173560420','1436859892','18428658','7719696','451573056','247944034','407964088','460563723','6860189','427553890','26669533','4213518589','12331195','28527810','12281817','208560325','145821237','305701719','217867189','20824486','25025320','787132','260375673','290023231','1269788896','29394004','11830955','6380930','2094200507','9777455']
    while c > 0:
        for i in range(len(FOLLOW)):
            try:
                clnt.user_follow(FOLLOW[i])
            except Exception as key:
                print("[!] Unexpected Error !")
                time.sleep(1)
                print("[+] Exiting...")
                exit(0)
            print("[+] Following "+str(FOLLOW[i])+"...")
            time.sleep(2)
        for e in range(len(UNFOLLOW)):
            try:
                clnt.user_unfollow(UNFOLLOW[e])
            except Exception as key:
                print("[!] Unexpected Error !")
                time.sleep(1)
                print("[+] Exiting...")
                exit(0)
            print("[+] Unfollowing "+str(UNFOLLOW[e])+"...")
            time.sleep(2)
#End of the Program
