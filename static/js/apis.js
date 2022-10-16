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


let second_product_row = document.querySelector('.second-product-row');
let second_product_title = document.querySelector('.second-product-title .card-title');
let second_product_img = document.querySelector('.second-product-img img');
let second_product_gpu = document.querySelector('.second-product-gpu .card-subtitle');
let second_product_price = document.querySelector('.second-product-price .price');


const send_url = () => {
    let url_value = url.value
    if (!isValidURL(url_value)) {
        alert("Please enter a valid URL");
        return;
    };
    postData('/get-product/', { 'url': url_value }).then((data) => {
        d = data.data;
        console.log(data);
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
    postData('/search-product/', { 'price': first_product_price.textContent, 'gpu': first_product_gpu.textContent }).then((data) => {
        console.log(data);
        if (data.status == 'success') {
            second_product_row.style.visibility = 'visible';
            second_product_title.textContent = data.title;
            second_product_img.src = data.image;
            second_product_gpu.textContent = data.gpu;
            second_product_price.textContent = data.price + ' ლ';
        }
        else if (d.status == 'not_found') {
            console.log('Cannot find Cheaper Product')
        }
        else {
            console.log('Something went wrong');
        }
    });;

};