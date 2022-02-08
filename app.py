import flask
from flask import request

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

    return '''
          1: {}
          2: {}
          3: {}
          4: {}
          5: {}
          include: {}
          exclude: {}
    '''.format(first, second, third, fourth, fifth, includeList, excludeList)
