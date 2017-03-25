import win32com.client
from getAction import getTopAction


class Slide(object):
    def __init__(self):
        self.getA = getTopAction()
        try:
            self.app = win32com.client.Dispatch("PowerPoint.Application")
            self.presentation = self.app.Presentations.Open(FileName=u'G:\\preLogue\\preLogue\\p.pptx', ReadOnly=1)
            self.presentation.SlideShowSettings.Run()
        except:
            print("Powerpoint not Open")

    def get_top_classifier(self, message):
        return self.getA.get_top_classifier(message)

    def main_loop(self, message):
        action = self.get_top_classifier(message)
        print action
        if action['class_name'] == 'action.next':
            self.presentation.SlideShowWindow.View.Next()
            return "action.next"

        elif action['class_name'] == 'action.previous':
            self.presentation.SlideShowWindow.View.Previous()
            return "action.previous"

        elif action['class_name'] == 'action.exit':
            self.presentation.SlideShowWindow.View.Exit()
            return "action.exit"

        elif action['class_name'] == 'action.quit':
            self.app.Quit()
            return "action.quit"
