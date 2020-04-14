#Exercise: Create a sigmoid function
def sigmoid(x): 
    """Given a 1-D array, calculate the signoid values.
    Return an np array"""
    return 1./(1.+np.exp(-x))