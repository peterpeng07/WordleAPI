import flask
from flask import request


def load_words(fname):
    with open(fname) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    request_data = request.get_json()

    first = request_data['first']
    second = request_data['second']
    third = request_data['third']
    fourth = request_data['fourth']
    fifth = request_data['fifth']
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
        include.append((w['letter'], w['position']))

    for i in excludeList:
        exclude.append(i)

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

    return result

    # '''
    #       req: {}
    #       include: {}
    #       exclude: {}
    # '''.format(req, include, exclude)

 # 1: {}
    # 2: {}
    # 3: {}
    # 4: {}
    # 5: {}
