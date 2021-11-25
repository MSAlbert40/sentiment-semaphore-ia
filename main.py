from flask import Flask, request
from flask_cors import CORS, cross_origin
from connection_api.model import Model
import json
import operator

api = Flask(__name__)
api.config['CORS_HEADERS'] = 'Content-type'

cors = CORS(api, resources={r"/*": {"origins": "*"}})
model = None

@api.route('/api/sentiment-analysis', methods=['POST'])
@cross_origin()
def sentimentPredict():
    posData = request.data.decode("utf-8") 
    requestData = json.loads(posData)

    # Create body Request
    accountT = requestData['account_tweets']
    dateT = requestData['date_tweets']
    numberT = int(requestData['number_tweets'])

    model.getData(accountT, dateT, numberT)
    prediction = model.getPrediction()

    globalLabel = {'Positivo': 0, 'Negativo': 0, 'Neutro': 0}
    details = []

    for index, text in enumerate(model.rawTexts):
        values = list(prediction[index])
        label = getLabel(values.index(max(values)))
        response = {}

        response['accurancy'] = str(round(max(values) * 100, 2)) + "%"
        response['date'] = model.rawDates[index]
        response['result'] = label
        response['text'] = text

        globalLabel[label] += 1
        details.append(response)

    maxLabel = max(globalLabel.items(), key = operator.itemgetter(1))[0]
    mean = getIndex(maxLabel)

    res = {"mean_text": maxLabel, "mean": mean, "details": details}
    return res


def getLabel(label):
    return 'Positivo' if label == 0 else ('Neutro' if label == 1 else 'Negativo')

def getIndex(index): 
    return 1 if index == 'Positivo' else (0 if index == 'Neutro' else -1)

if __name__ == "__main__":
    model = Model()
    api.run(host='localhost')