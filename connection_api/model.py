from tensorflow import keras
from keras.preprocessing.sequence import pad_sequences
from connection_api.twitter_api_data import getTweets
from training_model.utils import preprocessText
import tensorflow as tf
import numpy as np
import pandas as pd
import pickle

class Model:
    def __init__(self):

        self.model = keras.models.load_model('cnn_model_3')

        self.max_sequence_length = 50

        with open('tokenizer3.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        self.tokenizer = tokenizer
        self.rawDates = None
        self.rawTexts = None
        self.text = None

    def getData(self, account, date, number):
        getTweets(account, date, number)
        dataFrame = pd.read_csv('dataTweets.csv', encoding = 'utf-8')

        dataFrame['date'] = dataFrame['date'].apply(lambda x: str(x))
        self.rawDates = dataFrame['date'].tolist()

        dataFrame['text'] = dataFrame['text'].apply(lambda x: str(x))
        self.rawTexts = dataFrame['text'].tolist()

        dataFrame['text'] = dataFrame['text'].apply(lambda x: preprocessText(x))
        self.texts = dataFrame['text'].tolist()

    def getPrediction(self):
        data = self.tokenizer.texts_to_sequences(self.texts)
        data = pad_sequences(data, maxlen = self.max_sequence_length)

        prediction = self.model.predict(data)
        for index, p in enumerate(prediction): prediction[index] = [round(num, 3) for num in p]
        
        return prediction
