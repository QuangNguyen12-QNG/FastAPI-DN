from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# db = client["DethiTN"]

# taode_collection = db["Taode"]

# def insert_exam(exam_data):
#     return taode_collection.insert_one(exam_data)
    