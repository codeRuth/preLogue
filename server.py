import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket

from libkey.keywordr import keywordr as k
from getAction import getTopAction
from processSlide import ProcessSlide
from changeSlides import Slide
from convert.convert import convertPPT

PORT = 5000
UPLOAD_PATH = 'slides/'
top = getTopAction()
slideObj = Slide()
p = ProcessSlide('slides/java.pptx')

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("ammu.html")

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def data_received(self, chunk):
        pass

    def open(self):
        print("Connection Open.")

    def on_message(self, message):
        print p.getKeywords()
        for x in p.getKeywords():
            print x
        self.write_message(message)
        print message
        hello = top.get_top_classifier(message)
        print hello
        if hello['confidence'] > 0.98:
            slideObj.main_loop(hello)
        else:
            for index, x in enumerate(p.getKeywords()):
                if k.get_keywords(message) == x:
                    slideObj.goToSlide(index)


    def on_close(self):
        print("Connection Closed.")


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        if self.request.files.get('uploadfile', None):
            uploadFile = self.request.files['uploadfile'][0]
            filename = uploadFile['filename']
            fileObj = open(UPLOAD_PATH + filename, 'wb')
            fileObj.write(uploadFile['body'])
            conv = convertPPT(UPLOAD_PATH + filename)
            conv.convertPNG()
            self.redirect('/')

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
