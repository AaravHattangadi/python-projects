import pyshorteners
import pyperclip
print('Enter url to be shortened: \n')
urltbs = input()
s = pyshorteners.Shortener(api_key='15cdccb2a76b842f6b69eaf0927ab37341bd3')
url = s.cuttly.short(urltbs)
print(url)
pyperclip.copy(url)
print('URL has been automatically copied to the clipboard')

