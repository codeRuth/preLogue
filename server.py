import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import os
import keywordr.keywordr as k
# from keywordExt import GetKeywords

from changeSlides import Slide

PORT = 5000


# slideObj = Slide()
# key = GetKeywords()

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
        print 'get_keywords(query) = ', k.get_keywords(message)
        # self.write_message(key.getKey(message))
        # slideObj.main_loop(message)

    def on_close(self):
        print("Connection Closed.")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/ws', WebSocketHandler),
            (r'/', IndexHandler),
            (r'/(.*)', tornado.web.StaticFileHandler, {'path': os.path.dirname(__file__)})
        ]
        tornado.web.Application.__init__(self, handlers, debug=True)


if __name__ == '__main__':
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(PORT)
    print('*** Server Started at 127.0.0.1 : %d ***' % PORT)
    tornado.ioloop.IOLoop.instance().start()
