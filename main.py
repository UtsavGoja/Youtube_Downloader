import tkinter as tk
from tkinter import * 
from tkinter import ttk, messagebox
from pytube import YouTube

root= tk.Tk()
root.resizable(0, 0)

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised' )
canvas1.pack()
canvas1.configure(background="lightblue")

label1 = tk.Label(root, text='Youtube Video Downloader')
label1.configure(background="lightblue")
label1.config(font=('helvetica', 18,), fg="navyblue")
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter url of the video')
label2.configure(background="lightblue")
label2.config(font=('helvetica', 15), fg="navyblue")
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

Label(text="Utsav_Goja", fg="navyblue",bg="lightblue", font=("calbri", 13)).place(x=300, y=270)

def download():
    ytd_url = entry1.get()
    try:
        obj = YouTube(ytd_url)
        filter = obj.streams.filter(progressive=True,file_extension='mp4')
        filter.get_highest_resolution().download(filename='myvideo.mp4')
        label3 = tk.Label(root, text= "Downloading Started",font=('helvetica', 10))
        canvas1.create_window(200, 210, window=label3)
    except Exception as e:
        label4 = tk.Label(root, text= "Downloading Failed",font=('helvetica', 10))
        canvas1.create_window(200, 210, window=label4)

    
button1 = tk.Button(text='Download', command=download, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()