from pymongo import MongoClient

# Connect to MongoDB (Update with your MongoDB URI)
client = MongoClient('mongodb+srv://yugeshkaran01:GEMBkFW5Ny5wi4ox@blog.adtwl.mongodb.net/Blog-Data?retryWrites=true&w=majority&appName=blog')
db = client["Blog-Data"]  # Replace with your actual database name
authors_collection = db["authors"]  # Replace with your actual collection name

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
