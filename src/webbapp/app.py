from flask import Flask, jsonify, make_response, request, abort, render_template
from db_manager import master_list
import time
import logging

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler('webapp_log.log')
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

app = Flask(__name__, static_folder="./static", template_folder="./static")

@app.route("/list")
def get_list():
    return "Master List:{}".format(master_list)
    #return render_template("index.html")

@app.route("/ping")
def hello():
    return "PONG"

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