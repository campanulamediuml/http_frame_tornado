from data.server import Data
from app.push.relay import Relay
from werkzeug.security import generate_password_hash, check_password_hash

class cs_execute():

    @staticmethod
    def login(sid,data):
        phone = data['phone']
        pw = data['passwd']

        user_info = Data.find('openluat_user',[('phone','=',phone)])
        if user_info == None:
            Relay.send_error(sid)

        if check_password_hash(pw,user_info['password_hash']) != True:
            Relay.send_error(sid)

        user_id = user_info['id']

        Relay.user_login(sid,user_id)
        return

    @staticmethod
    def connect_push_system(sid):
        # Data.find()
        Relay.connect_push_system(sid)
        return

    @staticmethod
    def push_info(sid,data):
        # Data.find()
        if Relay.is_admin(sid) == False:
            return
        to_user_id = data['user_id']
        user = Relay.get_user(user_id)
        if user == None:
            return


        msg = data['msg']
        Relay.send_msg_by_user_id(user.get_id(),'ACK_PUSH',msg)
        return

    @staticmethod
    def user_exit(sid):
        if Relay.is_admin(sid) == True:
            Relay.kill_admin(sid)
            return

        user = Relay.get_user_by_sid(sid)
        if user != None:
            user_id = user.get_id()
            Relay.user_exit(user_exit)

        print(sid,'退出了推送系统')
        return


    @staticmethod
    def get_my_sid(sid):
        print(sid)
        data = {
            'sid':sid,
        }
        code = 'ack_send_sid'
        Relay.send_msg(sid, code, data)
        return


