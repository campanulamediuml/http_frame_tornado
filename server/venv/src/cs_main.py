from app.push.cs_server import GameServer
from config.config import push_config
   
print('running')
print('push_server in',push_config['host'],push_config['port'])
host = push_config['host']
port = push_config['port']
server = GameServer(host, port)
server.run()