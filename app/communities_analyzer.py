from app import Vk

print(Vk.pub_api.wall.get(owner_id=-1, offset=0, count=3))