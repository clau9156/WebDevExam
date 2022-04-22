from bottle import get, redirect, request
import g
import jwt

##############################
@get("/logout")
def _():
    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt, "smart key", algorithms="HS256")
    session = user_info
    g.SESSIONS.remove(session)
    return redirect("/login")