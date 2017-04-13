from app import vk_api

print(vk_api.users.get(user_ids=(1,2)))