import tkinter as tk
import pygame

# Initialize audio
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Sound definitions
sounds = {
    "Donate": "donate.mp3",
    "Dismantle": "dismantle.mp3",
    "Put Away": "putaway.mp3",
    "Trash": "trash.mp3",
    "I Don't Know": "idontknow.mp3",
    "Go Back": "goback.mp3",
    "Sell": "x.mp3",
    "Recycle": "x.mp3",
    "Maybe": "x.mp3",
    "Later": "x.mp3",
}

# Load sounds
for key in sounds:
    sounds[key] = pygame.mixer.Sound(sounds[key])

# Play sound
def play_sound(name):
    sounds[name].play()

# Window setup
root = tk.Tk()
root.title("Sound Board")
root.geometry("1200x500")
root.configure(bg="black")

# Keep on top
root.attributes("-topmost", True)

# Button layout
button_names = list(sounds.keys())

for index, name in enumerate(button_names):
    row = index // 5
    col = index % 5

    btn = tk.Button(
        root,
        text=name,
        command=lambda n=name: play_sound(n),
        font=("Arial", 20, "bold"),
        width=14,
        height=4,
        bg="#222",
        fg="white",
        activebackground="#444",
        activeforeground="white",
        relief="raised",
        bd=4
    )

    btn.grid(
        row=row,
        column=col,
        padx=10,
        pady=15
    )

# Center grid nicely
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

for i in range(2):
    root.grid_rowconfigure(i, weight=1)

# Run app
root.mainloop()