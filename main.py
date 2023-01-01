from colorama import Fore, Style
from bs4 import BeautifulSoup
import requests
import os

print("Have you been hacked/pwned ? Let's check !")
user_mail = input("Enter your Mail Address : ")
url = "https://haveibeenpwned.com/unifiedsearch/" + user_mail
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
if response.ok:
    print(Fore.RED + "Oh no ! Your account have been hacked !")
    hack_infos = soup.find("pre")
    stock_info = input("Do you want to have more information about the hacking of your e-mail address ? (Yes/No) : ")
    if stock_info == str("Yes"):
        file = open("hack_informations.txt", "w+")
        file.write("There is the informations of your hacking : \n" + hack_infos.text)
else:
    print(Fore.GREEN + "Yoohoooo ! Your account has not been hacked !")