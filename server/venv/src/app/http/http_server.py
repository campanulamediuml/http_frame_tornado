from app.http.server.base import ServerBase
from app.http.relay.relay import Relay


from app.http.mods.test_mod import route_list

class HttpServer(ServerBase):

    def __init__(self, host, port):
        ServerBase.__init__(self, host, port)
        Relay.init(self)

    def register_handles(self):
        route = []
        route.extend(route_list)

        return route


