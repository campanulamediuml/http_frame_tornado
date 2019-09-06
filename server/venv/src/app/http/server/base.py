import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from common.Scheduler import Scheduler

class ServerBase(object):

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._apps = self.register_handles()

    def register_handles(self):
        # 
        return handlers
  
    def run(self):
        print("start server")
        print(self._host + ":" + str(self._port))
        tornado.options.parse_command_line()
        http_server = tornado.httpserver.HTTPServer(tornado.web.Application(self._apps))
        http_server.bind(self._port, self._host)
        http_server.start(0) 
        # http_server.listen(self._port, self._host)
        tornado.ioloop.PeriodicCallback(Scheduler.run, 500).start()
        # Scheduler.run(True)
        tornado.ioloop.IOLoop.current().start()