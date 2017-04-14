#import vk, urllib
#vk_api_version = '5.63'
#vk_api_lang = 'ru'
#vk_api_timeout = 10

# TODO: fix token
#access_token = open('../config/access_tokens.tkn', 'r').readline()
#session = vk.Session()#vk.AuthSession(app_id=5974863, user_login='+79636800030', user_password='r75:!779B')
#vk_api = vk.API(session, v=vk_api_version, lang=vk_api_lang, timeout=vk_api_timeout)

from .vk_apies import Vk

Vk.init()