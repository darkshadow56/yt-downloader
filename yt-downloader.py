from pytube import YouTube
print("Simple youtube downloader")
print("Download quality will be set to maximum available automatically! ")
# Creating link variable to store video URL
link = input("Enter your URL for video here: ")
# Storing youtube link in video variable
video = YouTube(link)
# Using stream function to download maximum quality available
stream = video.streams.get_highest_resolution()
# Downloading to the folder you're in
stream.download()
print("Video has been download to current directory!")