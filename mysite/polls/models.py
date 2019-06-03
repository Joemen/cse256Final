import pickle
from sklearn.feature_extraction.text import CountVectorizer
# read the django docs on models:
# https://docs.djangoproject.com/en/dev/topics/db/models/

# a model for an airport

class Airport():

    
    def get_id(self):
        return self.id

    def get_code(self, input):
        filename = 'finalized_model.sav'
        data = []
        data.append(input)

        count_Vector = CountVectorizer()
        X = count_Vector.fit_transform(data)



        loaded_model = pickle.load(open(filename, 'rb'))
        yp = loaded_model.predict(X)

        return yp
