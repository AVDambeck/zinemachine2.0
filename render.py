from util import html2pdf

file = "http://thelemapedia.org"
html2pdf.initialize()
html2pdf.convert(file, "print.pdf")
input()
html2pdf.deinitialize()
exit()
