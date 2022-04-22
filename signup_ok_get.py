from bottle import get, request, view
import uuid
import g

##############################
@get("/signup-ok")
@view("signup-ok")
def _():
    user_username = request.params.get("user-username")
    return dict(user_username=user_username)   