from flask_restful import Resource, reqparse
import requests


class Language(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = Language.parser.parse_args()
        text = data['text']

        params = {'access_key': '12525a4a8f71d1952ad454c2df7061cb', "query": text}
        languages = requests.get('http://apilayer.net/api/detect', params=params).json()

        if languages['success']:
            return languages
        else:
            return {"message": "Can't detect"}
