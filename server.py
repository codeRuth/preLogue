import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import os

from changeSlides import Slide

PORT = 5000

app = Slide()


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
        print(message)
        self.write_message(message)
        app.main_loop(message)

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
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(PORT)
    # hostIP = socket.gethostbyname(socket.gethostname())
    print('*** Websocket Server Started at localhost : %d***' % PORT)
    tornado.ioloop.IOLoop.instance().start()
