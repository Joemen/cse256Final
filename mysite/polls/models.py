import pickle
from sklearn.feature_extraction.text import CountVectorizer
from pylab import *
import matplotlib.pyplot as plt, mpld3
import mglearn

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
        feature_names = count_Vector.get_feature_names()

        loaded_model = pickle.load(open(filename, 'rb'))
        yp = loaded_model.predict(X)

        mglearn.tools.visualize_coefficients(loaded_model.coef_, feature_names, n_top_features=25)
        plt.savefig('polls/static/freq.png')
        # Data for plotting

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