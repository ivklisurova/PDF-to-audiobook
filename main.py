from tkinter import Tk
from tkinter.filedialog import askopenfilename

import PyPDF2
from gtts import gTTS
import os

Tk().withdraw()
file_location = askopenfilename()

pdf_file = open(file_location, mode='rb')
pdf_doc = PyPDF2.PdfFileReader(pdf_file)
len_document = pdf_doc.numPages
print(pdf_doc.numPages)

text_to_read = ''

for page in range(len_document):
    current_page = pdf_doc.getPage(page)
    a = current_page.extractText()
    text_to_read += a


myobj = gTTS(text=text_to_read, lang='en', slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
# os.system("mpg321 welcome.mp3")
