import numpy as np
def mean_var_std():
    n, m = list(map(int, input().split()))
    arr = np.array([input().split() for i in range(n)], dtype=int)
    print(np.mean(arr, axis=1))
    print(np.var(arr, axis=0))
    output = np.std(arr)
    print(output.round(12))
    return output.round(12)