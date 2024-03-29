db_config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'12345678',
    'database':'test_base',
    'port':3306,
}

mongo_address = "mongodb://127.0.0.1:27017"
refresh_time = '00:00:00'

http_config = {
    'host':'0.0.0.0',
    'port':9527
}

mqtt_server = 'mq.aichihuo.vip'
mq_time_out = 15

push_config = {
    'host':'0.0.0.0',
    'port':9001,
    'client_host':'127.0.0.1'
}
# ws超时时间
ws_time_out = 15
# token超时时间
token_time_out = 120

# 用户类型
admin_type=9
player_type=10