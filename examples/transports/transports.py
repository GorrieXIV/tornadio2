from os import path as op

import tornado.web
import tornadio3
import tornadio3.router
import tornadio3.server
import tornadio3.conn

ROOT = op.normpath(op.dirname(__file__))


class IndexHandler(tornado.web.RequestHandler):
    """Regular HTTP handler to serve the chatroom page"""
    def get(self):
        self.render('index.html')


class SocketIOHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('../socket.io.js')


class WebSocketFileHandler(tornado.web.RequestHandler):
    def get(self):
        # Obviously, you want this on CDN, but for sake of
        # example this approach will work.
        self.set_header('Content-Type', 'application/x-shockwave-flash')

        with open(op.join(ROOT, '../WebSocketMain.swf'), 'rb') as f:
            self.write(f.read())
            self.finish()


class ChatConnection(tornadio3.conn.SocketConnection):
    # Class level variable
    participants = set()

    def on_open(self, info):
        self.send("Welcome from the server.")
        self.participants.add(self)

    def on_message(self, message):
        # Pong message back
        for p in self.participants:
            p.send(message)

    def on_close(self):
        self.participants.remove(self)

# Create chat server
ChatRouter = tornadio3.router.TornadioRouter(ChatConnection, dict(websocket_check=True))

# Create application
application = tornado.web.Application(
    ChatRouter.apply_routes([(r"/", IndexHandler),
                             (r"/socket.io.js", SocketIOHandler),
                             (r"/WebSocketMain.swf", WebSocketFileHandler)
                            ]),
    flash_policy_port = 843,
    flash_policy_file = op.join(ROOT, 'flashpolicy.xml'),
    socket_io_port = 8001
)

if __name__ == "__main__":
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    tornadio3.server.SocketServer(application)
