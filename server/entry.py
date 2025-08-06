from app import initApp, setupRoutes
from flask import Flask, jsonify
from flask_cors import CORS
import r6statsapi

portNumber : int = 5000
frontEndUrl : str = "http://localhost:5173/"
app : Flask = initApp()
CORS(app, resources={r"/*": {"origins": frontEndUrl}})
setupRoutes(app)

if __name__ == "__main__":
    app.run(debug=True, port=portNumber)
