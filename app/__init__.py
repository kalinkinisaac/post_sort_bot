import vk, urllib
vk_api_version = '5.63'
vk_api_lang = 'ru'
vk_api_timeout = 10

# TODO: fix token
access_token = open('../config/access_token.tkn', 'r').readline()
session = vk.Session()
vk_api = vk.API(session, v=vk_api_version, lang=vk_api_lang, timeout=vk_api_timeout)