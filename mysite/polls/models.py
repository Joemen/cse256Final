import pickle
from sklearn.feature_extraction.text import CountVectorizer
# read the django docs on models:
# https://docs.djangoproject.com/en/dev/topics/db/models/

# a model for an airport

class SentimentAnalysisModel():

    def get_code(self, input):
        filename = 'finalized_Sentiment_model.sav'
        data = []
        data.append(input)

        count_Vector = CountVectorizer(vocabulary=pickle.load(open("feature_Sentiment.pkl", "rb")))
        X = count_Vector.transform(data)

        loaded_model = pickle.load(open(filename, 'rb'))
        yp = loaded_model.predict(X)

        return yp
class SpamDetectionModel():

    def get_code(self, input):
        filename = 'finalized_Spam_model.sav'
        data = []
        data.append(input)

        count_Vector = CountVectorizer(vocabulary=pickle.load(open("feature_Spam.pkl", "rb")))
        X = count_Vector.transform(data)

        loaded_model = pickle.load(open(filename, 'rb'))
        yp = loaded_model.predict(X)

        return yp