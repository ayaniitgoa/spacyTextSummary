from flask import Flask, request, jsonify
from spacyModel import text_summarizer
from readTime import readingTime
from getUrltext import geturlText



app = Flask(__name__)

text = [[]]
urltext=[[]]


@app.route('/', methods=['GET'])
def get():
    return {'text': text}


@app.route('/', methods=['POST'])
def post():

    gottext = request.get_json()
    gottext = str(gottext)
    gottext.strip()
    finaltext = text_summarizer(gottext)
    readTime=readingTime(gottext)
    text.append([finaltext, readTime])
    # print(finaltext)

    return {'text': text}

@app.route('/texturl', methods=['GET'])
def getUrl():
    return {'urltext': urltext}

@app.route('/texturl', methods=['POST'])
def postUrl():
    goturl=request.get_json()
    # print(goturl)
    finaltext=geturlText(goturl)
    readTime=readingTime(finaltext)
    urltext.append([finaltext, readTime])
    return {'urltext': urltext}

if __name__ == '__main__':
    app.run(debug=True)
