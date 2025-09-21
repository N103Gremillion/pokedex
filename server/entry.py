import os
from flask import Flask
from flask_cors import CORS
from pymongo.database import Database
from app import initApp, setupRoutes
from mongo.db_utils import getDb, setupCollections


port_number: int = int(os.environ.get("PORT", 5000))
flask_env: str = os.environ.get("FLASK_ENV", "development")  # 'development' or 'production'

# Frontend URL for CORS
# Production: use deployed frontend URL
# Development: allow localhost & 127.0.0.1
if flask_env == "production":
	frontend_url = os.environ.get("FRONTEND_URL") 
	if not frontend_url:
		raise ValueError("FRONTEND_URL must be set in production environment")
	CORS_ORIGINS = [frontend_url.rstrip('/')]
else:
	# allow localhost and 127.0.0.1 in development
	CORS_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"]

app: Flask = initApp()
CORS(app, origins=CORS_ORIGINS)

# Setup routes
setupRoutes(app)

globalDb: Database = getDb()
setupCollections(globalDb)


if __name__ == "__main__":
	if flask_env == "production":
		# Production: listen on 0.0.0.0 and platform-provided PORT
		app.run(host="0.0.0.0", port=port_number)
	else:
		# Development: run locally on localhost
		app.run(host="localhost", port=port_number, debug=True)
