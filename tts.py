from gtts import gTTS


print("Enter text in English")
text_to_speak = input()
print("Enter name of file to be saved")
filename = input()

def convert():
    language = "en"
    tts = gTTS(text=text_to_speak, lang=language, slow=False)

    tts.save(filename + ".mp3")

convert()