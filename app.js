function _one(q, e=document){return e.querySelector(q)}
function _all(q, e=document){return e.querySelectorAll(q)}



async function sendTweet() {
    const form = event.target
    // const button = document.querySelector("button[type='submit']", form)
    const button = _one("button[type='submit']", form)
    console.log(button)
    const connection = await fetch("/create-tweet", {
        method : "POST",
        body : new FormData(form)
    })

    if( ! connection.ok ){
        return
    }
    console.log("works")

    const tweet_id = await connection.text()
    // <div>${document.querySelector("input", form).value}</div>
    console.log(tweet_id)
    let tweet = `
    <div id="${tweet_id}" class="tweet">
        
        <div>${_one("input[type=text]", form).value}</div>
        <div>${_one("input[type=file]", form).value}</div>
        <img src="/images/23df3ae2-0c6c-4cd0-845a-31c458c571ce.png">
        <div>
            <button onclick="tweet_delete('${tweet_id}')">DELETE</button>
            <button onclick="tweet_update()">UPDATE</button>
        </div>
        
    

    </div>
    `


    // replace with image id from server

    // document.querySelector("input", form).value = ""
    _one("input", form).value = ""

    // document.querySelector("#tweets").insertAdjacentHTML("afterbegin", tweet)
    _one("#tweets").insertAdjacentHTML("afterbegin", tweet)
    console.log(tweet_id)
}

// DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE

async function tweet_delete(tweet_id) {
    console.log("delete")
    console.log(tweet_id)
    const connection = await fetch(`/tweet-delete/${tweet_id}`, {
        method : "DELETE",
    })

    if( ! connection.ok ){
        return
    }
    
    // _one(`[id="${tweet_id}"]`).remove()
    document.querySelector(`[id='${tweet_id}']`).remove()
}

// UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE

async function updateTweet() {
    const form = event.target
    // const button = _one("button[type='submit']", form)
    // console.log(button)
    const connection = await fetch("/update-tweet", {
        method : "PUT",
        body : new FormData(form)
    })

    if( ! connection.ok ){
        return
    }
    console.log("update")

    const text_connection = await connection.text();
    const object_connection = JSON.parse(text_connection);

    _one("#tweets").innerHTML = "";
    object_connection.tweets.forEach(tweet => {
        if (object_connection.user_id == tweet.user_id) {
            let updated_tweet = `
            <div id="${tweet_id}" class="tweet">
        
                <div>${_one("input[type=text]", form).value}</div>
                <div>${_one("input[type=file]", form).value}</div>
                <img src="/images/23df3ae2-0c6c-4cd0-845a-31c458c571ce.png">
                <div>
                    <button onclick="tweet_delete('${tweet_id}')">DELETE</button>
                    <button onclick="tweet_update()">UPDATE</button>
                </div>
            
        
    
            </div>
            `
            _one("input", form).value = ""

            // document.querySelector("#tweets").insertAdjacentHTML("afterbegin", tweet)
            _one("#tweets").insertAdjacentHTML("afterbegin", updated_tweet)
            console.log(tweet_id)
        }
    })
}