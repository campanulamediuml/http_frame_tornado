from ws_client.WS import WSC 
import json
from flask import Flask

# # test1.test1()
# # test2.test2()

# CountdownTask(15,exit)
app = Flask(__name__)

@app.route('/')
def get_test():
    data = {}
    WSC.send_data('req_my_sid',data)
    res = WSC.get_result()
    return json.dumps(res)

    

app.run('127.0.0.1',9876)