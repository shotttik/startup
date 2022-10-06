from flask import Flask, render_template, request
import re
from automation.config import config_browser
from automation.webdriver import Browser
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search/', methods=['POST'])
def search():
    json_data = request.json

    if not json_data:
        return {"Error": "Json Data is empty"}

    url = json_data.get('url', None)
    if url is None:
        return {"Error": "Json URL is empty"}

    websites = ['https://alta.ge/',
                'https://zoommer.ge/',
                'https://ultra.ge/']

    supported_website = None
    for website in websites:
        if url.startswith(website):
            supported_website = website
            break

    if not supported_website:
        return {"Error": "Sorry, our program doesn't support that website"}

    domain = re.findall('://([\w\-\.]+).ge', supported_website)[0]
    browser_i = Browser(config_browser(), url)
    browser_i.quit()
    return {'domain': domain}
