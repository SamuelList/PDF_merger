import PyPDF2


watermark = 'wtr.pdf'
input_pdf = 'merged-pdf.pdf'
output_pdf = 'stamped.pdf'

with open(input_pdf, 'rb') as file, open(watermark, 'rb') as wtr:
	input_file = PyPDF2.PdfReader(file)
	water_file = PyPDF2.PdfReader(wtr)
	water_page = water_file.pages[0]
	# print(water_page)

	outer = PyPDF2.PdfWriter()
	
	for i in range(input_file._get_num_pages()):
		page = input_file.pages[i]
		page.merge_page(water_page)
		outer.add_page(page)
		
	with open(output_pdf, 'wb') as watered:
		outer.write(watered)
