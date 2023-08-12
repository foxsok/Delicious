from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://davidpaez662:baseAtlas@pruebaapi.x6crczp.mongodb.net/"
conn = MongoClient(uri, server_api=ServerApi('1'))
