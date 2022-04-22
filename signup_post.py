from bottle import post, redirect, request, error
import g
import re
import uuid

##############################
@post("/signup")
def _():
    # user_name = request.forms.get("user_name")
    # user_last_name = request.forms.get("user_last_name")
    # user_username = request.forms.get("user_username")
    # user_email = request.forms.get("user_email")
    # user_password = request.forms.get("user_password")
    # user_id = str(uuid.uuid4())
    # user = {"id":user_id, "username":user_username, "name":user_name, "last_name":user_last_name, "email":user_email, "password":user_password}
    # g.USERS.append(user)
    # return redirect(f"/signup-ok?user-username={user_username}") 


    if not request.forms.get("user_name"):
        return redirect("/signup?error=user_name")
    if len(request.forms.get("user_name")) < 2:
        return redirect("/signup?error=user_name")
    
    user_name = request.forms.get("user_name")

    if not request.forms.get("user_last_name"):
        return redirect("/signup?error=user_last_name&user_name={user_name}")
    if len(request.forms.get("user_last_name")) < 2:
        return redirect("/signup?error=user_last_name&user_name={user_name}")
    
    user_last_name = request.forms.get("user_last_name")

    if not request.forms.get("user_username"):
        return redirect("/signup?error=user_username&user_last_name={user_last_name}&user_name={user_name}")
    if len(request.forms.get("user_username")) < 2:
        return redirect("/signup?error=user_username&user_last_name={user_last_name}&user_name={user_name}")
    
    user_username = request.forms.get("user_username")

    if not request.forms.get("user_email"):
        return redirect("/signup?error=user_email&user_username={user_username}&user_last_name={user_last_name}&user_name={user_name}")
    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        return redirect("/signup?error=user_email&user_username={user_username}&user_last_name={user_last_name}&user_name={user_name}")
    
    user_email = request.forms.get("user_email")

    if not request.forms.get("user_password"):
        return redirect(f"/signup?error=user_password&user_email={user_email}&user_username={user_username}&user_last_name={user_last_name}&user_name={user_name}")
    if len(request.forms.get("user_password")) < 6:
        return redirect(f"/signup?error=user_password&user_email={user_email}&user_username={user_username}&user_last_name={user_last_name}&user_name={user_name}")
    if len(request.forms.get("user_password")) > 20:
        return redirect(f"/signup?error=user_password&user_username={user_username}")

    user_password = request.forms.get("user_password")

    user_id = str(uuid.uuid4())
    user = {"id":user_id, "username":user_username, "name":user_name, "last_name":user_last_name, "email":user_email, "password":user_password}
    g.USERS.append(user)
    return redirect(f"/signup-ok?user-username={user_username}") 
