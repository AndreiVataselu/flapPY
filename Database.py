import pymongo


class Database:

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.database = self.client["database"]
        self.high_scores = self.database["highscore"]

    def get_highscore(self):
        return self.high_scores.find_one()["highscore"]

    def exists(self):
        return not self.high_scores.index_information() == {}

    def update_highscore(self, current_highscore):
        self.high_scores.update_one(self.high_scores.find_one(),
                                    {'$set' : {
                                        "highscore" : current_highscore
                                    }})

    def insert_highscore(self, score):
        self.high_scores.insert_one({'highscore' : score})

