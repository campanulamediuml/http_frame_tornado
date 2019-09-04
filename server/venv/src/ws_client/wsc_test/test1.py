from ws_client.WS import WSC 
import json

def test1():
    data = {
        
    }
    WSC.send_data('REQ_LOGIN',data)
    WSC.update_result()
    res = WSC.get_result()
    print('test1',res)
    return json.dumps(res)
