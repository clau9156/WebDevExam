from bottle import post, redirect, request
import g
import uuid
import time
import imghdr
import os

##############################
@post("/create-tweet")
def _():
    # title = request.forms.get("tweet_title")
    # description = request.forms.get("tweet_description")

    tweet_text = request.forms.get("tweet_text", "")
    tweet_image = request.files.get("tweet_image")

    file_name, file_extension = os.path.splitext(tweet_image.filename)

    tweet_id = str(uuid.uuid4())
    tweet_time = time.ctime(int(time.time()))

    # tweet={"tweet_id":tweet_id, "title":title, "description":description, "tweet_time":tweet_time}
    # g.TWEETS.append(tweet)
    # print(tweet)

    # return redirect("/tweet")

    image_name = f"{tweet_id}{file_extension}"
    tweet_image.save(f"images/{image_name}")

    tweet = {"id":tweet_id, "text":tweet_text, "image":tweet_image, "tweet_time":tweet_time}
    g.TWEETS.append(tweet)
    return tweet_id, "anything"