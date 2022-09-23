from ast import arg
from tracemalloc import start
from flask import Flask
from flask_restful import Resource, Api, reqparse
import datetime
from connDB import ConnDB

app = Flask(__name__)
api = Api(app)
conndb = ConnDB()

class myApiTool():
    @staticmethod
    def eval_datetime(time:str) -> datetime.datetime:
        try:
            return datetime.datetime.fromisoformat(time)
        except Exception as e:
            return False


class WordsFreq(Resource, myApiTool):
    def __init__(self):
        super().__init__()
        self.input_args = reqparse.RequestParser()
        self.input_args.add_argument("start_time", type=str, help="Start time of request", location='json', required=True)
        self.input_args.add_argument("end_time", type=str, help="End time of request", location='json', required=True)
        self.input_args.add_argument("screen_name", type=str, help="The screen name", location='json', required=True)
        self.input_args.add_argument("choice", type=list, help="what info you want", location='json')

    def get(self):
        args = self.input_args.parse_args()
        start_time = self.eval_datetime(args['start_time'])
        end_time = self.eval_datetime(args['end_time'])

        return conndb.getFreq(start_time, end_time, args['screen_name'], args['choice'])

    def post(self):
        args = self.input_args.parse_args()
        return args



api.add_resource(WordsFreq, "/api/wf/")


if __name__ == '__main__':
    app.run(debug=True)
