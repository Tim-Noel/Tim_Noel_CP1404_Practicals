"""
CP1404 Prac
Quick Pick Program
"""

import random

NUMBER_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    number_of_quick_picks = int(input("How many quick picks?: "))
    while number_of_quick_picks < 0:
        print("Please insert a valid response")
        number_of_quick_picks = int(input("How many quick picks?: "))

    for i in range(number_of_quick_picks):
        quick_pick = 1
        for x in range(NUMBER_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number - random.randint(MIN, MAX)
            quick_pick.apped(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
