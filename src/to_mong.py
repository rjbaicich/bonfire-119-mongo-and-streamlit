# Import statements
from base import Base
from dotenv import load_dotenv
import pymongo
import os

# Class definition
class ToMongo(Base):
    '''
    Designed as a class to transport data from the Base class to a MongoDB instance.
    Initializes an instance of the inherited class
    Defined methods are as follows:

    upload_one_by_one: Uploads pieces of information one by one to a database over an iterable structure

    upload_collection: uploads an entire document of items to MongoDB

    delete_collection: drops an entire collection of data
    '''

    def __init__(self):
        # Initialize the instance of our inherited class:
        Base.__init__(self)
        # Load in the env variables
        load_dotenv()
        self.mongo_url = os.getenv('MONGO_URL')
        # Connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)
        # Create a database
        self.db = self.client.db
        # Create a collection
        self.cards = self.db.cards
        # Set dataframe index to the id column:
        self.df.set_index('id', inplace=True)
    
    def upload_collection(self):
        '''
        Upload an entire collection of items to MongoDB.
        BEWARE: there is a maximum size to the upload
        Limitations to the amount of data you can upload at once.
        '''
        self.cards.insert_many([self.df.to_dict()])
    
    def upload_one_by_one(self):
        ''' Uploads items to MongoDB one-by-one. This method takes longer, but ensures all data is uploaded properly'''
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())
            
    def delete_collection(self, collection_name):
        ''' Drop a collection'''
        self.db.drop_collection(collection_name)


if __name__ == '__main__':
    c = ToMongo()
    print('Successful connection to client object')
    c.upload_one_by_one()
    print('Cards have been successfully uploaded to Mongo Instance')
    # c.delete_collection('cards')
    # print('Collection has been successfully deleted')