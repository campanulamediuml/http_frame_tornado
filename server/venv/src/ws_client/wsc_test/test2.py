from ws_client.WS import WSC 

def test2():
    WSC.send_data('req_my_sid',{})
    # WSC.update_result()
    print('test2',WSC.get_result())