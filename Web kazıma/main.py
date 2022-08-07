import requests
import json
from flask import Flask, render_template, jsonify, make_response, Response, request
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

similar_words_frequency = {}
words_total_dict_1 = {}
similar_words_frequency_dict = {}
similar_words_frequency_dict_3 = {}
similar_words_frequency_dict_4 = {}
similar_words_frequency_dict_5 = {}
words_common_dict_1 = {}
words_common_dict_2 = {}

# URL_1 = 'http://www.scholarpedia.org/article/Main_Page'
# URL_2 = 'https://en.wikipedia.org/wiki/Main_Page'
# URL_3 = 'https://en.wikipedia.org/wiki/March_2021_Australian_floods'
# URL_4 = 'https://en.wikipedia.org/wiki/2021_Suez_Canal_obstruction'
# URL_5 = 'https://en.wikipedia.org/wiki/Qingdao'

URL_1 = ''
URL_2 = ''
URL_3 = ''
URL_4 = ''
URL_5 = ''

score = 0.0
score3 = 0.0
score4 = 0.0
score5 = 0.0


def calculateEverything():
    global words_common_dict_1
    global words_common_dict_2

    words_common_dict_1 = {}
    words_common_dict_2 = {}
    words_common_dict_3 = {}
    words_common_dict_4 = {}
    words_common_dict_5 = {}
    words_total_dict_2 = {}
    MOST_COMMON_AMOUNT = 5

    # Calculate first page
    r = requests.get(URL_1)
    soup = BeautifulSoup(r.content, 'html.parser')

    text_p_1 = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c_p_1 = Counter((x.rstrip(punctuation).lower() for y in text_p_1 for x in y.split()))

    total_words_1 = c_p_1

    common_1 = total_words_1.most_common(MOST_COMMON_AMOUNT)

    # Calculate second page
    r = requests.get(URL_2)
    soup = BeautifulSoup(r.content, 'html.parser')

    text_p_2 = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c_p_2 = Counter((x.rstrip(punctuation).lower() for y in text_p_2 for x in y.split()))

    total_words_2 = c_p_2

    common_2 = total_words_2.most_common(MOST_COMMON_AMOUNT)

    # Calculate first subdomain
    r = requests.get(URL_3)
    soup = BeautifulSoup(r.content, 'html.parser')

    text_p_3 = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c_p_3 = Counter((x.rstrip(punctuation).lower() for y in text_p_3 for x in y.split()))

    total_words_3 = c_p_3

    common_3 = total_words_3.most_common(MOST_COMMON_AMOUNT)

    # Calculate second subdomain
    r = requests.get(URL_4)
    soup = BeautifulSoup(r.content, 'html.parser')

    text_p_4 = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c_p_4 = Counter((x.rstrip(punctuation).lower() for y in text_p_4 for x in y.split()))

    total_words_4 = c_p_4

    common_4 = total_words_4.most_common(MOST_COMMON_AMOUNT)

    # Calculate third subdomain
    r = requests.get(URL_5)
    soup = BeautifulSoup(r.content, 'html.parser')

    text_p_5 = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c_p_5 = Counter((x.rstrip(punctuation).lower() for y in text_p_5 for x in y.split()))

    total_words_5 = c_p_5

    common_5 = total_words_5.most_common(MOST_COMMON_AMOUNT)

    # Generate dict for common words
    for value in common_1:
        words_common_dict_1[value[0]] = value[1]

    for value in common_2:
        words_common_dict_2[value[0]] = value[1]

    for value in common_3:
        words_common_dict_3[value[0]] = value[1]

    for value in common_4:
        words_common_dict_4[value[0]] = value[1]

    for value in common_5:
        words_common_dict_5[value[0]] = value[1]

    global words_total_dict_1
    words_total_dict_1 = dict(total_words_1)
    words_total_dict_2 = dict(total_words_2)

    similar_words = set(words_common_dict_1.keys()).intersection(words_common_dict_2.keys())
    # similar_words_frequency = {}

    for word in similar_words:
        similar_words_frequency[word] = words_common_dict_2[word]

    similar_words_3 = set(words_common_dict_1.keys()).intersection(words_common_dict_3.keys())
    similar_words_frequency_3 = {}

    for word in similar_words_3:
        similar_words_frequency_3[word] = words_common_dict_3[word]

    similar_words_4 = set(words_common_dict_1.keys()).intersection(words_common_dict_4.keys())
    similar_words_frequency_4 = {}

    for word in similar_words_4:
        similar_words_frequency_4[word] = words_common_dict_4[word]

    similar_words_5 = set(words_common_dict_1.keys()).intersection(words_common_dict_5.keys())
    similar_words_frequency_5 = {}

    for word in similar_words_5:
        similar_words_frequency_5[word] = words_common_dict_5[word]

    global similar_words_frequency_dict
    global similar_words_frequency_dict_3
    global similar_words_frequency_dict_4
    global similar_words_frequency_dict_5

    similar_words_frequency_dict = dict(similar_words_frequency)
    similar_words_frequency_dict_3 = dict(similar_words_frequency_3)
    similar_words_frequency_dict_4 = dict(similar_words_frequency_4)
    similar_words_frequency_dict_5 = dict(similar_words_frequency_5)

    # Find total of similar words freq
    total = 0.0
    total3 = 0.0
    total4 = 0.0
    total5 = 0.0

    for word in similar_words_frequency:
        total += similar_words_frequency[word]

    for word in similar_words_frequency_3:
        total3 += similar_words_frequency_3[word]

    for word in similar_words_frequency_4:
        total4 += similar_words_frequency_4[word]

    for word in similar_words_frequency_5:
        total5 += similar_words_frequency_5[word]

    # CALCULATE SCORE
    # Divide by amont of words

    global score
    global score3
    global score4
    global score5

    score = total / len(similar_words_frequency)
    score3 = total3 / len(similar_words_frequency_3)
    score4 = total4 / len(similar_words_frequency_4)
    score5 = total5 / len(similar_words_frequency_5)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get_url():
    global URL_1
    global URL_2
    global URL_3
    global URL_4
    global URL_5

    URL_1 = request.form['text']
    URL_2 = request.form['text2']
    URL_3 = request.form['text3']
    URL_4 = request.form['text4']
    URL_5 = request.form['text5']

    calculateEverything()

    return asama1()


@app.route('/asama1', methods=['GET', 'POST'])
def asama1():
    data = words_total_dict_1
    resp = json.dumps(data, indent=2, sort_keys=True)
    return render_template('asama1.html', data=resp)


@app.route('/asama2', methods=['GET', 'POST'])
def asama2():
    data = similar_words_frequency_dict
    resp = json.dumps(data, indent=2, sort_keys=True)
    return render_template('asama2.html', data=resp, n=len(data))


@app.route('/asama3', methods=['GET', 'POST'])
def asama3():
    data1 = words_common_dict_1
    resp1 = json.dumps(data1, indent=2, sort_keys=True)
    data2 = words_common_dict_2
    resp2 = json.dumps(data2, indent=2, sort_keys=True)
    data3 = similar_words_frequency_dict
    resp3 = json.dumps(data3, indent=2, sort_keys=True)
    data4 = score
    resp4 = json.dumps(data4, indent=2, sort_keys=True)
    return render_template('asama3.html', data1=resp1, data2=resp2, data3=resp3, data4=resp4)


@app.route('/asama4', methods=['GET', 'POST'])
def asama4():
    key_value = {"Ana": score, "1. Alt": score3, "2. Alt": score4, "3. Alt": score5}

    sortedDict = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))

    data1 = score
    data2 = score3
    data3 = score4
    data4 = score5
    data5 = URL_2
    data6 = URL_3
    data7 = URL_4
    data8 = URL_5
    data9 = similar_words_frequency_dict
    data10 = similar_words_frequency_dict_3
    data11 = similar_words_frequency_dict_4
    data12 = similar_words_frequency_dict_5

    resp1 = str(sortedDict[3][0]) + " URL: " + str(sortedDict[3][1])
    resp2 = str(sortedDict[2][0]) + " URL: " + str(sortedDict[2][1])
    resp3 = str(sortedDict[1][0]) + " URL: " + str(sortedDict[1][1])
    resp4 = str(sortedDict[0][0]) + " URL: " + str(sortedDict[0][1])
    resp5 = str(data5)
    resp6 = str(data6)
    resp7 = str(data7)
    resp8 = str(data8)
    resp9 = json.dumps(data9, indent=2, sort_keys=True)
    resp10 = json.dumps(data10, indent=2, sort_keys=True)
    resp11 = json.dumps(data11, indent=2, sort_keys=True)
    resp12 = json.dumps(data12, indent=2, sort_keys=True)

    return render_template('asama4.html', data1=resp1, data2=resp2, data3=resp3, data4=resp4, data5=resp5,
                           data6=resp6, data7=resp7, data8=resp8, data9=resp9, data10=resp10, data11=resp11,
                           data12=resp12, n1=str(len(data9)), n2=str(len(data10)), n3=str(len(data11)), n4=str(len(
            data12)))


app.run(host='0.0.0.0', port=5000, debug=True)
