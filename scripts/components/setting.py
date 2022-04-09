# =========== Step1 : INTILIZATION ===========
# Main variables settings
import os
import colorama
from colorama import Fore
import pyfiglet
os.system('CLS')
# DC: Batman, Superman, Cyborg, and Aquaman


print(Fore.LIGHTCYAN_EX +
      '*****************************************************************************')
print(Fore.LIGHTMAGENTA_EX + '\t\t' +
      pyfiglet.figlet_format('DC Universe Quiz',
                             justify="center"))
print(Fore.LIGHTCYAN_EX +
      '*****************************************************************************')
colorama.init(autoreset=True)
userName = input("\n\n\tEnter Your Name Please: ")

print(Fore.CYAN + '\t***********************************')
print("\t\tWelcom " + userName.upper())
print(Fore.CYAN + '\t***********************************')


userAnswers = []
userResult = []
playAgain = 1
