from re import I
from bottle import put, request, response, redirect
import g
import jwt

@put("/tweet-update")
def _():

    tweet_id = request.forms.get('tweet_id')
    updated_text = request.forms.get('tweet_text_update').strip()
    print("#"*40)
    print(updated_text, tweet_id)

    try:
        encoded_jwt = request.get_cookie("jwt")
        user_info = jwt.decode(encoded_jwt, "smart key", algorithms="HS256")

        for tweet in g.TWEETS:
            if tweet["id"] == tweet_id:
                tweet["text"] = updated_text
                print(tweet)
        
        response.status = 200
        return dict(username = user_info["username"], tweets=g.TWEETS)
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"error"}