import pytube 

# Selecting Location to store the Downloaded video 

download_loc = '/Users/kodalisimac/Downloads/YT videos Downloading through PY'
my_url = input('Enter url: ')

# Creating an instance of YouTube video

video_instance = pytube.YouTube(my_url) 

# Selecting High Resolution video quality instance

video_quality = video_instance.streams.get_highest_resolution()

# Downloading 

video_quality.download(download_loc)