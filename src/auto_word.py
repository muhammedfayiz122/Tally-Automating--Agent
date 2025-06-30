import pyautogui
import time
from pywinauto.application import Application
import os

def launch_word_start_menu():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Word', interval=0.1)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(6)  # Wait for Word to load

def create_and_save_cv():
    launch_word_start_menu()

    app = Application(backend="uia").connect(title_re=".*Word")
    word_win = app.window(title_re=".*Word")
    word_win.wait('visible', timeout=15)
    word_win.set_focus()

    try:
        word_win.type_keys("^n")
        word_win['Blank document'].click_input()
        time.sleep(2)
    except:
        pass

    doc = word_win.child_window(title="Editing area", control_type="Edit")
    doc.wait('ready', timeout=10)

    cv_text = (
        "MUHAMMED FAYIZ\n"
        "Aspiring Machine Learning Engineer\n\n"
        "Email: fayiz@example.com\n"
        "Phone: +91-9876543210\n\n"
        "Education:\n"
        "- B.Tech in Computer Science (2025) - XYZ College\n\n"
        "Skills:\n"
        "Python, Machine Learning, IoT, Multi-Agent Systems\n\n"
        "Projects:\n"
        "- Just Walk Out Store: An AI-powered cashierless retail system\n"
        "- Smart Home Robot: Voice-activated robotic arm for home chores\n"
    )
    doc.type_keys(cv_text, with_spaces=True, pause=0.05)

    word_win.type_keys("^s")
    time.sleep(2)

    save_dialog = app.window(title_re=".*Save As.*")
    save_dialog.wait("visible", timeout=10)

    filename_box = save_dialog.child_window(auto_id="1001", control_type="Edit")
    filename_box.type_keys(os.path.join(os.environ["USERPROFILE"], "Documents\\Sample_CV.docx"))

    time.sleep(1)
    save_dialog.child_window(title="Save", control_type="Button").click_input()
    time.sleep(2)

    print("✅ CV created and saved successfully.")

create_and_save_cv()
