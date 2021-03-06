import flask
from flask import request, jsonify
from flask_cors import CORS
import re


def load_words(fname):
    with open(fname) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


app = flask.Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to Wordle Solver API!"


@app.route('/', methods=['POST'])
def search():
    request_data = request.get_json()

    first = request_data['first'].lower()
    second = request_data['second'].lower()
    third = request_data['third'].lower()
    fourth = request_data['fourth'].lower()
    fifth = request_data['fifth'].lower()
    includeList = request_data['includeList']
    excludeList = request_data['excludeList']

    words = load_words('words_5.txt')
    req = ''
    include = []
    exclude = []
    result = []

    if first != '':
        req += first
    else:
        req += '.'
    if second != '':
        req += second
    else:
        req += '.'
    if third != '':
        req += third
    else:
        req += '.'
    if fourth != '':
        req += fourth
    else:
        req += '.'
    if fifth != '':
        req += fifth
    else:
        req += '.'

    for w in includeList:
        include.append((w['letter'].lower(), w['position']))

    for i in excludeList:
        exclude.append(i.lower())

    for word in words:
        if re.search(req, word):
            valid = True
            for i in include:
                if (i[0] not in word) or (word[i[1]] == i[0]):
                    valid = False
                    break
            if valid:
                for e in exclude:
                    if e in word:
                        valid = False
                        break
            if valid:
                result.append(word)

    return jsonify(result)
