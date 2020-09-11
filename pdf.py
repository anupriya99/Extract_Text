from PyPDF2 import PdfFileReader

#opening the pdfin read mode
file = open('C:/Users/dell/Downloads/sample.pdf','rb')

# installing the object
reader= PdfFileReader(file)

print("printing",(reader.getDocumentInfo()))

print()

print("No. of pages",reader.getNumPages())

print("File created by ",reader.getDocumentInfo().creator)

pages = reader.getNumPages()
for i in range(0,pages):
    print("page num",i+1)
    pageObj=reader.getPage(i)
    print(pageObj.extractText())

file.close()