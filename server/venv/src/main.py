from config.config import http_config
from app.http.http_server import HttpServer


host = http_config['host']
port = http_config['port']
print('http_server_runing',host,port)
server = HttpServer(host, port)
server.run()

