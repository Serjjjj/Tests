import time
from plyer import notification

count = 0
notification.notify(
    message="Pomodoro timer запущен, начинайте работу!")
if __name__ == "__main__":
    while True:
        time.sleep(20)
        count += 1
        notification.notify(
            title="Хорошая работа!",
            message="Возьмите перерыв на 10 минут! Вы закончили " +
                    str(count) + " круг(-ов)",
        )
        time.sleep(10)
        notification.notify(
            title="Возвращайтесь к работе!",
            message="Продолжайте работу...",
        )