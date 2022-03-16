import json

def read_user_information():
    with open(r'face_login_post\user_information.json', encoding='utf8') as f:
        user_information = json.load(f)
    return user_information

class FACEBOOK_USERNAME_INFORMATION:

    def username(self):
        user_information = read_user_information()
        user = user_information["username"]
        return user

    def password(self):
        user_information = read_user_information()
        passw = user_information["password"]
        return passw

    def groups(self):
        user_information = read_user_information()
        groups = user_information["groups"]
        return groups