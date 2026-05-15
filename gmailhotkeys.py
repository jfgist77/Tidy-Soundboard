import tkinter as tk
import keyboard
import time


# =========================
# Gmail Hotkey Functions
# =========================

def press_key(key):
    time.sleep(0.05)
    keyboard.press_and_release(key)


def select_message():
    press_key("x")


def older_message():
    press_key("j")


def newer_message():
    press_key("k")


def delete_message():
    press_key("#")


def archive_message():
    press_key("e")


def report_spam():
    press_key("!")


# =========================
# GUI
# =========================

root = tk.Tk()
root.title("Gmail Pad")
root.geometry("900x120")
root.attributes("-topmost", True)

button_font = ("Arial", 14, "bold")

frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)


buttons = [
    ("Select", select_message),
    ("Older", older_message),
    ("Newer", newer_message),
    ("Delete", delete_message),
    ("Archive", archive_message),
    ("Spam", report_spam),
]

for text, command in buttons:
    btn = tk.Button(
        frame,
        text=text,
        command=command,
        font=button_font,
        width=12,
        height=3
    )
    btn.pack(side="left", padx=5)


root.mainloop()