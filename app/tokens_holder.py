import json

class Tokens():
    com_token = None
    user_token = None

    @staticmethod
    def Collect():
        tokens_file = open('../config/access_tokens.tkn')
        tokens_dict = dict(json.loads(tokens_file.read()))
        if 'community token' in tokens_dict.keys():
            Tokens.com_token = tokens_dict


