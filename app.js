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
    const text_connection = await connection.text();
    const object_connection = JSON.parse(text_connection);
    const tweet_info = object_connection.tweet;
    console.log(text_connection);
    const tweet_id = text_connection.slice(0, 36);
    const tweet_time = text_connection.slice(36, 60);
    const image_name = text_connection.slice(60, 100);
    console.log (tweet_time)
    // const username = text_connection.slice(10); 

    // <div>${document.querySelector("input", form).value}</div>
    console.log(tweet_id)
    let tweet = ''
    if (image_name == "false") {

        if(tweet_info.like == "true"){
            tweet = `
            <div id="${tweet_info.id}" class="tweet">
                <div>${tweet_info.username}</div>
                <div>${tweet_info.tweet_time}</div>
                <div>${tweet_info.text}</div>
                <div class="show">
                    <img src="/svg/heart-solid.svg" alt="like"/>
                </div>
                <div>
                    <button onclick="tweet_delete('${tweet_info.id}')">DELETE</button>
                    <button onclick="tweet_update('${tweet_info.id}', '${tweet_info.text}')">UPDATE</button>
                </div>
            </div>
            `
        } else {
            tweet = `
            <div id="${tweet_info.id}" class="tweet">
                <div>${tweet_info.username}</div>
                <div>${tweet_info.tweet_time}</div>
                <div>${tweet_info.text}</div>
                <div>
                    <button onclick="tweet_delete('${tweet_info.id}')">DELETE</button>
                    <button onclick="tweet_update('${tweet_info.id}', '${tweet_info.text}')">UPDATE</button>
                </div>
            </div>
            `
        }
    } else {
        if(tweet_info.like == "true"){
            tweet = `
            <div id="${tweet_info.id}" class="tweet">
                <div>${tweet_info.username}</div>
                <div>${tweet_info.tweet_time}</div>
                <div>${tweet_info.text}</div>
                <div class="show">
                    <img src="/svg/heart-solid.svg" alt="like"/>
                </div>
                <img src="/images/${tweet_info.image}" alt="tweet_image"/>
                <div>
                    <button onclick="tweet_delete('${tweet_info.id}')">DELETE</button>
                    <button onclick="tweet_update('${tweet_info.id}', '${tweet_info.text}', '/images/${tweet_info.image}')">UPDATE</button>
                </div>
            </div>
            `
        } else {
            tweet = `
            <div id="${tweet_info.id}" class="tweet">
                <div>${tweet_info.username}</div>
                <div>${tweet_info.tweet_time}</div>
                <div>${tweet_info.text}</div>
                
                <img src="/images/${tweet_info.image}" alt="tweet_image"/>
                <div>
                    <button onclick="tweet_delete('${tweet_info.id}')">DELETE</button>
                    <button onclick="tweet_update('${tweet_info.id}', '${tweet_info.text}', '/images/${tweet_info.image}')">UPDATE</button>
                </div>
            </div>
            `
        }
    }   



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
    const connection = await fetch("/tweet-update", {
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
        if (object_connection.username == tweet.username) {
            if (tweet.image_name) {
                const new_tweet = `
                <div id="${tweet.id}" class="tweet">
                    <div>${tweet.username}</div>
                    <div>${tweet.tweet_time}</div>
                    <div>${tweet.text}</div>
                    <div>${tweet.image_name}</div>
                    <div>
                        <button onclick="tweet_delete('${tweet.id}')">DELETE</button>
                        <button onclick="tweet_update('${tweet.id}', '${tweet.text}')">UPDATE</button>
                    </div>
                </div>
                `
                // _one("input", form).value = ""

                // document.querySelector("#tweets").insertAdjacentHTML("afterbegin", tweet)
                _one("#tweets").insertAdjacentHTML("afterbegin", new_tweet);
                _one(".update_modal").style.display = "none";
                console.log("updated");
                console.log(new_tweet);
            } else {
                const new_tweet = `
                <div id="${tweet.id}" class="tweet">
                    <div>${tweet.username}</div>
                    <div>${tweet.tweet_time}</div>
                    <div>${tweet.text}</div>
                    <div>
                        <button onclick="tweet_delete('${tweet.id}')">DELETE</button>
                        <button onclick="tweet_update('${tweet.id}', '${tweet.text}')">UPDATE</button>
                    </div>
                </div>
                `
                // _one("input", form).value = ""

                // document.querySelector("#tweets").insertAdjacentHTML("afterbegin", tweet)
                _one("#tweets").insertAdjacentHTML("afterbegin", new_tweet);
                _one(".update_modal").style.display = "none";
                console.log("updated");
                console.log(new_tweet);
            }
        }
    })
}

// TWEET MODAL UPDATE TWEET MODAL UPDATE TWEET MODAL UPDATE TWEET MODAL UPDATE TWEET MODAL UPDATE TWEET MODAL UPDATE
function tweet_update(tweet_id, tweet_text) {
    console.log(tweet_id, tweet_text);
    _one("#div_tweet_id input[type=text]").value = tweet_id;
    _one(".update_modal").style.display = "block";
    _one("#tweet_text_update").value = tweet_text;
    console.log(tweet_text);
    
    document.getElementById("close_modal").addEventListener("click", closeModal);
}

// TWEET MODAL CLOSE TWEET MODAL CLOSE TWEET MODAL CLOSE TWEET MODAL CLOSE TWEET MODAL CLOSE TWEET MODAL CLOSE
function closeModal() {
    _one(".update_modal").style.display = "none";
    console.log("closed modal");
}

// LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE
// LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE LIKE
async function tweet_like(tweet_id) {
    target = event.target;
    const connection = await fetch(`/tweet_like/${tweet_id}`, {
        method: "PUT"
    })

    if (!connection.ok) {
        return
    }

    const text_connection = await connection.text();
    console.log(text_connection);
    if(text_connection == "liked") {
        target.style.display = "block";
    } else {
        target.style.display = "none";
    }
}



// const searchBar = document.querySelector("#searchBar");

// SEARCH SEARCH SEARCH SEARCH SEARCH SEARCH SEARCH SEARCH SEARCH SEARCH SEARCH SEARCH SEARCH SEARCH
// searchBar.addEventListener("keyup", (e) => {
//     console.log("search");
//     let searchString = e.target.value;
//     let emptyArray = [];
//     if(searchString) {
//         emptyArray = suggestions.filter((users)=>
//         return users.toLowerCase().u)
//     }
//     searchString = searchString.toLowerCase();
//     const filterUsers = users.filter((user) => {
//         return (user.username.toLowerCase().includes(searchString));
//     });
//     displayListFiltered(filterUsers);
// });

// function displayUser(user) {
//     _one("[data-field=username]").textContent = user.user
// }

// function displayListFiltered(filtered) {
//     document.querySelector("#list li").innerHTML = "";
//     filtered.forEach(displayUser);
// }
// let 

