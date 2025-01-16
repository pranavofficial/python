import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

player = pyttsx3.init()

rate = player.getProperty('rate')
player.setProperty('rate', rate - 50)
volume = player.getProperty('volume')
player.setProperty('volume', volume + 0.25)

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    text = text.lower()
    player.say(text)

player.runAndWait()