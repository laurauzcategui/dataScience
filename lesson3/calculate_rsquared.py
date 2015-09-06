import numpy as np
from scipy import stats

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced
    # predictions.
    #
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE

    mean_p = np.mean(data) # mean of observations

    sse = np.sum((data-predictions)**2) #sum squared error
    sst = np.sum((data-mean_p)**2) # total sum of squares

    r_squared = 1 - ( sse / sst )

    return r_squared
