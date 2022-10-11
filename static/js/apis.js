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

let search_gr = document.querySelector('.search-gr');
let first_product_row = document.querySelector('.first-product-row');
let first_product_title = document.querySelector('.first-product-title .card-title');
let first_product_img = document.querySelector('.first-product-img img');
let first_product_gpu = document.querySelector('.first-product-gpu .card-subtitle');
let first_product_price = document.querySelector('.first-product-price .price');
let url = document.querySelector('.search-form-input');



const send_url = () => {
    let url_value = url.value
    if (!isValidURL(url_value)) {
        alert("Please enter a valid URL");
        return;
    };
    postData('/get-product/', { 'url': url_value }).then((data) => {
        d = data.data;
        search_gr.className = 'col-lg-6 search-gr'
        first_product_row.style.visibility = 'visible';
        first_product_title.textContent = d.title;
        first_product_img.src = d.image;
        first_product_gpu.textContent = d.gpu;
        first_product_price.textContent = d.price + ' ლ';
    });;

};


const search_product = () => {
    let url_value = url.value
    if (!isValidURL(url_value)) {
        alert("Url isn't valid a valid URL");
        return;
    };
    postData('/get-product/', { 'gpu': first_product_gpu.textContent }).then((data) => {
        d = data.data;
        search_gr.className = 'col-lg-6 search-gr'
        first_product_row.style.visibility = 'visible';
        first_product_title.textContent = d.title;
        first_product_img.src = d.image;
        first_product_gpu.textContent = d.gpu;
        first_product_price.textContent = d.price + ' ლ';
    });;

};