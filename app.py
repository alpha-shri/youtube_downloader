"""
Date : 23rd August 2020
Objective : Creating YouTube Video downloader
"""

from pytube import *

# Add the YouTube URL
url = "https://www.youtube.com/watch?v=reyfIve119Q&list=PL8uhW8cclMiODNMBhI6MNzw5zTudkQz4G&index=2&t=0s"       

# Saving path
path_to_save_video = "D:\\Seasons"

# Creating the object of YouTube class

objectYouTube = YouTube(url)    #We can fetch videos from the Object passing URL as parameter

stream = objectYouTube.streams.all()

#to fetch the title of the video
# title = objectYouTube.title
# print(title)

# TO fetch the first stream of video
first_stream = objectYouTube.streams.first()
# title = objectYouTube.title()

# print(first_stream)

#   You can also specify a destination path where to DOWNLOAD:
first_stream.download(path_to_save_video)

print("Download Successful")

# Fetch the audio file
# audio_file = objectYouTube.streams.filter(only_audio=True).all()
# print(audio_file)

# Subtitle/Caption Tracks
# subtitles = objectYouTube.captions.all()

