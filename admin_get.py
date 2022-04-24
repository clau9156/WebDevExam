from bottle import get, redirect, request, view, response
import g
import jwt

##############################
@get("/admin")
@view("admin")
def _():
    # VALIDATE
    # if len(g.SESSIONS) < 1:
    #     return redirect("/admin-login?error=invalid")
    # if not (request.get_cookie("jwt")):
    #     return redirect("/admin-login?error=invalid")
    
    # encoded_jswt = request.get_cookie("jwt")
    # user_info = jwt.decode(encoded_jwt, "smart key", algorithms="HS256")

    # for session in g.SESSIONS:
    #     if not session['session_id'] == user_info["session_id"]:
    #         response.status = 400
    #         return redirect("/admin-login?error=invalid")

    # user_id = user_info["user_id"],
    try:
        return dict(tweets=g.TWEETS, users=g.USERS, sessions=g.SESSIONS)
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"error"}