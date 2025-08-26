from dotenv import load_dotenv, dotenv_values
import os
from pymongo import MongoClient

load_dotenv()

username : str = os.getenv('MONGO_DB_ATLAS_USER')
password : str = os.getenv('MONGO_DB_ATLAS_PASSWORD')
clusterId : str = os.getenv('MONGO_DB_ATLAS_Cluster')
appName : str = os.getenv('MONGO_DB_ATLAS_App_Name')
dbName : str = os.getenv('MONGO_DB_ATLAS_DB_Name')

if not all([username, password, clusterId, dbName]):
    raise ValueError("One or more required environment variables are missing.")

dBconnectionString : str = f"mongodb+srv://{username}:{password}@{clusterId}/?retryWrites=true&w=majority&appName={appName}"

client = MongoClient(dBconnectionString)
db = client[dbName]

print(db.list_collection_names())  