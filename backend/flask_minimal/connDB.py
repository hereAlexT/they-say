from data_preparation.data_processing.TweetProcessingEngine import TweetProcessingEngine
from data_preparation.data_collection.TweetCollectionEngine import TweetCollectionEngine
import datetime
import project_config as config
import sys
import dateutil.parser


class ConnDB:
    def __init__(self):
        self.tpe = TweetProcessingEngine()
        self.tce = TweetCollectionEngine()

    @staticmethod
    def eval_datetime(time: str):
        try:
            return dateutil.parser.isoparse(time)
        except Exception as e:
            print(f"{time} is not isofromat time", file=sys.stderr)
            return None

    def get_freq(self, start_time, end_time, screen_name: str, choice: list):

        start_time = self.eval_datetime(start_time)
        end_time = self.eval_datetime(end_time)

        if start_time is None or end_time is None:
            return {'status': 400, 'msg': "invlaid time"}

        if len(choice) == 0:
            choice = config.FREQ_CHOICE

        # look up userid
        userid = self.tpe.get_user_id(screen_name=screen_name)
        if userid is not None:
            if self.tpe.is_user_in_db(userid=userid) is False:
                return {'status': 404, "msg": "We don't have the data of request twitter account", 'data': {}}
            return {
                'status': 200,
                'msg': "Data attached",
                'data': self.tpe.cal_freq(userid, start_time, end_time, choice)
            }

        else:
            return {
                'status': 400,
                'msg': "given username is invalid",
                'data': []
            }

    def get_available_users_on_db(self):
        """
        :return: {"screen_name": []}
        """
        res = self.tce.get_distinct_user_profile_on_db()
        return {
            'status': 200,
            'msg': "distinct user profiles that you can check",
            'data': res
        }


