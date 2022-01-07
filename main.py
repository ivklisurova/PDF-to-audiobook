from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os


my_text = 'Примерен техт'
language = 'bg'

myobj = gTTS(text=my_text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
