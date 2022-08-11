"""
Stampa su schermo il testo contenuto nella prima pagina
del PDF dato.

Opzionalmente, specifica come secondo argomento la pagina
specifica da stampare.
"""

from sys import argv
from PyPDF2 import PdfReader
from src.libs.general import secondOrNone, thirdOrNone
from src.libs.parse import parseInt

# Parse
pdf = secondOrNone(argv)
n = parseInt(thirdOrNone(argv), 1)

# Extract
reader = PdfReader(pdf)
number_of_pages = len(reader.pages)
if n > number_of_pages:
    raise Exception(f"Il PDF ha {number_of_pages} pagine, non arriva a pagina {n}")
page = reader.pages[n - 1]
text = page.extract_text()

# Print
print(f">>> PAGINA {n}")
print(text)
print("")
print(">>> NUMERO PAGINE")
print(number_of_pages)
