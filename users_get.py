from bottle import get, redirect, request, view
import g
import jwt

##############################
@get("/users")
@view("users")
def _():
    # VALIDATE
    if len(g.SESSIONS) < 1:
        return redirect("/login?error=invalid")
    if not (request.get_cookie("jwt")):
        return redirect("/login?error=invalid")
    
    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt, "smart key", algorithms="HS256")

    for session in g.SESSIONS:
        if not session['session_id'] == user_info["session_id"]:
            return redirect("/login?error=invalid")

    return dict(users=g.USERS, sessions=g.SESSIONS) 








