from flask import Flask
from flask_restful import Api

from Resources.sentiment import SentimentAnalysis

# from db import db

app = Flask(__name__)

# genereted for dev purposes with secrets.token_urlsafe
app.secret_key = 'CcxU23e8f9WtwAGuNISewAw91WJWp-60TNCDfG6ws78'
api = Api(app)

api.add_resource(SentimentAnalysis, '/')


if __name__ == '__main__':
    # db.init_app(app)
    app.run(port=5000, debug=True)
