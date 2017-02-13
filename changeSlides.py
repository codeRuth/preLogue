import win32com.client
from getAction import getTopAction


class Slide(object):
    def __init__(self):
        self.getA = getTopAction()
        try:
            self.app = win32com.client.Dispatch("PowerPoint.Application")
            self.presentation = self.app.Presentations.Open(FileName=u'p.pptx', ReadOnly=1)
            self.presentation.SlideShowSettings.Run()
        except:
            print("Powerpoint not Open")

    def main_loop(self, message):
        action = self.getA.get_top_classifier(message)
        print action

        if action['class_name'] == 'action.next':
            print("next")
            self.presentation.SlideShowWindow.View.Next()

        elif action['class_name'] == 'action.previous':
            print("previous")
            self.presentation.SlideShowWindow.View.Previous()

        elif action['class_name'] == 'action.exit':
            print("exit")
            self.presentation.SlideShowWindow.View.Exit()

        elif action['class_name'] == 'action.quit':
            print("quit")
            self.app.Quit()
