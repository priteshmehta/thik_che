import time
import logging
from flask import Flask, jsonify, make_response, request, abort, render_template

import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', '')))

from db_manager import master_list
from cache_manager import CacheManager

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler('webapp_log.log')
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

app = Flask(__name__, static_folder="./static", template_folder="./static")
ch = CacheManager()

@app.route("/list")
def get_list():
    return "Master List:{}".format(master_list)
    #return render_template("index.html")

@app.route("/ping")
def hello():
    return "PONG"

@app.route("/mylist")
def get_my_list():
    items = ch.get_list_items("mylist")
    unique_items = set(items)
    return str(unique_items)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

'''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
'''