from flask import Flask, jsonify, request
from flask_cors import CORS

import comments
import language_processing as lp
import video_info as vi

import json

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

with open('api.json') as f:
    data = json.load(f)

api_key = data['api_key']


@app.route('/videorequest', methods=['GET', 'POST'])
def ping_pong():
    if request.method == "POST":
        response_object = {'status': 'success'}
        post_data = request.get_json()
        url = post_data.get('url')
        new_request = comments.VideoRequest(url, api_key)
        new_request.request_comments()

        new_info_request = vi.VideoInfoRequest(url, api_key)
        new_info_request.request_info()
        info = {
            'publishedAt': new_info_request.publishedAt,
            'title': new_info_request.title,
            'thumbnail': new_info_request.thumbnail,
            'channel': new_info_request.channel,
            'tags': new_info_request.tags,
            'views': new_info_request.views,
            'likes': new_info_request.likes,
            'dislikes': new_info_request.dislikes,
            'commentCount': new_info_request.commentCount
        }

        processed = lp.LanguageProcessing(new_request.all_comments)
        processed.add_unwanted(["video"])
        processed.extract_keywords()
        new_dict = {
            "words": processed.words,
            "nouns": processed.nouns,
            "adjectives": processed.adj,
            "verbs": processed.verbs,
            "links": processed.links,
            "entities": processed.entities,
            "topComment": new_request.top_comment,
        }
        response_object['data'] = new_dict
        response_object['videoInfo'] = info
        print(processed.entities)
        return jsonify(response_object)
    else:
        return jsonify("yes")


if __name__ == '__main__':
    app.run()