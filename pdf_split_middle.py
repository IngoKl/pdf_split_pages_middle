import copy
import decimal
from PyPDF2 import PdfWriter,PdfReader

output = PdfWriter()

def pdf_split_middle(pdf_path, pdf_output_path='split_middle.pdf', skip_pages=[], shift_middle_percentage=0):
	pdf = PdfReader(open(pdf_path, 'rb'))

	for page_nr in range(len(pdf.pages)):

		page = pdf.pages[page_nr]

		if page_nr not in skip_pages:
			lr = page.cropbox.lower_right
			ur = page.cropbox.upper_right

			if shift_middle_percentage > 49:
				shift_middle_percentage = 49

			if shift_middle_percentage < -49:
				shift_middle_percentage = -49

			# ur[0] = width of document
			shift_middle = ur[0] / 100 * decimal.Decimal(shift_middle_percentage) * -1

			# Left Page
			page_left = copy.copy(page)

			page_left.mediabox.lower_right = (lr[0]/2 + (shift_middle), lr[1])
			page_left.mediabox.upper_right = (ur[0]/2 + (shift_middle), ur[1])

			# Right Page
			page_right = copy.copy(page)

			page_right.mediabox.lower_left = (lr[0]/2 + (shift_middle), lr[1])
			page_right.mediabox.upper_left = (ur[0]/2 + (shift_middle), ur[1])

			output.add_page(page_left)
			output.add_page(page_right)
		else:
			output.add_page(page)

	with open(pdf_output_path, 'wb') as out_f:
		output.write(out_f)
