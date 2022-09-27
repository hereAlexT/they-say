import os
import sys
from pathlib import Path

curPath = Path(os.path.abspath(os.path.dirname(__file__)))
newPath = str(curPath.parent.absolute())
print(newPath)
sys.path.append(newPath)

from flask import Flask, jsonify, request
from connDB import ConnDB
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
conndb = ConnDB()


@app.route('/api/wf', methods=['POST'])
def wordFreq():
    error = None
    if request.method == 'POST':
        args = request.json
        # valid the input
        if "start_time" in args and type(args['start_time']) == str \
                and "end_time" in args and type(args['end_time']) == str \
                and "screen_name" in args and type(args['screen_name']) == str \
                and "choice" in args and type(args['choice']) == list:

            res = conndb.get_freq(args['start_time'], args['end_time'], args['screen_name'], args['choice'])
            return jsonify(res), res['status']
        else:
            return "Wrong arg!", 400

    else:
        return "Wrong arg!", 400


@app.route('/api/basic', methods=['POST'])
def basic():
    args = request.json
    print(args, file=sys.stderr)
    if "arg" in args and type(args['arg']) == str:
        if args['arg'] == "get_search_auto_complete":
            res = conndb.get_available_users_on_db()
            return jsonify(res), res['status']

    return "Wrong arg!", 400


@app.route('/api', methods=['GET', 'POST'])
def index_api():
    return jsonify({"msg": "Stay hungry, stay foolish. - Steve Jobs"}), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({"msg": "Stay hungry, stay foolish. - Steve Jobs"}), 404



if __name__ == '__main__':
    # app.run(debug=True)
    app.run("0.0.0.0", port=8888)
