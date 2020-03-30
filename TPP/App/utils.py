import hashlib
import time
import uuid
import requests


#短信验证码
def send_verify_code(phone):
    url = " https://api.netease.im/sms/sendcode.action"
    nonce = hashlib.new("sha512", str(time.time()).encode("utf-8")).hexdigest()
    curtime = str(int(time.time()))
    sha1 = hashlib.sha1()
    secret = "5bf0cd8994a6"
    sha1.update((secret + nonce + curtime).encode("utf-8"))
    check_sum = sha1.hexdigest()
    header = {
        "AppKey": "a531b96af2d2fa5de1f0bb140f53548b",
        "Nonce": nonce,
        "CurTime": curtime,
        "CheckSum": check_sum
    }
    post_data = {
        "mobile": phone
    }
    resp = requests.post(url, data=post_data, headers=header)
    return resp

""""
"""

MOVIE_USER = "movie_user"
ADMIN_USER = "admin_user"
CINEMA_USER = "cinema_user"

# 创建token
def generate_token(prefix=None):
    token = prefix + uuid.uuid4().hex
    return token


def generate_movie_user_token():
    return generate_token(prefix=MOVIE_USER)


def generate_admin_user_token():
    return generate_token(prefix=ADMIN_USER)


def generate_cinema_user_token():
    return generate_token(prefix=CINEMA_USER)
