from base import Base
from dotenv import load_dotenv
import pymongo
import os

class ToMongo(Base):


    def __init__(self):
        Base.__init__(self)
        load_dotenv()
        self.mongo_url = os.getenv('MONGO_URL')
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client.db
        self.cards = self.db.cards
        self.df.set_index('id', inplace=True)

    def upload_collection(self):
        self.card.insert_many([self.df.to_dict()])

    def upload_one_by_one(self):
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())

    def delete_collection(self, collection_name):
        self.db.drop_collection(collection_name)
        
if __name__ == '__main__':
    c = ToMongo()
    print('Successful connection to client object')
    c.upload_one_by_one()
    print('Cards have been successfully run on Mongo instance')