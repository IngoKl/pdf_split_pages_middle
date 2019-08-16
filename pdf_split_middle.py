import copy
import decimal
from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger

output = PdfFileWriter()

def pdf_split_middle(pdf_path, pdf_output_path='split_middle.pdf', skip_pages=[], shift_middle_percentage=0):
	pdf = PdfFileReader(open(pdf_path, 'rb'))

	for page_nr in range(pdf.getNumPages()):

		page = pdf.getPage(page_nr)

		if page_nr not in skip_pages:
			lr = page.cropBox.getLowerRight()
			ur = page.cropBox.getUpperRight()

			if shift_middle_percentage > 49:
				shift_middle_percentage = 49

			if shift_middle_percentage < -49:
				shift_middle_percentage = -49

			# ur[0] = width of document
			shift_middle = ur[0] / 100 * decimal.Decimal(shift_middle_percentage) * -1

			# Left Page
			page_left = copy.copy(page)

			page_left.mediaBox.lowerRight = (lr[0]/2 + (shift_middle), lr[1])
			page_left.mediaBox.upperRight = (ur[0]/2 + (shift_middle), ur[1])

			# Right Page
			page_right = copy.copy(page)

			page_right.mediaBox.lowerLeft = (lr[0]/2 + (shift_middle), lr[1])
			page_right.mediaBox.upperLeft = (ur[0]/2 + (shift_middle), ur[1])

			output.addPage(page_left)
			output.addPage(page_right)
		else:
			output.addPage(page)

	with open(pdf_output_path, 'wb') as out_f:
		output.write(out_f)
