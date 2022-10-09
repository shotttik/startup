from flask import Flask, render_template, request
import re
from automation.config import config_browser
from automation.webdriver import Browser
import importlib.util
import sys
import json
from automation.websites.sites import WEBSITES
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/get-product/', methods=['POST'])
def get_product():
    json_data = request.json

    if not json_data:
        return {"Error": "Json Data is empty"}

    url = json_data.get('url', None)
    if url is None:
        return {"Error": "Json URL is empty"}

    supported_website = None
    for website in WEBSITES:
        if url.startswith(website):
            supported_website = website
            break

    if not supported_website:
        return {"Error": "Sorry, our program doesn't support that website"}

    domain = re.findall('://([\w\-\.]+).ge', supported_website)[0]
    browser_i = Browser(config_browser(), url)

    pth = f'automation/websites/{domain}/parser.py'
    cls_name = 'Parse'
    spec = importlib.util.spec_from_file_location(cls_name, pth)
    foo = importlib.util.module_from_spec(spec)
    sys.modules[cls_name] = foo
    spec.loader.exec_module(foo)
    data = foo.Main().parser(html=browser_i.driver.page_source)

    browser_i.quit()
    return json.dumps({'data': data})


@app.route('/search-product/', methods=['POST'])
def search_product():
    json_data = request.json
