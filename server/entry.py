import os
from flask import Flask
from flask_cors import CORS
from pymongo.database import Database
from app import initApp, setupRoutes
from mongo.db_utils import getDb, setupCollections


port_number: int = int(os.environ.get("PORT", 5000))
flask_env: str = os.environ.get("FLASK_ENV", "development")  # 'development' or 'production'

app: Flask = initApp()
CORS(app)

# Setup routes
setupRoutes(app)

globalDb: Database = getDb()
setupCollections(globalDb)


if __name__ == "__main__":
	if flask_env == "production":
		# Production: listen on 0.0.0.0 and platform-provided PORT
		app.run(host="0.0.0.0", port=5000)
	else:
		# Development: run locally on localhost
		app.run(host="localhost", port=5000, debug=True)
