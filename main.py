"""
Date : 23rd August 2020
Objective : Creating YouTube Video downloader
"""

from pytube import *


file_size = 0
url = "https://www.youtube.com/watch?v=reyfIve119Q&list=PL8uhW8cclMiODNMBhI6MNzw5zTudkQz4G&index=2&t=0s"       

def startDownload(url):

    global file_size
    try:        
        
        path_to_save_video = "D:\\Seasons"  # Saving path

        # Creating the object of YouTube class
        objectYouTube = YouTube(url)    #We can fetch videos from the Object passing URL as parameter

        stream = objectYouTube.streams.all()
        
        first_stream = objectYouTube.streams.first()        # TO fetch the first stream of video
        
        first_stream.download(path_to_save_video)           #   You can also specify a destination path where to DOWNLOAD:

        print("Download Successful")

    except Exception as e:
        print("Error: ", e)