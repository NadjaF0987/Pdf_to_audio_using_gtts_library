from PyPDF2 import PdfFileReader
from gtts import gTTS

# pdf file to convert
pdf_file_path = "test.pdf"

#---------- Convert the PDF text to a string ----------
reader = PdfFileReader(pdf_file_path, strict=False)
number_of_pages = reader.numPages
# Loop through all pages and gather all text in a string
text_list = []
for i in range(number_of_pages):
    try:
        page = reader.getPage(i)
        text_list.append(page.extractText())
    except:
        pass
new_list = [s.replace("\n", "") and s.split() for s in text_list]
text_string = ""
for list_ in new_list:
    for item in list_:
        text_string += f" {item}"
#print(text_string)

#---------- Convert a string to audio via Google Tranlates text-to-speech API ----------
# Language options: run this in the terminal: gtts-cli --all
language = 'da'
audio = gTTS(text=text_string, lang=language, slow=False)
audio.save("audio.mp3")
