from bottle import post, redirect, request
import g
import uuid
import time
import jwt

##############################
@post("/tweet-update")
def _():

    # VALIDATE
    if len(g.SESSIONS) < 1:
        return redirect("/login?error=invalid")
    if not (request.get_cookie("jwt")):
        return redirect("/login?error=invalid")
    
    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt, "smart key", algorithms="HS256")

    for session in g.SESSIONS:
        if not session['session_id'] == user_info["session_id"]:
            return redirect("/login?error=invalid")

    title_updated = request.forms.get("tweet_title")
    description_updated = request.forms.get("tweet_description")
    tweet_id = request.forms.get("tweet_id")
    tweet_time = request.forms.get("tweet_time")

    updated_tweet={"tweet_id":tweet_id, "title":title_updated, "description":description_updated, "tweet_time":tweet_time}
    
    print(updated_tweet)
    print("#"*30)
    print(g.TWEETS)

    for index, tweet in enumerate(g.TWEETS):
        if tweet["tweet_id"] == updated_tweet["tweet_id"]:
            print(tweet , updated_tweet)
            g.TWEETS.remove(tweet)
            g.TWEETS.append(updated_tweet)
            return redirect("/tweet")

    return redirect("/tweet")