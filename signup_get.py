from bottle import get, view, error, request

##############################
@get("/signup")
@view("signup")
def _():
    error = request.params.get("error")
    user_name = request.params.get("user_name")
    user_last_name = request.params.get("user_last_name")
    user_username = request.params.get("user_username")
    user_email = request.params.get("user_email")
    return dict(error=error, user_name=user_name, user_last_name=user_last_name, user_username=user_username, user_email=user_email)   