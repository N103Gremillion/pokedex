from app import initApp, setupRoutes
from flask import Flask, jsonify
import r6statsapi

portNumber : int = 5000
app : Flask = initApp()
setupRoutes(app)

if __name__ == "__main__":
    app.run(debug=True, port=portNumber)
