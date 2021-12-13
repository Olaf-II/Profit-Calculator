import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
import os
import sys
init()

clearConsole = lambda: os.system('cls') if os.name in ('nt', 'dos') else 'clear'
clearConsole
URL = "https://bitinfocharts.com/comparison/ethereum-mining_profitability.html#3m"

def getHashrate(prettifiedResults):

    permh = float(str(prettifiedResults)[97:-39])

    usersMH = input("What is your current mh/s rate?\n")
    try:
        permh = profitRate = float(usersMH)*permh
    except:
        print("Invalid number. Please only use numbers and \".\"")
        input("Press enter to continue...")
        os.system('python ProfitCalculator.py')

    profitRate = str(profitRate)[:4]
    clearConsole
    print("Revenue per day: $" + profitRate)
    print("Revenue per hour: $" + str(float(profitRate) / 24)[:4])

def updateEarnings():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="abtb")
    prettifiedResults = results.prettify
    return prettifiedResults

prettifiedResults = updateEarnings()
option = input("What would you like to do?\n\n1 - Get Revenue Rate\n2 - Refresh Rates\n3 - Close\n\nSelect > ")
if option == "1":
    getHashrate(prettifiedResults)
elif option == "2":
    prettifiedResults = updateEarnings()
elif option == "3":
    sys.exit()
else:
    print("Stop trying to make my life hard... please")
    input("Press enter to continue...")
    os.system('python ProfitCalculator.py')

os.system('python ProfitCalculator.py')