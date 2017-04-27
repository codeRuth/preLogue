import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket

from libkey.keywordr import keywordr as k
from getAction import getTopAction
from processSlide import ProcessSlide
from changeSlides import Slide

def processFile():
    # print os.path.abspath(fileUp)
    p = ProcessSlide('G:\\preLogueClient\\preLogue\\slides\\lecture2.pptx')
    return p.getKeywords()

PORT = 5000
UPLOAD_PATH = 'slides/'
g = getTopAction()
s = Slide()
keyWords = processFile()

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("index.html")


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def data_received(self, chunk):
        pass

    def open(self):
        print("Connection Open.")

    def on_message(self, message):
        cvi = g.get_top_classifier(message)
        key = k.get_keywords(message)
        print key
        # if cvi['confidence'] > 0.98:
        #     s.main_loop(cvi['class_name'])
        #     print cvi['class_name']
        #     print cvi['confidence']
        # else:
        #     for x in key:
        #         print x

        # self.write_message(key.getKey(message))
        # slideObj.main_loop(message)

    def on_close(self):
        print("Connection Closed.")


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        if self.request.files.get('uploadfile', None):
            uploadFile = self.request.files['uploadfile'][0]
            filename = uploadFile['filename']
            fileObj = open(UPLOAD_PATH + filename, 'wb')
            fileObj.write(uploadFile['body'])
            self.redirect('/')
            processFile(UPLOAD_PATH + filename)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/ws', WebSocketHandler),
            (r'/', IndexHandler),
            ('/upload', UploadHandler)
        ]
        tornado.web.Application.__init__(self, handlers,
                                         template_path='templates',
                                         static_path='static',
                                         debug=True)




if __name__ == '__main__':
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(PORT)
    print('*** Server Started at 127.0.0.1 : %d ***' % PORT)
    tornado.ioloop.IOLoop.instance().start()
