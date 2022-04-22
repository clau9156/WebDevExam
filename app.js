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

    const tweet_id = await connection.text()
    // <div>${document.querySelector("input", form).value}</div>
    let tweet = `
    <div id="${tweet_id}" class="tweet">
        <div>${_one("input[type=text]", form).value}</div>
        <div>${_one("input[type=file]", form).value}</div>
        <img src="/images/23df3ae2-0c6c-4cd0-845a-31c458c571ce.png">
    </div>
    `

    // replace with image id from server

    // document.querySelector("input", form).value = ""
    _one("input", form).value = ""

    // document.querySelector("#tweets").insertAdjacentHTML("afterbegin", tweet)
    _one("#tweets").insertAdjacentHTML("afterbegin", tweet)
}