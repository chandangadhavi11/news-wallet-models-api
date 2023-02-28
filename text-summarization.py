import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from flask import Flask, jsonify, request
from flask_cors import cross_origin
import json

psudotext = """India (Hindi: Bhārat), officially the Republic of India (Hindi: Bhārat Gaṇarājya) and also known as Hindustan within the country, is a country in South Asia. It is second largest country by number of people and seventh largest country by land area. It also has the most people of any democracy in the world.[9][10] India is a peninsula, bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast. It has six neighbors: Pakistan in the north-west, China, Nepal, and Bhutan in the north, and Bangladesh and Myanmar in the east. Sri Lanka is nearby to the south.
    The capital of India is New Delhi. India has the second largest military force in the world and is also a nuclear weapon state.[11] India's economy became the world's fastest growing in the G20 developing nations during 2014, replacing the People's Republic of China.[12] India's literacy and wealth are also rising.[13] According to New World Wealth, India is the fifth richest country in the world with a total individual wealth of $5.6 trillion.[14][15] However, it still has many social and economic issues like poverty and corruption. India is a founding member of the World Trade Organisation (WTO), and has signed the Kyoto Protocol.
    India has the fourth largest number of spoken languages per country in the world, only behind Papua New Guinea, Indonesia, and Nigeria.[16] People of many different religions live there, including the five most popular world religions: Hinduism, Buddhism, Sikhism, Islam, and Christianity. The first three religions originated from the Indian subcontinent along with Jainism."""
stopwords = set(stopwords.words('english'))


def text_summerization_model(text):

    words = word_tokenize(text)
    freqTable = dict()

    sentences = sent_tokenize(text)
    sentenceValue = dict()

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
        average = int(sumValues / len(sentenceValue))

    for word in words:
        word = word.lower()
        if word in stopwords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    average = int(sumValues / len(sentenceValue))

    summary = ""
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    return (summary)


app = Flask(__name__)
@app.route('/api/text-summerization-model/', methods=['POST'])
@cross_origin()
def home():
    if (request.method == 'POST'):
        request_data = json.loads(request.data)
        text = str(request_data["rawData"])
        return jsonify({'data': text_summerization_model(text)})
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)