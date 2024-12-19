import random
import string
import pathlib 
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

main = f"""

  {Fore.LIGHTBLUE_EX}
                                                    ________________________
                                                    |Giftcard Psn Generator|
                                                    |    Made by 1AM       |
                                                    |         V1           |
                                                    ------------------------
                                        
                                        
                                        
                                        
                                        
                                        
                                        

"""
os.system("cls")
print(main)
print(f"[ 1 ] Gen PSN Giftcard")
print(f"[ 2 ] Amazon Gen Giftcard")
print(f"[ 3 ] Roblox Gen Giftcard ")
print(f"[ 4 ] Check Codes")
Generator = random.choice(string.ascii_letters + string.digits)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))+"-"+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))+"-"+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
Choice = input(f"Choice :")
base = f"{Generator}"
num_links = int(input("How much codes to gen ?"))
def generate_links(base):
    """Génère plusieurs liens avec des chaînes aléatoires et les retourne sous forme de liste."""
Codes = []
for _ in range(num_links):
 random_string = Generator
 code = f"{base}"
Codes.append(code)
api = f"https://Playstation.com/"

response = requests.get(api)
if response.status_code == 200:
   validecode = print(f"{Fore.GREEN}                 [ CHECKER ]{Fore.RESET} : Le code est valide !!")
if response.status_code == 400:
   invalidecode = print(f"{Fore.RED}                 [ CHECKER ]{Fore.RESET} : Le code est invalide")
if Choice == "1" :
 os.system("cls")
 print(main)
print(f"Succesfully Generated :" + code)
print(f"Want to verify the link ? (Y/N)")
ww = input(f"Choice :")
exit
if Choice == "2" :
  os.system("cls")
  print(main)
COde = str(input(f"Code :"))
def check(COde):
 for COde in Codes:
     if response.status_code == 200:
       print(f"{Fore.GREEN}                 [ CHECKER ]{Fore.RESET}{COde} : Le code est valide !!")
     if response.status_code == 400:
       print(f"{Fore.RED}                 [ CHECKER ]{Fore.RESET}{COde} : Le code est invalide !!")


if ww == "Y":
  check(COde)
  time.sleep(5)
exit

if ww == "N" :
  print(f"Tysm to use Multi Giftcard Gen !!! (Made by 1AM)")
  print(f"Closing Multi Giftcard Gen...")
time.sleep(5)
exit








if Choice == "3" :
 num_links1 = int(input("How much codes to gen ?"))
 for x in range(num_links):
  Generator1 = random.choice(string.ascii_letters + string.digits)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))+"-"+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
Choice1 = input(f"Choice :")
base1 = f"{Generator}"
def generate_links(base1):
    """Génère plusieurs liens avec des chaînes aléatoires et les retourne sous forme de liste."""
Codes = []
for _ in range(num_links1):
 random_string = Generator
 code = f"{base1}"
Codes.append(code)
api = f"https://Amazon.com/"

response = requests.get(api)
if response.status_code == 200:
   validecode = print(f"{Fore.GREEN}                 [ CHECKER ]{Fore.RESET} : Le code est valide !!")
if response.status_code == 400:
   invalidecode = print(f"{Fore.RED}                 [ CHECKER ]{Fore.RESET} : Le code est invalide")
if Choice1 == "1" :
 os.system("cls")
 print(main)
print(f"Succesfully Generated :" + code)
print(f"Want to verify the link ? (Y/N)")
ww = input(f"Choice :")
exit
if Choice == "2" :
  os.system("cls")
  print(main)
COde = str(input(f"Code :"))
def check(COde):
 for COde in Codes:
     if response.status_code == 200:
       print(f"{Fore.GREEN}                 [ CHECKER ]{Fore.RESET}{COde} : Le code est valide !!")
     if response.status_code == 400:
       print(f"{Fore.RED}                 [ CHECKER ]{Fore.RESET}{COde} : Le code est invalide !!")


if ww == "Y":
  check(COde)
  time.sleep(5)
exit

if ww == "N" :
  print(f"Tysm to use Multi Giftcard Gen !!! (Made by 1AM)")
  print(f"Closing Multi Giftcard Gen...")
time.sleep(5)
exit