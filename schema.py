from pymongo import MongoClient
import os
from dotenv import load_dotenv
# Connect to MongoDB (Update with your MongoDB URI)
load_dotenv()
MongoDB_URL = os.getenv('MONGODB_URL')
client = MongoClient(MongoDB_URL)
db = client["Blog"]  # database name
authors_collection = db["authors"]  # collection name

def get_recommendation_dict():
    recommendation_dict = {}
    
    # Fetch only email and followers fields
    authors = authors_collection.find({}, {"email": 1, "following": 1, "_id": 0})

    for author in authors:
        recommendation_dict[author["email"]] = author.get("following", [])  # Default to empty list if no followers

    return recommendation_dict


if __name__ =='__main__':

    # Execute the function and print the result
    recommendation_dict = get_recommendation_dict()
    print(recommendation_dict)

    # Example output format:
    {
        'yugeshkaran01@gmail.com':
          ['kumaranv.set2022@dsuniversity.ac.in', 'ssibi3290@gmail.com', 
           'rosiniisuresh@gmail.com', 'haricharanuggirala1133@gmail.com', 
           '21aid060@dsuniversity.ac.in'],

        'ssibi3290@gmail.com': [], 
        
        'haricharanuggirala1133@gmail.com': ['pradeepshiyam1314@gmail.com'], 

        'ajayvarsan2020@gmail.com': [], 

        'yugeshkaran001@gmail.com': 
           ['haricharanuggirala1133@gmail.com', 'yugeshkaran01@gmail.com', '21aid060@dsuniversity.ac.in'], 
        
        'rosiniisuresh@gmail.com': [], 
        
        'rosiniis.set2022@dsuniversity.ac.in': [], 
        
        'kumaranv.set2022@dsuniversity.ac.in':
           ['yugeshkaran01@gmail.com', 'yugeshkaran01@gmail.com', 'pradeepshiyam1314@gmail.com'], 
           
        '21aid145@dsuniversity.ac.in': [], 
        
        '21aid060@dsuniversity.ac.in': ['ssibi3290@gmail.com']

        }
