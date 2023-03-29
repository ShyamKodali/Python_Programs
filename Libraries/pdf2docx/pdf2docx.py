import pdf2docx 
from pdf2docx import converter

pdf_file_name = 'demofile.pdf'
docx_file_name = 'demofile.docx'

cvr = converter(pdf_file=pdf_file_name)
cvr.convert(docx_filename=docx_file_name)

cvr.close()