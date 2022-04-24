from bottle import error, get, request, view, response

##############################
@get("/admin-login")
@view("admin-login")
def _():
    try: 
        error = request.params.get("error")
        user_username = request.params.get("user_username")
        return dict(error=error, user_username=user_username) 

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"error"}