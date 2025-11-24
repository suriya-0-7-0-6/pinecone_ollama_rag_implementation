import numpy as np

def l2_normalizer(vector):
    vector = np.array(vector)
    return (vector / (np.linalg.norm(vector) + 1e-10)).tolist()

def normalize_scores(values):
    arr = np.array(values, dtype=float)
    if len(arr) == 0:
        return []
    minv, maxv = arr.min(), arr.max()
    if maxv - minv <= 1e-12:
        return [1.0 for _ in arr]
    norm = (arr - minv) / (maxv - minv)
    return norm.tolist()