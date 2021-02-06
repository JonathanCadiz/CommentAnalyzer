from flask import Flask, jsonify, request
from flask_cors import CORS

import comments
import language_processing as lp

import json

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

with open('api.json') as f:
    data = json.load(f)

api_key = data['api_key']


@app.route('/ping', methods=['GET', 'POST'])
def ping_pong():
    if request.method == "POST":
        response_object = {'status': 'success'}
        post_data = request.get_json()
        url = post_data.get('url')
        key = post_data.get('key')
        new_request = comments.VideoRequest(url, api_key)
        new_request.request_comments()

        for comment in new_request.all_comments:
            print(comment.text)

        processed = lp.LanguageProcessing(new_request.all_comments)
        processed.add_unwanted(["video"])
        processed.extract_keywords()
        new_dict = {
            "words": processed.words,
            "nouns": processed.nouns,
            "adjectives": processed.adj,
            "verbs": processed.verbs,
            "links": processed.links
        }
        response_object['data'] = new_dict
        print(response_object)
        return jsonify(response_object)
    else:
        return jsonify("yes")
        


if __name__ == '__main__':
    app.run()