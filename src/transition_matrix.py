import numpy as np

def build_matrix(df, states):
    index = {s:i for i,s in enumerate(states)}
    P = np.zeros((len(states), len(states)))

    for i in range(len(df)-1):
        s1 = df.iloc[i]["state"]
        s2 = df.iloc[i+1]["state"]
        P[index[s1], index[s2]] += 1

    P = P / P.sum(axis=1, keepdims=True)
    return P
