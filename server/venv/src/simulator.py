import requests
import json
import time

url = 'https://api.aichihuo.vip/player/usemachine?token=db296ae1981c500c226159974b68747e'

def get(session, url, params={}):
    headers = {'Content-Type': 'application/json', 'User-Agent': 'MicroMessenger'}
    print(url)
    r = session.get(url, params=params, headers=headers)
    if r.status_code == requests.codes.ok:
        # print(r.headers)
        if isinstance(r.text, dict):
            print(json.loads(r.text))
        else:
            print(r.text)
        return r.text
    else:
        print(r.status_code)
        # print(r.headers)
        if isinstance(r.text, dict):
            print(json.loads(r.text))
        else:
            print(r.text)
        print(type(r.text))


def post(session, url, payload={}, params={}):
    headers = {'Content-Type': 'application/json'}
    r = session.post(url, params=params, data=json.dumps(payload), headers=headers)
    if r.status_code == requests.codes.ok:
        print(r.headers)
        print('显示请求头⤴')
        print(r.cookies.get_dict())
        if isinstance(r.text, dict):
            print(json.loads(r.text))
        else:
            print(r.text)
        return r.text
    else:
        print(r.status_code)
        print(r.headers)
        if isinstance(r.text, dict):
            print(json.loads(r.text))
        else:
            print(r.text)
        print(type(r.text))
        # print(json.loads(r.text)['msg'])

# id_pool = []
# while 1:
#     s = requests.session()
#     # time.sleep(5)
#     res = get(s,url)
#     res = json.loads(res)
#     event = res['data']['event_id']
#     if event in id_pool:
#         break

#     id_pool.append(event)
#     time.sleep(2)

# print(event,id_pool)
s = requests.session()
content = {"imei":"866262043966885"}
res = post(s,url,payload=content)
