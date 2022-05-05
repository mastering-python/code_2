# The common shorthand for statsmodels is sm

>>> import statsmodels.api as sm
>>> import numpy as np

>>> Y = np.arange(8)
>>> X = np.ones(8)

# Create the weighted-least-squares model

>>> model = sm.WLS(Y, X)

# Fit the model and generate the regression results

>>> fit = model.fit()

# Show the estimated parameters and the t-values:

>>> fit.params
array([3.5])
>>> fit.tvalues
array([4.04145188])
