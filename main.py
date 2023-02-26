import pyttsx3
import PyPDF2
from tkinter.filedialog import *

pdf = askopenfilename()
reader = PyPDF2.PdfReader(pdf)
page_number = len(reader.pages)

player = pyttsx3.init()

for num in range(0, page_number):
    page = reader.pages[num]
    text = page.extract_text()
    player.say(text)
    player.runAndWait()
