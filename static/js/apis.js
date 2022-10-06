async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json(); // parses JSON response into native JavaScript objects
}


const send_url = () => {
    let url = document.querySelector('.search-form-input').value;
    postData('/search/', { 'url': url }).then((data) => {
        console.log(data.domain); // JSON data parsed by `data.json()` call
    });;
};