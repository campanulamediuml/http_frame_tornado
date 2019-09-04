from app.http.mods import test_mod
from app.http.mods import shop
from app.http.mods import agent
from app.http.mods import player
from app.http.mods import admin

route_list = []
route_list.extend(test_mod.route_list)
route_list.extend(shop.route_list)
route_list.extend(agent.route_list)
route_list.extend(player.route_list)
route_list.extend(admin.route_list)