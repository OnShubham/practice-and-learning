# pip install pyPDF2

import PyPDF2

# Open the file
with open('./file/012 dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfWriter()
    writer.addPage(page)
    with open('./file/012 dummy.pdf', 'wb') as new_file:
        writer.write(new_file)

    print(file)