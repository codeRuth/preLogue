import glob
import win32com.client
from subprocess import check_output
import sys
import os
from comtypes import client


class convertPPT(object):
    def __init__(self, files):
        self.files = glob.glob(os.path.abspath("../slides/%s" % files))
        self.powerpoint = win32com.client.Dispatch("Powerpoint.Application")

    def convertPDF(self, files, formatType=32):
        for filename in files:
            newName = os.path.splitext(filename)[0] + ".pdf"
            deck = self.powerpoint.Presentations.Open(filename, WithWindow=False)
            deck.SaveAs(newName, formatType)
            deck.Close()
        self.powerpoint.Quit()

    def convertHTML(self):
        check_output("pdf2htmlEX --embed cfijo --fit-width 1024 --dest-dir ../slides/html "
                     + os.path.splitext(self.files[0])[0] + ".pdf")

    def convertImage(self, files, formatType=18):
        for filename in files:
            newName = os.path.splitext(filename)[0] + ".png"
            deck = self.powerpoint.Presentations.Open(filename, WithWindow=False)
            deck.SaveAs(newName, formatType)
            deck.Close()
        self.powerpoint.Quit()

    def convertPNG(self):
        try:
            self.convertPDF(self.files)
            self.convertHTML()
        except Exception:
            return False

    def convertFile(self):
        try:
            self.convertPDF(self.files)
            self.convertHTML()
        except Exception:
            return False
        return True
