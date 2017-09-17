from flask_restful import Resource, reqparse
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAnalysis(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = SentimentAnalisys.parser.parse_args()
        text = data['text']
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(text)
        pass
