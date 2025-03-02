import time
from random import randint
import requests as requests
from flask import Flask, render_template

app = Flask(__name__)

def get_xkcd_image():
    comicid = randint(0,1000)
    response = requests.get(f'https://xkcd.com/{comicid}/info.0.json')
    return response.json()['img']

def get_multiple_images(number):
    return [get_xkcd_image() for _ in range(number)]

@app.get('/comic')
def hello():
    start = time.perf_counter()
    urls = get_multiple_images(10)
    end=time.perf_counter()
    return render_template('index.html',end=end,start=start,urls=urls)

if __name__ == '__main__':
    app.run(debug=True,port=5555)
