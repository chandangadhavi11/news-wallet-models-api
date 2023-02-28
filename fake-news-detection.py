import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from flask import Flask, jsonify, request
from flask_cors import cross_origin
import json



#Read the data
df=pd.read_csv("data/news.csv")
labels=df.label

x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# DataFlair - Fit and transform train set, transform test set



tfidf_train = tfidf_vectorizer.fit_transform(x_train)


#DataFlair - Initialize a PassiveAggressiveClassifier
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)



app = Flask(__name__)
@app.route('/api/fake-news-detection/', methods=['POST'])
@cross_origin()
def home():
    C_data = [f"""${request.data}"""]
    # Create the pandas DataFrame with column name is provided explicitly
    c = pd.DataFrame(C_data, columns=['text'])
    tfidf_test = tfidf_vectorizer.transform(c["text"])

    # print(pac.predict(tfidf_test))
    return {'data': str(pac.predict(tfidf_test)[0])}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)