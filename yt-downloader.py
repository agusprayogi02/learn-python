from tkinter import *

from pytube import YouTube

root = Tk()
root.geometry("700x300")
root.resizable(0, 0)
root.title("Youtube Video Downloader")
Label(root, text="Copy the link of the video you want to download from YouTube",
      font="arial 15 bold").pack()
# enter link
link = StringVar()

Entry(root, textvariable=link, width=80).pack(after=Label(root, text="Paste Link Here : ",
                                                          font="arial 15 bold").pack())


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="Downloaded", font="arial 15 bold").pack()


Button(root, text="Download", font="arial 15 bold", bg="white",
       padx=2, command=Downloader).pack()
root.mainloop()
