from app.push.handler.broad_cast_handler import cs_execute

import json

class WebSocketHandlers():

    def __init__(self):
        pass

    @staticmethod
    def test(sid, _):
        print('done!')


    @staticmethod
    def register(sio):
        # 注册消息事件
        handler_list = dict()
        handler_list['connect'] = WebSocketHandlers.connect
        handler_list['disconnect'] = WebSocketHandlers.user_exit
        handler_list['heart_beat'] = WebSocketHandlers.heart_beat
        handler_list['req_my_sid'] = WebSocketHandlers.get_my_sid
        handler_list['req_test'] = WebSocketHandlers.req_test


        handler_list['REQ_LOGIN'] = WebSocketHandlers.handler_login
        handler_list['ADMIN_IN'] = WebSocketHandlers.admin_in
        handler_list['REQ_PUSH_INFO'] = WebSocketHandlers.push_info

        for code, handler in handler_list.items():
            sio.on(code, namespace='/')(handler)

    #=======================================================
    

    @staticmethod
    def connect(sid, environ):
        # print(request.sid)
        return
    # 链接

    # ==================
    @staticmethod
    def on_message(sid, message):
        pass

    def on_locse(self):
        pass

    def check_origin(self, origin):
        return True

    # 简单方法
    # 测试用
    # =====================
    @staticmethod
    def get_my_sid(sid,environ):
        cs_execute.get_my_sid(sid)
        return

    @staticmethod
    def req_test(sid,environ):
        try:
            data = json.loads(environ)
        except:
            data = environ
        cs_execute.req_test(sid,data)
        return
    # =====================
    # 正式方法
    @staticmethod
    def heart_beat(sid,environ):
        cs_execute.heart_beat(sid)
        return

    @staticmethod
    def handler_login(sid, environ):
        # 用户登录请求
        try:
            data = json.loads(environ)
        except:
            data = environ

        cs_execute.login(sid, data)
        return

    @staticmethod
    def admin_in(sid,environ):
        cs_execute.connect_push_system(sid)
        return

    @staticmethod
    def push_info(sid,environ):
        try:
            data = json.loads(environ)
        except:
            data = environ

        cs_execute.push_info(sid,data)
        return

    @staticmethod
    def user_exit(sid):
        # 用户退出请求
        cs_execute.user_exit(sid)
        return





    

