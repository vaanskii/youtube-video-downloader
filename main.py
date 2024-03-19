import tkinter
import customtkinter
from pytube import YouTube


# System settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title('Youtube video downloader')

# Run app
app.mainloop()