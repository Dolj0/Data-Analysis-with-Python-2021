#!/usr/bin/env python3

import gzip
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def read_files(fraction):
    ham_file = gzip.open("src/ham.txt.gz").readlines()
    ham_frac = int(fraction*len(ham_file))

    spam_file = gzip.open("src/spam.txt.gz").readlines()
    spam_frac = int(fraction*len(spam_file))
    
    ham = ham_file[:ham_frac]
    spam = spam_file[:spam_frac]

    return ham, spam
    

def spam_detection(random_state=0, fraction=1.0):
    ham, spam = read_files(fraction)

    #feature matrix is list starting with ham ending with spam
    feature_matrix = ham + spam

    #transform email list to word vector array
    #this x array form the predictor variables
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(feature_matrix).toarray()

    #create dependent variables array
    #create array of 0 with length equal to number of emails in total
    y =  np.zeros(len(feature_matrix))
    #labels all spam emails with 1
    y[len(ham):] = 1
    
    #randomly split data into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state, train_size=0.75)

    #create multinominal model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    #create one d array with what the model beleives is the classificiation for X_test values    
    y_fitted = model.predict(X_test)

    #compare y_fitted with y_test to see how accurate the algorithm is
    acc = accuracy_score(y_test, y_fitted)

    #number of incorrect spam/ham assignments
    misclassified = np.sum(y_test != y_fitted)

    return acc, len(X_test), misclassified


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
