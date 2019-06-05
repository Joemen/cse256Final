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

        #pred result
        loaded_model = pickle.load(open(filename, 'rb'))
        yp = loaded_model.predict(X)
        pred_proba = loaded_model.predict_proba(X)

        # words weights
        import string
        coefs = loaded_model.coef_[0]
        features = count_Vector.get_feature_names()
        punctuation = set(string.punctuation)
        word_score_list = {features[word_i]: coefs[word_i] for word_i in (X[0].nonzero()[1]) if
                           ' ' not in features[word_i]}
        proc_sentence = input.lower()
        for p in punctuation:
            proc_sentence = proc_sentence.replace(p, " ")
        words = proc_sentence.split(" ")
        for w in words:
            if w and w not in word_score_list:
                word_score_list[w] = 0.0
        word_score_list = sorted([(word_score_list[w], w) for w in word_score_list], reverse=True)
        plt.figure()
        plt.xticks(rotation=60)
        plt.bar([w for (_, w) in word_score_list], [sc for (sc, _) in word_score_list])
        plt.savefig('polls/static/word_weights.png')

        mglearn.tools.visualize_coefficients(loaded_model.coef_, feature_names, n_top_features=25)
        plt.savefig('polls/static/coefs.png')

        # word cloud
        frequency = {}
        for t in word_score_list:
            if abs(t[0]) < 1:
                frequency[t[1]] = 1.0
            else:
                frequency[t[1]] = abs(t[0])
        from wordcloud import WordCloud
        wordcloud = WordCloud(width=500, height=500, background_color="white").generate_from_frequencies(frequency)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig('polls/static/wordcloud.png')

        return yp, word_score_list, pred_proba


class SpamDetectionModel():

    def get_code(self, input):
        filename = 'finalized_model_spam.sav'
        data = []
        data.append(input)

        count_Vector = CountVectorizer(vocabulary=pickle.load(open("feature_spam.pkl", "rb")))
        X = count_Vector.transform(data)
        feature_names = count_Vector.get_feature_names()

        # pred result
        loaded_model = pickle.load(open(filename, 'rb'))
        yp = loaded_model.predict(X)
        pred_proba = loaded_model.predict_proba(X)

        #words weights
        import string
        coefs = loaded_model.coef_[0]
        features = count_Vector.get_feature_names()
        punctuation = set(string.punctuation)
        word_score_list = {features[word_i]: coefs[word_i] for word_i in (X[0].nonzero()[1]) if
                           ' ' not in features[word_i]}
        proc_sentence = input.lower()
        for p in punctuation:
            proc_sentence = proc_sentence.replace(p, " ")
        words = proc_sentence.split(" ")
        for w in words:
            if w and w not in word_score_list:
                word_score_list[w] = 0.0
        word_score_list = sorted([(word_score_list[w], w) for w in word_score_list], reverse=True)
        plt.figure()
        plt.xticks(rotation=60)
        plt.bar([w for (_, w) in word_score_list], [sc for (sc, _) in word_score_list])
        plt.savefig('polls/static/word_weights.png')

        #word cloud
        frequency = {}
        for t in word_score_list:
            if abs(t[0]) < 1:
                frequency[t[1]] = 1.0
            else:
                frequency[t[1]] = abs(t[0])
        from wordcloud import WordCloud
        wordcloud = WordCloud(width=500, height=500, background_color= "white").generate_from_frequencies(frequency)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig('polls/static/wordcloud.png')

        mglearn.tools.visualize_coefficients(loaded_model.coef_, feature_names, n_top_features=25)
        plt.savefig('polls/static/coefs.png')

        return yp, word_score_list, pred_proba