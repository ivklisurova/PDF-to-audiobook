from tkinter import Tk
from tkinter.filedialog import askopenfilename
from os.path import splitext
import PyPDF2
from gtts import gTTS


Tk().withdraw()
file_location = askopenfilename()

pdf_file = open(file_location, mode='rb')
pdf_doc = PyPDF2.PdfFileReader(pdf_file)
len_document = pdf_doc.numPages

text_to_read = ''

for page in range(len_document):
    current_page = pdf_doc.getPage(page)
    a = current_page.extractText()
    text_to_read += a


final_file = gTTS(text=text_to_read, lang='en', slow=False)

out_name = splitext(file_location)[0] + '.mp3'
final_file.save(out_name)

