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

# adding ui elements
title = customtkinter.CTkLabel(app, text='Insert a youtube link')
title.pack(padx=10, pady=10)

# link input
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

# Run app
app.mainloop()