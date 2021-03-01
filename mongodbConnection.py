'''
Connection data to MongoDB using pymongo lib
'''
import os
from pymongo import MongoClient

def connect_mongo(data, collection, content):
    # Making Connection 
    myclient = MongoClient("mongodb://localhost:27017/")
    
    # database  
    db = myclient[data] 

    # Created or Switched to collection  
    Collection = db[collection] 
 
    # Inserting the loaded data in the Collection 
    # if JSON contains data more than one entry 
    # insert_many is used else inser_one is used 
    if isinstance(content, list): 
        Collection.insert_many(content)   
    else: 
        Collection.insert_one(content) 

    myclient.close()
    
if __name__ == "__main__":
    connect_mongo()
