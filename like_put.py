from bottle import put, request, response
import g

@put("/tweet-like")
def _():
    tweet_id = request.forms.get('tweet_id')
    print(tweet_id)

    try:
        for tweet in g.TWEETS:
            if tweet["id"] == tweet_id:
                if tweet["like"] == "false":
                    tweet["like"] = "true"
                    is_liked = "liked"
                else:
                    tweet["like"] == "false"
                    is_liked = "no like"

        response.status = 200
        return is_liked

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"error"}