import os
import sys
from pathlib import Path
curPath = Path(os.path.abspath(os.path.dirname(__file__)))
newPath = str(curPath.parent.parent.absolute())
print(newPath)
sys.path.append(newPath)

from flask import Flask
from flask_restful import Resource, Api, reqparse
from connDB import ConnDB


app = Flask(__name__)
api = Api(app)
conndb = ConnDB()


class myApiTool():
    @staticmethod
    def no_method(time: str):
        pass


class WordsFreq(Resource, myApiTool):
    def __init__(self):
        super().__init__()
        self.input_args = reqparse.RequestParser()
        self.input_args.add_argument("start_time", type=str, help="require start_time", location='json', required=True)
        self.input_args.add_argument("end_time", type=str, help="require end_time", location='json', required=True)
        self.input_args.add_argument("screen_name", type=str, help="require screen_time", location='json',
                                     required=True)
        self.input_args.add_argument("choice", type=list, help="require choice", location='json')

    def post(self):
        args = self.input_args.parse_args()
        res = conndb.get_freq(args['start_time'], args['end_time'], args['screen_name'], args['choice'])
        return res, res['status']


class Basic(Resource, myApiTool):
    def __init__(self):
        super().__init__()
        self.input_args = reqparse.RequestParser()
        self.input_args.add_argument("arg", type=str, help="arg required", location='json', required=True)

    def post(self):
        args = self.input_args.parse_args()
        if args['arg'] == "get_search_auto_complete":
            res = conndb.get_available_users_on_db()
            return res, res['status']


api.add_resource(WordsFreq, "/api/wf/")
api.add_resource(Basic, "/api/basic/")

if __name__ == '__main__':
    app.run(debug=True)
