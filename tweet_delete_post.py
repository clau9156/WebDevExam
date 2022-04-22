from bottle import post, redirect, request
import g
import jwt

##############################
@post("/tweet-delete/<tweet_id>")
def _(tweet_id):

    # tweet_id = request.forms.get("tweet_id")
    for index, tweet in enumerate(g.TWEETS):
        if tweet["tweet_id"] == tweet_id:
            g.TWEETS.pop(index)
            return redirect("/tweet")
    return redirect("/tweet")