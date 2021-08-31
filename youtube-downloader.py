import getpass
from pytube import YouTube
from datetime import datetime

now = datetime.now()
formatted = now.strftime("%d %m %Y %H %M %S")

username = getpass.getuser()
save_path = f"C:/users/{username}/Desktop"
link = input("Youtube Link: ")

try:
    YouTube(link).streams.first().download()
    print('Success')
except:
    print('unhandled error')

