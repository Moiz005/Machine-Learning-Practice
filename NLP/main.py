import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# re library is used for regular expressions for string manipulation
import re
# Natural Language Toolkit for text processing.
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
# PorterStemmer is used for converting a word into it's stem form by removing the pre and postfix
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB # Classifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Delimiter tells us about the seperation of the data file
# quoting=3 is used for ignoring quotes in the data file
df = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)

# corpus array stores the preprocessed text from which we have removed all the useless stuff
corpus = []
for i in range(0, 1000):
    #re.sub(a, b, text) method sunstitutes 'a' with 'b' in 'text'
    reviews = re.sub('[^a-zA-Z]', ' ', df['Review'][i])
    reviews = reviews.lower()
    reviews = reviews.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    reviews = [ps.stem(word) for word in reviews if not word in set(all_stopwords)]
    reviews = ' '.join(reviews)
    corpus.append(reviews)

# Implementing the bag of words model
# Reducing the total number of features so that less computational power is expended
# CountVectorizer(max_features=1500) Basically selects the most frequent 1500 words
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