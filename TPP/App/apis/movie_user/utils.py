from flask import request, g
from flask_restful import abort

from App.apis.movie_user.model_utils import get_movie_user
from App.ext import cache
from App.utils import MOVIE_USER


def _verify():
    token = request.args.get("token")
    if not token:
        abort(401, msg=" not login")

    if not token.startswith(MOVIE_USER):
        abort(403, msg='no access')

    user_id = cache.get(token)

    if not user_id:
        abort(401, msg="用户不存在")
    user = get_movie_user(user_id)
    if not user:
        abort(401, msg="用户不存在")

    g.user = user
    g.auth = token


def login_required(fun):

    def wrapper(*args, **kwargs):
        _verify()
        return fun(*args, **kwargs)
    return wrapper


def require_permission(permission):
    def require_permission_wrapper(fun):
        def wrapper(*args, **kwargs):
            _verify()
            if not g.user.check_permission(permission):
                abort(403, msg="没有此权限")
            return fun(*args, **kwargs)
        return wrapper
    return require_permission_wrapper