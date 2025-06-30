import time
import pyautogui
from pywinauto.application import Application
import os

def write_text(text, delay=1, enter=True):
    pyautogui.write(text, interval=0.05)
    if enter:
        pyautogui.press('enter')
    time.sleep(delay)

def press_key(key, delay=1):
    pyautogui.press(key)
    time.sleep(delay)

def launch_tally_start_menu():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('tally', interval=0.1)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(6)  # Wait for Word to open
    # Wait until the Tally window is opened
    app = None
    for _ in range(15):  # Try for up to ~30 seconds
        try:
            app = Application(backend="uia").connect(title_re=".*TallyPrime*", timeout=1)
            break
        except Exception:
            time.sleep(1)
    if app is None:
        raise RuntimeError("Tally window did not open in time.")
    else:
        print("Tally is opened")

    press_key("T")

def operate_tally():
    time.sleep(3)
    # Select company name
    press_key("F3")
    try:
        check = pyautogui.locateOnScreen('Picture2.png', confidence=0.8)
        if check:
            write_text("hi")
    except :
        print("List of companies list not found")
        return

    # Select Voucher
    try:
        if pyautogui.locateOnScreen('main-window.png', confidence=0.8):
            press_key("v")
            try:
                if pyautogui.locateOnScreen('3.png', confidence=0.8):
                    write_text("Cash")
            except:
                print("3 not found")
    except:
        print("2 not found")
        return
        
    try: 
        if pyautogui.locateOnScreen('4.png', confidence=0.8) and pyautogui.locateOnScreen('delivery_note.png', confidence=0.8):
            #Dispath deatils
            write_text("deelivery_note_1")
            write_text("1-Apr-25")
            write_text("deelivery_note_2")
            write_text("1-Apr-25")
            press_key("Esc")
            press_key("y")
    except:
        write_text("Cash")
        write_text("1000")

        write_text("Cash")
        write_text("1000")

        write_text("Cash")
        write_text("1000")

        press_key("enter")

        write_text("hello")
        write_text("y")

    

    pyautogui.press('F8')
    time.sleep(2)




# launch_tally_start_menu()
operate_tally()
