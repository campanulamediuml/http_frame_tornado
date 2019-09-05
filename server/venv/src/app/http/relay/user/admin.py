from data.server import Data

class User(object):
    def __init__(self,user_id,user_role,user_token,login_time):
        self._id = user_id
        self.token = user_token
        self.role = user_role
        self.login_time = login_time

    def get_user_id(self):
        return self._id