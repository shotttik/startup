const check_url_web = (url) => {
    const website_list = ['https://alta.ge/', 'https://zoommer.ge/', 'https://ultra.ge/']
    for (const item of website_list) {
        if (url.startsWith(item))
            return true;
    };
    return false;
};

//setup before functions
let typingTimer;                //timer identifier
let doneTypingInterval = 200;  //time in ms 
let myInput = document.querySelector('.search-form-input');

//on keyup, start the countdown
myInput.addEventListener('keyup', () => {
    clearTimeout(typingTimer);
    if (myInput.value) {
        typingTimer = setTimeout(doneTyping, doneTypingInterval);
    }
});

//user is "finished typing," do something
function doneTyping() {
    let url = document.querySelector('.search-form-input').value;
    if (check_url_web(url)) {
        document.querySelector('.search-form-btn').disabled = false;
    };
}

document.querySelector('.search-form-btn').addEventListener('click', send_url)
document.querySelector('.search-form-clear-btn').addEventListener('click', function () {
    document.querySelector('.search-form-input').value = '';
    document.querySelector('.search-form-btn').disabled = true;
});
