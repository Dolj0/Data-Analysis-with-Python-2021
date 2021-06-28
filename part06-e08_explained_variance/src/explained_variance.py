#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def explained_variance():
    X = pd.read_csv("src/data.tsv", sep="\t")
    varience = X.var(axis=0)

    pca = PCA()
    pca.fit(X)
    explained_varience=pca.explained_variance_

    return varience, explained_varience

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    v_string = " ".join([f"{i:.3f}" for i in v])
    ev_string = " ".join([f"{i:.3f}" for i in ev])

    print(f"The variances are: {v_string}")
    print(f"The explained variances after PCA are: {ev_string}")

    plt.plot(np.arange(1, 11), np.cumsum(ev))
    plt.show()


if __name__ == "__main__":
    main()
