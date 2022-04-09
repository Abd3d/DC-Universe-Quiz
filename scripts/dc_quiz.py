import colorama
from colorama import Fore
from components import setting, validation,  db
from PIL import Image
from emoji import emojize
# Chose Chaecter


def newQuiz():
    q = db.mQuestions.items()
    #Rertiving Data #
    currentQuestion = 0
    setting.userAnswers.clear()
    setting.userResult.clear()
    for value in q:
        print(Fore.LIGHTCYAN_EX + "\n\t" +
              str(value[0]) + ": " + str(value[1]))
        answer = validation.validation("inputAnswer")
        if (answer.lower() == "y"):
            for k in db.mVar[currentQuestion]:
                if (k == "b"):
                    db.mB += 1
                elif (k == "s"):
                    db.mS += 1
                elif (k == "c"):
                    db.mC += 1
                else:
                    db.mA += 1
        else:
            rest = set(['b', 's', 'c', 'a']) - set(db.mVar[currentQuestion])
            for k in rest:
                if (k == "b"):
                    db.mB += 1
                elif (k == "s"):
                    db.mS += 1
                elif (k == "c"):
                    db.mC += 1
                else:
                    db.mA += 1
        currentQuestion += 1

    # Display the result #
    print(Fore.GREEN + "\n\tThank You: " + emojize(':thumbs_up:'))

    imgPath = ""
    result = max(db.mA, db.mB, db.mC, db.mS)
    if(result == db.mA):
        im = Image.open("aquaman.png")
    elif(result == db.mB):
        im = Image.open("batman.jpg")
    elif(result == db.mC):
        im = Image.open("Cyborg.jpg")
    else:
        im = Image.open("superman.jpg")
    im.show()
    # Play Again #
    pAgain = validation.validation("playAgain")


while (setting.playAgain == 1):
    newQuiz()
