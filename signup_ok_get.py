from bottle import get, request, view, response
import uuid
import g

##############################
@get("/signup-ok")
@view("signup-ok")
def _():
    try:
        user_username = request.params.get("user-username")
        return dict(user_username=user_username)   
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"error"}