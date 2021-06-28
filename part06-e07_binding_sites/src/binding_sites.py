#!/usr/bin/env python3

from hashlib import new
import pandas as pd
import numpy as np
import scipy
from scipy.spatial import distance
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def toint(x):
    if x == 'A':
        return 0
    elif x == 'C':
        return 1
    elif x == 'G':
        return 2
    elif x == 'T':
        return 3


def get_features_and_labels(filename):

    df = pd.read_csv(filename, sep='\t')
    X = df['X']
    X_toint = []
    for item in X:
        single_feature = []
        for letter in item:
            single_feature.append(toint(letter))
        X_toint.append(single_feature)

    X_return = np.array(X_toint)
    y = np.array(df['y'])

    return (X_return, y)

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    features, labels = get_features_and_labels(filename)
    distance = pairwise_distances(features, metric='euclidean')
    clustering = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='average').fit(features, labels) #
    y_predict = clustering.labels_ #
    permutation = find_permutation(2, labels, y_predict) #
    new_labels = [permutation[label] for label in y_predict] #
    score = accuracy_score(labels, new_labels)
    plot(distance)
    return score

def cluster_hamming(filename):
    features, labels = get_features_and_labels(filename)
    ham_dist = pairwise_distances(features, metric='hamming')
    clustering = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average').fit(ham_dist, labels)
    y_predict = clustering.labels_
    permutation = find_permutation(2, labels, y_predict)
    new_labels = [permutation[label] for label in y_predict] #
    score = accuracy_score(labels, new_labels)
    return score


def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
