from app import initApp, setupRoutes
from flask import Flask
from flask_cors import CORS
from pymongo.database import Database
from mongo.db_utils import getDb, setupCollections

# Configs
portNumber : int = 5000
frontEndUrl : str = "http://localhost:5173/"

# Flask app Initalization
app : Flask = initApp()
CORS(app)
setupRoutes(app)

# database Initialization
globalDb : Database = getDb()
setupCollections(globalDb)

if __name__ == "__main__":
    app.run(debug=True, port=portNumber)
