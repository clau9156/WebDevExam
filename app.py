from bottle import default_app, error, get, post, redirect, request, run, static_file, view
import uuid
import re
import g

##############################
# import home_get             #GET
import signup_get           #GET
import signup_ok_get        #GET
import login_get            #GET
import users_get            #GET
import logout_get           #GET
import tweet_get            #GET
# import tweet_create_get     #GET
# import tweet_update_get     #GET

import tweet_update_post    #POST
import tweet_delete         #DELETE
import login_post           #POST
import signup_post          #POST
import tweet_post           #POST

import tweet_put            #PUT


##############################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

##############################
@get("/app.js")
def _():
    return static_file("app.js", root=".")

##############################
@get("/validator.js")
def _():
    return static_file("validator.js", root=".")

##############################
@get("/images/<image_name>")
def _(image_name):
    return static_file(image_name , root="./images") 

##############################
@get("/")
@view("index")
def _():
    return dict(tweets=g.TWEETS)

##############################
try:
    import production
    application = default_app()
except Exception as ex:
    print(ex)
    run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")