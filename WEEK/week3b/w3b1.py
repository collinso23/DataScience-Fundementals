def sigmoidfor(x):
    f = np.array([])
    for xi in x:
        fi = 1. / (1. + np.exp(-xi))
        f = np.append(f, fi)
    return f