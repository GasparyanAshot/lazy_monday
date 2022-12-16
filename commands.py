import os
import keyboard
import time


isBrowserOpened=False

def OpenCmd():
    os.system("start cmd")
    time.sleep(1)
def CloseCmd():
    Input("exit")
    Enter()

def OpenBrowser(browser,incognito):
    global isBrowserOpened
    isBrowserOpened=True
    OpenCmd()
    text="start "+browser
    if incognito==True:
        text+=" /incognito"
    Input(text)
    Enter()
    CloseCmd();
    time.sleep(2)

def OpenWebsite(url):
    if isBrowserOpened:
        Input(url)
        Enter()
        time.sleep(2)
    else: print("Open browser first")




def Input(text):
    keyboard.write(text)
    time.sleep(0.1)

def Tab(count):
    for i in range(count):
        keyboard.press_and_release("tab")

def Enter():
    keyboard.press_and_release("enter")