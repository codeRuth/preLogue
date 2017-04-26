import sys
import os
import glob
import win32com.client

class convertPDF(object):
    def __init__(self, files):
        self.files = glob.glob("slides/"+files)
        self.isVisible = False
        self.powerpoint = win32com.client.Dispatch("Powerpoint.Application")

    def convert(self, files, formatType=32):
        print os.path.splittext(files)
        for filename in files:
            newname = os.path.splitext(filename)[0] + ".pdf"
            deck = self.powerpoint.Presentations.Open(filename)
            deck.SaveAs(newname, formatType)
            deck.Close()
        self.powerpoint.Quit()

    def convertFile(self):
        self.convert(self.files)


if __name__ == '__main__':
    c = convertPDF("abc.pptx")
    c.convertFile()
