from PyPDF2 import PdfWriter
import sys
import os

args = sys.argv[1:]
pdfs = [pdf for pdf in args if pdf.endswith('.pdf') and os.path.exists(pdf)]

# instantiates merger
merger = PdfWriter()

# appends all pdfs into merger
for pdf in pdfs:
    merger.append(pdf)
    
merger.write("merged-pdf.pdf")
print("Success")
merger.close()
