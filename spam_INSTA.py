import pyautogui, time
time.sleep(10)
f = open("Insta_spamfile.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    