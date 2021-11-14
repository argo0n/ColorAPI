from flask import Flask, send_file, request
from tqdm import tqdm
from PIL import Image
import os
import time
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def home_page():
    return "Hello!"

@app.route('/color/<color>')
def show_colow(color):
    try:
        num = int(color, base=16)
    except ValueError:
        return '<h1>You did not provide a proper hex.</h1>'
    if num < 0 or num > 16777215:
        return '<h1>You did not provide a proper hex.</h1>'
    im = Image.new(mode="RGB", size=(300, 300), color=num)
    img_byte_arr = BytesIO()
    im.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return send_file(img_byte_arr, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)