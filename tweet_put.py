from re import I
from bottle import put, request, response, redirect
import g
import jwt

@put("/tweet-update")
def _():
    tweet_id = request.forms.get("tweet_id")
    text_updated = request.forms.get("tweet_text_update").strip()

    try:
        encoded_jwt = request.get_cookie("jwt")
        user_info = jwt.decode(encoded_jwt, "smart key", algorithms="HS256")

        for tweet in g.TWEETS:
            if tweet["tweet_id"] == tweet_id:
                tweet["text"] == text_updated
        
        response.status = 200
        return dict(user_id = user_info["user_id"], tweets=g.TWEETS)
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"error"}