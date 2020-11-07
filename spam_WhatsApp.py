# import time
# import pyautogui as pya
#
#
# class cordinate:
#     emptyMessage = (173, 700)
#     sendChat = (450, 700)
#     pya.size()
#
#
# def clicktochat():
#     pya.click(cordinate.emptyMessage)
#
#
# def typetochat():
#     print("Hi")
#
#
# def detailtext():
#     print("Sup?")
#
#
# def sendtochat():
#     pya.click(cordinate.sendChat)
#     print("I am bored!!!")
#
#
# while True:
#     clicktochat()
#     typetochat()
#     detailtext()
#     sendtochat()
#     time.sleep(0.5)

import time
import pyautogui as pya


class cordinate:
    emptyMessage = [90, 110]  # set the coordinates accordingly- to click on the bar
    pya.size()


def clicktochat():
    pya.click(cordinate.emptyMessage)


def typetochat():
    pya.write('Hi')  # type text
    pya.press('enter')  # hit enter
    pya.write("What's up?")
    pya.press('enter')
    pya.write("I am bored!!!")
    pya.press('enter')


numberOfTimes = 10
while numberOfTimes:
    clicktochat()
    typetochat()
    time.sleep(0.5)
