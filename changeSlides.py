import win32com.client
from getAction import getTopAction


class Slide(object):
    def __init__(self):
        self.getA = getTopAction()
        try:
            self.app = win32com.client.Dispatch("PowerPoint.Application")
            self.presentation = self.app.Presentations.Open(FileName=u'G:\\preLogueClient\\preLogue\\slides\\java.pptx', ReadOnly=1)
            self.presentation.SlideShowSettings.Run()
        except:
            print("Powerpoint not Open")

    def main_loop(self, message):
        print message
        if message == 'action.next':
            self.presentation.SlideShowWindow.View.Next()
            return "action.next"

        elif message == 'action.previous':
            self.presentation.SlideShowWindow.View.Previous()
            return "action.previous"

        elif message == 'action.exit':
            self.presentation.SlideShowWindow.View.Exit()
            return "action.exit"

        elif message == 'action.quit':
            self.app.Quit()
            return "action.quit"

    def goToSlide(self, index):
        self.presentation.SlideShowWindow.View.GotoSlide(index)
