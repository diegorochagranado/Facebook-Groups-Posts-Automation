from face_login_post.Facebook import FACEBOOK_GROUPS_POST
from face_login_post.Facebook_User_Information import FACEBOOK_USERNAME_INFORMATION


post_text = ''' '''

user_information = FACEBOOK_USERNAME_INFORMATION()
username = user_information.username()
password = user_information.password()

test = FACEBOOK_GROUPS_POST()

test.sign_in(username,password)

groups = user_information.groups()
for group in groups:
    test.write_post(group,post_text)

test.close_browser()

