import pyttsx3
import PyPDF2

book = open('JS.pdf', 'rb')  # opening a file

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages  # get the number of pages

print(pages)

speaker = pyttsx3.init()  # initialize the speaker
page = pdfReader.getPage(43)  # get the index of the page
text = page.extractText()  # convert the page contents to text
speaker.say(text)  # feed the text to the speaker
speaker.runAndWait()  # Run the speaker



