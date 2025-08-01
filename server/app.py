from flask import Flask;

def initApp() -> Flask:
  app : Flask = Flask(__name__)
  return app

def setupRoutes(app : Flask) -> None:
  
  @app.route('/')
  def home():
      return "Hello, Flask!"