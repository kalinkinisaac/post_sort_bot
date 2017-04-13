from app import vk_api, access_token

print(vk_api.messages.getDialogs(offset=0, count = 10))