from app.push.cs_server import GameServer
from config.config import push_config
   
print('running')
print('push_server in 9001')
host = push_config['host']
port = push_config['port']
server = GameServer(host, port)
server.run()