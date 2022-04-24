from bottle import post, redirect, request, response
import re
import g
import time
import uuid
import jwt

@post ("/admin-login")
def _():
    if not request.forms.get("user_username"):
        return redirect("/admin-login?error=user_username")
    if len(request.forms.get("user_username")) < 5:
        return redirect("/admin-login?error=user_username")
    if len(request.forms.get("user_username")) > 20:
        return redirect("/admin-login?error=user_username")

    user_username = request.forms.get("user_username")

    if not request.forms.get("user_password"):
        return redirect(f"/admin-login?error=user_password&user_username={user_username}")
    if len(request.forms.get("user_password")) < 6:
        return redirect(f"/admin-login?error=user_password&user_username={user_username}")
    if len(request.forms.get("user_password")) > 20:
        return redirect(f"/admin-login?error=user_password&user_username={user_username}")

    user_password = request.forms.get("user_password")

    for user in g.USERS:
        if user["password"] == "AdminPassword" and user["username"] == "administrator":
            user_session_id = str(uuid.uuid4())
            session = {"session_id":user_session_id, "username":user_username, "iat": int(time.time())}
            g.SESSIONS.append(session)
            encoded_jwt = jwt.encode(session, "smart key", algorithm="HS256")
            response.set_cookie("jwt", encoded_jwt)
            return redirect("/admin")

    return redirect("/admin")