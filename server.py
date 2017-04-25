import os

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket

from lib.keywordr import keywordr as k

# from keywordExt import GetKeywords

PORT = 5000
UPLOAD_PATH = 'uploads/'


# slideObj = Slide()
# key = GetKeywords()

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
        print 'get_keywords(query) = ', k.get_keywords(message)
        # self.write_message(key.getKey(message))
        # slideObj.main_loop(message)

    def on_close(self):
        print("Connection Closed.")


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        print "Im being called"
        if self.request.files.get('uploadfile', None):
            uploadFile = self.request.files['uploadfile'][0]
            filename = uploadFile['filename']
            fileObj = open(UPLOAD_PATH + filename, 'wb')
            fileObj.write(uploadFile['body'])
            self.redirect('/')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/ws', WebSocketHandler),
            (r'/', IndexHandler),
            ('/upload', UploadHandler),
            (r'/(.*)', tornado.web.StaticFileHandler, {'path': os.path.dirname(__file__)})
        ]
        tornado.web.Application.__init__(self, handlers, debug=True)


if __name__ == '__main__':
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(PORT)
    print('*** Server Started at 127.0.0.1 : %d ***' % PORT)
    tornado.ioloop.IOLoop.instance().start()
