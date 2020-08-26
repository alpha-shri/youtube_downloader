"""
Date : 23rd August 2020
Objective : Creating YouTube Video downloader with tKinter
"""

from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


file_size = 0  

def startDownload():

    global file_size
    try:        
        url = urlField.get()
        print(url)
        # Changing Button Text
        downloadButton.config(text = "Please Wait....")
        downloadButton.config(state = DISABLED)
        path_to_save_video = askdirectory()

        if path_to_save_video is None:
            return

        # Creating the object of YouTube class
        objectYouTube = YouTube(url)    #We can fetch videos from the Object passing URL as parameter

        stream = objectYouTube.streams.all()
        
        first_stream = objectYouTube.streams.first()        # TO fetch the first stream of video
        
        first_stream.download(path_to_save_video)           #   You can also specify a destination path where to DOWNLOAD:

        print("Download Successful")
        downloadButton.config(state = NORMAL)

        downloadButton.config(text =  "Start Download")
        showinfo("Download Successful", "Download Finished")
        urlField.delete(0, END)

    except Exception as e:
        print("Error: ", e)

"""
GUI Building for YouTube Downloader 
"""

main = Tk()

# Setting the Title
main.title("My YouTube Downloader")

# Setting the ICON
main.iconbitmap('youtube_icon.ico')

# Setting the height and width of the Wizard
main.geometry("500x600")

# Heading ICON
file = PhotoImage(file = 'youtube_icon.png')
headingIcon = Label(main, image = file)
headingIcon.pack(side = TOP)

# URL Text
urlField = Entry(main, font=("Consolas", 18), justify=CENTER)
urlField.pack(side = TOP, fill =X, padx=10) 

# Download Button
downloadButton = Button(main, text = "Start Download", font=("Consolas", 18), relief='ridge', command = startDownload())
downloadButton.pack(side = TOP, pady=10)

main.mainloop()