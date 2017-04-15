import vk
from .tokens_holder import Tokens


class Vk():
    # API parameters
    api_version = '5.63'
    api_lang = 'ru'
    api_timeout = 10

    # Sessions
    pub_session = None
    com_session = None
    user_session = None

    # VK APIes
    pub_api = None
    com_api = None
    user_api = None

    @staticmethod
    def init():
        Tokens.collect()
        # User vk API init
        print("Auth...\n")
        Vk.user_session = vk.AuthSession(
            app_id=Tokens.app_id,
            user_login=Tokens.user_token['user_login'],
            user_password=Tokens.user_token['user_password']
        )
        Vk.user_api = vk.API(Vk.user_session, v=Vk.api_version, lang=Vk.api_lang, timeout=Vk.api_timeout)

        # Pub vk API init
        Vk.pub_session = vk.Session()
        Vk.pub_api = vk.API(Vk.pub_session, v=Vk.api_version, lang=Vk.api_lang, timeout=Vk.api_timeout)

        # Com vk API init
        Vk.com_session = vk.Session(access_token=Tokens.com_token)
        Vk.com_api = vk.API(Vk.com_session, v=Vk.api_version, lang=Vk.api_lang, timeout=Vk.api_timeout)
        print("Done!\n")

