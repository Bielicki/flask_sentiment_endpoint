from flask import Flask
from flask_restful import Api
from resources.sentiment import SentimentAnalysis
from resources.language import Language
# from db import db

app = Flask(__name__)

app.secret_key = 'CcxU23e8f9WtwAGuNISewAw91WJWp-60TNCDfG6ws78'
api = Api(app)

api.add_resource(SentimentAnalysis, '/sentiment')
api.add_resource(Language, '/language')

if __name__ == '__main__':
    # db.init_app(app)
    app.run(port=5000, debug=True)
