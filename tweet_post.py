from bottle import post, redirect, request, response
import g
import uuid
import time
import imghdr
import os
import jwt

##############################
@post("/create-tweet")
def _():
    # VALIDATE
    if len(g.SESSIONS) < 1:
        response.status = 400
        return redirect("/login?error=invalid")
    if not (request.get_cookie("jwt")):
        response.status = 400
        return redirect("/login?error=invalid")
    
    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt, "smart key", algorithms="HS256")

    try:
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
        return tweet_id
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"error"}