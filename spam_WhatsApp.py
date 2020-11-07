import time
import pyautogui as pya


class cordinate:
    emptyMessage = (173, 700)
    sendChat = (450, 700)
    pya.size()


def clicktochat():
    pya.click(cordinate.emptyMessage)


def typetochat():
    print("Hi")


def detailtext():
    print("Sup?")


def sendtochat():
    pya.click(cordinate.sendChat)
    print("I am bored!!!")


while True:
    clicktochat()
    typetochat()
    detailtext()
    sendtochat()
    time.sleep(0.5)

