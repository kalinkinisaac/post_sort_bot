import json


class TokenError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
         return repr(self.value)


class Tokens:
    com_token = None
    user_token = None
    app_id = None
    @staticmethod
    def collect():
        # Debug
        print("Collecting tokens...\n")

        tokens_file = open('config/access_tokens.tkn')
        tokens_dict = dict(json.loads(tokens_file.read()))

        if 'user_token' in tokens_dict.keys():
            Tokens.user_token = tokens_dict['user_token']
        else:
            raise TokenError('There is not user_token in access_tokens.tkn')

        if 'community_token' in tokens_dict.keys():
            Tokens.com_token = tokens_dict['community_token']
        else:
            raise TokenError('There is not community_token in access_tokens.tkn')

        if 'app_id' in tokens_dict.keys():
            Tokens.app_id = tokens_dict['app_id']
        else:
            raise TokenError('There is not app_id in access_tokens.tkn')

        print("Collected!\n")