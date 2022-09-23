
from data_preparation.data_processing.TweetProcessingEngine import TweetProcessingEngine
import datetime
import project_config as config

class ConnDB:
    def __init__(self):
        self.tpe = TweetProcessingEngine()

    def getFreq(self, start_time: datetime.datetime, end_time: datetime.datetime, screen_name: str, choice: list):
        if len(choice) == 0:
            choice = config.FREQ_CHOICE
        # look up userid
        id = self.tpe.get_user_id(screen_name=screen_name)
        if id is not None:
            return self.tpe.cal_freq(id, start_time, end_time, choice)
        else:
            return None


