import unittest
import time
from plyer import notification
import math


class MyTestCase(unittest.TestCase):

    def test_something(self):
        count = 0
        for n in range(5):
            time.sleep(1)
            count += 1
            notification.notify(
                title="Good work!",
                message="Take a 10 minute break! You have completed " + str(count) + " pomodoros so far",
            )
            time.sleep(1)
            notification.notify(
                title="Back to work!",
                message="Try doing another pomodoro...",
            )
            time.sleep(1)
        self.assertEqual(count,5)
    def test_timecode(self):
        count = 0
        tic = time.perf_counter()
        for n in range(5):
            time.sleep(1)
            count += 1
            notification.notify(
                title="Good work!",
                message="Take a 10 minute break! You have completed " + str(count) + " pomodoros so far",
            )
            time.sleep(1)
            notification.notify(
                title="Back to work!",
                message="Try doing another pomodoro...",
            )
            time.sleep(1)
        toc = time.perf_counter()
        n= toc-tic
        timer= math.trunc(n)
        self.assertEqual(timer,15)


if __name__ == '__main__':
    unittest.main()
