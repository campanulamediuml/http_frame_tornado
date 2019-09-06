from app.http.mods.test_mod.handlers.test import test
from app.http.mods.test_mod.handlers.gen_test import gen_test
from app.http.mods.test_mod.handlers.ws_sender import ws_sender
from app.http.mods.test_mod.handlers.mqtt_test import mqtt_test

route_list = [
    (r'/test/test',test),
    (r'/test/gen_test',gen_test),
    (r'/test/ws_sender',ws_sender),
    (r'/test/mqtt_test',mqtt_test),

]