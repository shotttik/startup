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
    if (!isValidURL(url)) {
        alert("Please enter a valid URL");
        return;
    };
    postData('/get-product/', { 'url': url }).then((data) => {
        d = data.data;
        document.querySelector('.search-gr').className = 'col-lg-6'
        document.querySelector('.first-product-row').style.visibility = 'visible';
        document.querySelector('.first-product-title .card-title').textContent = d.title;
        document.querySelector('.first-product-img img').src = d.image;
        document.querySelector('.first-product-gpu .card-subtitle').textContent = d.gpu;
        document.querySelector('.first-product-price .price').textContent = d.price + ' ლ';
        console.log(data.json); // JSON data parsed by `data.json()` call
    });;
};