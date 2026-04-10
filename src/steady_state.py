import numpy as np

def steady_state(P):
    eigvals, eigvecs = np.linalg.eig(P.T)
    vec = eigvecs[:, np.isclose(eigvals, 1)][:,0].real
    return vec / vec.sum()
