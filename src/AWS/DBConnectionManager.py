import pymongo
import sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class DBConnectionManager:
    def __init__(self, *args, **kwargs):
        self.client = None
        self.database = None
        self.test_collection = None
        self.permutation_collection = None
        self.api_response_collection = None
        self.username = 'daefa8f0e79d116a5c88efae5429385647fbfe916f6c9764845358187b41db1'
        self.password = '236ee49eafec34beff73bf82ae7e1166ba802335f52b23fbcf98a64dfd6d69ca'
        print("Connecting to client")
        self.client = self.connect()
        # print(self.client)
        print("Connecting to database")
        self.database = self.openDB('anagram')
        # print(self.database)
        print("Connecting to collections")
        self.permutation_collection = self.openPermutationCollection()
        self.api_response_collection = self.openResponsesCollection()
        # print(self.permutation_collection)
        # print(self.api_response_collection)
        print("Testing connection")
        try:
            if self.test_connection():
                print("Connection successful")
            else:
                print("Connection failed")
        except:
            print("Connection failed")


    def connect(self):
        if not self.client:
            return pymongo.MongoClient(f'mongodb://{self.username}:{self.password}@anagram-dev.cluster-chg4s8qsuoeo.us-west-2.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
            # return pymongo.MongoClient(f'mongodb://{self.username}:{self.password}@sample-cluster.node.us-east-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

    def openDB(self, db_name:str):
        if self.client != None:
            # return self.client[db_name]
            return self.client.anagram
        return None

    def openPermutationCollection(self):
        if self.database != None:
            # return self.database[collection_name]
            return self.database.permutations
        
    def openResponsesCollection(self):
        if self.database != None:
            # return self.database[collection_name]
            return self.database.api_responses

    def test_connection(self):
        if self.database != None:
            print("Creating Test Collection")
            self.test_collection = self.database.test_collection
            # print(self.test_collection)
            print("Inserting test document")
            post_id = self.test_collection.insert_one({"_id": "L411fm115rl148c", "test": "test"}).inserted_id
            print(post_id)
            print("Finding test document")
            x = self.test_collection.find_one({"_id": "L411fm115rl148c"})
            print(x)
            print("Deleting test document")
            self.test_collection.delete_one({"_id": "L411fm115rl148c"})
            print("Dropping test collection")
            self.test_collection.drop()
            return True
        
    def close_connection(self):
        self.client.close()

connection_manager = DBConnectionManager()