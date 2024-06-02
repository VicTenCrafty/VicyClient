import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import minecraft_launcher_lib
import subprocess
import tempfile
import os

def play_minecraft():
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    options = minecraft_launcher_lib.utils.generate_test_options()
    account_info = options
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.20.1", minecraft_directory, options)

    with tempfile.NamedTemporaryFile(suffix=".bat", delete=False) as temp_script:
        temp_script.write(' '.join(minecraft_command).encode("utf-8"))
        temp_script_path = temp_script.name

    try:
        subprocess.run(temp_script_path, shell=True)
    finally:
        os.unlink(temp_script_path)

def create_gui():
    root = tk.Tk()
    root.title("Minecraft Launcher")
    root.geometry("1220x700")

    # Load the background image
    background_image = Image.open("background_image.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a transparent image to use as a background for the title label
    transparent_image = Image.new('RGBA', (0, 0), (0, 0, 0, 0))
    transparent_photo = ImageTk.PhotoImage(transparent_image)

    # Create a label to display the transparent image as the background of the title
    title_background_label = tk.Label(root, image=transparent_photo)
    title_background_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Create the title label with the text "Minecraft Launcher"
    title_label = tk.Label(root, text="Minecraft Launcher", font=("Helvetica", 36, "bold"), fg="white", bg="black")
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Custom font
    custom_font = font.Font(family="Helvetica", size=12)

    # Create the "Play!" button
    play_button = tk.Button(root, text="Play!", command=play_minecraft, font=("Helvetica", 14, "bold"), foreground="white", background="#4CAF50", padx=20, pady=10, borderwidth=0, relief=tk.FLAT)
    play_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Start the GUI main loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
