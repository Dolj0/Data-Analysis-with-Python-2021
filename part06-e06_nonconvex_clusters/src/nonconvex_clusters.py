#!/usr/bin/env python3

from itertools import permutations
import scipy
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():

    df = pd.read_csv("src/data.tsv", sep = '\t')
    X = df[['X1','X2']].to_numpy()
    y = df.iloc[:, -1]
    y2 = df[['y']].to_numpy()

    #lenth of label set
    y_len = len(set(y))

    eps_vals = np.arange(0.05, 0.2, 0.05)

    return_list = []

    for value in eps_vals:

        #create model
        model = DBSCAN(eps = value)
        model.fit(X)

        #number of clusters
        outliers = 0
        clusters = len(set(model.labels_))

        #remove outliers from clusters and increment outliers count
        if -1 in model.labels_:
            clusters = clusters -1
            outliers = list(model.labels_).count(-1)

        #find permuations
        permutation = find_permutation(clusters, y, model.labels_)
        new_labels = pd.DataFrame([permutation[label] for label in model.labels_]).iloc[:,0]

        #create mask to remove outliers from dataset
        outliers_mask = model.labels_ == -1

        #If the number of labels does not equal number of clusters then accuracy is 0
        if y_len != clusters:
            acc = None
        else:
            acc = accuracy_score(y2[~outliers_mask], new_labels[~outliers_mask])

        return_list.append([value, acc, clusters, outliers])

    return_df = pd.DataFrame(return_list, columns=['eps','Score','Clusters','Outliers'], dtype=float)

    return return_df

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
