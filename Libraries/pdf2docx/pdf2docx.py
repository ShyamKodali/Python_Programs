from pdf2docx import Converter

pdf_file_name = 'demofile.pdf'
docx_file_name = 'demofile.docx'

cvr = Converter(pdf_file=pdf_file_name)
cvr.convert(docx_filename=docx_file_name)

cvr.close()