const send_url = () => {
    let url = document.querySelector('.c-form__input').value;
    console.log(url);
}
document.querySelector('.c-form__button').addEventListener('click', send_url)