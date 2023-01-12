import time
import random
import pyautogui
import os
from subprocess import Popen
import subprocess

#vai até screen 9 onde está aberto OBS e começa a gravar
pyautogui.hotkey("winleft", "9")
pyautogui.moveTo(3640, 834)
time.sleep(1)
pyautogui.click()
time.sleep(3)

#
pyautogui.hotkey("winleft", "1")
time.sleep(2)
time.sleep(1)
pyautogui.hotkey("ctrlleft", "a")
pyautogui.press('q')
time.sleep(0.5)
pyautogui.press('0')
time.sleep(0.5)
pyautogui.hotkey("ctrlleft", "c")
pyautogui.hotkey("ctrlleft", "l")
with open("nmap.txt") as file:
    for line in file:
        print("\n")
        pyautogui.press("enter")
        for char in line:
            pyautogui.press(char)
            Popen([f"cvlc --play-and-exit /tmp/key/{random.randint(1,9)}.mp3"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
            time.sleep(random.uniform(0.001,0.03))
pyautogui.press("enter")
with open ("examples.txt") as ex1, open("examples2.txt") as ex2:
    for x, y in zip(ex1, ex2):
        for char in x:
            pyautogui.press(char)
            Popen([f"cvlc --play-and-exit /tmp/key/{random.randint(1, 9)}.mp3"], shell=True, stdin=None, stdout=None,
                  stderr=None, close_fds=True)
            time.sleep(random.uniform(0.001, 0.03))
        Popen([f"screenkey"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "a")
        pyautogui.press('q')
        time.sleep(0.5)
        pyautogui.press('1')
        time.sleep(0.5)
        Popen(["ps -ef | grep screenkey | grep -v grep | awk '{print $2}'| xargs kill"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        for char in y:
            pyautogui.press(char)

            Popen([f"cvlc --play-and-exit /tmp/key/{random.randint(1, 9)}.mp3"], shell=True, stdin=None, stdout=None,
                  stderr=None, close_fds=True)
            time.sleep(random.uniform(0.001, 0.03))
        p = Popen([f"{y}"], shell=True, stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        # This makes the wait possible
        p_status = p.wait()

        Popen([f"screenkey"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "a")
        # pyautogui.keyDown('ctrlleft')
        # pyautogui.press('a')
        # pyautogui.keyUp('ctrlleft')
        pyautogui.press('q')
        time.sleep(0.5)
        pyautogui.press('0')
        time.sleep(0.5)
        Popen(["ps -ef | grep screenkey | grep -v grep | awk '{print $2}'| xargs kill"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
pyautogui.hotkey("winleft", "9")
pyautogui.moveTo(3640, 834)
time.sleep(1)
pyautogui.click()
time.sleep(3)

