from PyPDF2 import PdfReader

reader = PdfReader("storage/avvio-immissioni.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print('>>> PRIMA PAGINA')
print(text)
print('')
print('>>> NUMERO PAGINE')
print(number_of_pages)
