import time
from plyer import notification
from colorama import Fore

class Errors():
    def notnumb(self):
        print(Fore.RED + 'ОШИБКА:Введите числа!!')
        pass

count = 0
print("The pomodoro timer has started, start working!")

if __name__ == "__main__":
    try:
     w = input("Сколько собираетесь работать?")
     z = input("Сколько хотите отдыхать?")
     h = input("Сколько кругов помодоро хотите пройти?")
     ww = int(w)
     zz = int(z)
     hh = int(h)
    except:
        Errors.notnumb(self=0)
    for i in range(hh):
            time.sleep(ww)
            count += 1
            notification.notify(
                title="Good work!",
                message="Take a "+str(zz)+" seconds break! You have completed " + str(count) + " pomodoros so far",
            )
            time.sleep(zz)
            notification.notify(
                title="Back to work!",
                message="Try doing another pomodoro...", #Это прошло все!!
            )

