from tkinter import E
from bottle import delete, redirect, response
import g

##############################
@delete("/tweet-delete/<tweet_id>")
def _(tweet_id):

    # tweet_id = request.forms.get("tweet_id")
    print(tweet_id , g)

    try:
        for index, tweet in enumerate(g.TWEETS):
            

            if tweet["id"] == tweet_id:
                response.status = 200
                g.TWEETS.pop(index)

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"server error"}