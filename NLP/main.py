import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)

corpus = []
for i in range(0, 1000):
    reviews = re.sub('[^a-zA-Z]', ' ', df['Review'][i])
    reviews = reviews.lower()
    reviews = reviews.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    reviews = [ps.stem(word) for word in reviews if not word in set(all_stopwords)]
    reviews = ' '.join(reviews)
    corpus.append(reviews)

cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = df['Liked']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_pred, y_test)
print(cm)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)