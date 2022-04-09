from operator import truediv
import colorama
from colorama import Back, Fore
from components import setting
import pyfiglet

# ============= Validation Input Function :


def validation(value):
    colorama.init(autoreset=True)
    if(value == "playAgain"):
        pAgain = ""
        while (pAgain == ""):
            pAgain = input(Fore.RED +
                           "\tEnter (Q / q) to Quit: ")
            pAgain = pAgain.lower()
            if(pAgain != 'q'):
                setting.playAgain = 1
            else:
                print(Fore.LIGHTCYAN_EX +
                      '*****************************************************************************')
                print(Fore.LIGHTMAGENTA_EX + '\t\t' +
                      pyfiglet.figlet_format('Good By!!', justify="center"))
                print(Fore.LIGHTCYAN_EX +
                      '*****************************************************************************')
                exit()

    if(value == "inputAnswer"):
        setting.userChoice = ""
        while setting.userChoice == "":
            setting.userChoice = input(
                Fore.YELLOW+"\tChoose (Y / y) or (N / n): ")
            setting.userChoice = setting.userChoice.lower()
            if(setting.userChoice != 'y' and setting.userChoice != 'n'):
                setting.userChoice = ""
            else:
                setting.userAnswers.append(setting.userChoice.upper())
                return setting.userChoice.upper()
