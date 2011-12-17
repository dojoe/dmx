from pyPdf import PdfFileWriter, PdfFileReader
from Tkinter import Tk
import tkFileDialog

master = Tk()
master.withdraw()

page = None

inputFiles = master.tk.splitlist(tkFileDialog.askopenfilenames())

print inputFiles

for fname in inputFiles:
    file1 = file(fname, "rb")
    input1 = PdfFileReader(file1)
    if not page:
        page = input1.getPage(0)
    else:
        page.mergePage(input1.getPage(0))

output = PdfFileWriter()
output.addPage(page)
outputStream = file(tkFileDialog.asksaveasfilename(), "wb")
output.write(outputStream)
outputStream.close()
