from bottle import error, get, request, view

##############################
@get("/login")
@view("login")
def _():
    error = request.params.get("error")
    user_username = request.params.get("user_username")
    return dict(error=error, user_username=user_username) 