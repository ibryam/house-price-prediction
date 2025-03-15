# 1. Import all needed frameworks and libraries

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# 2. Load data and explore

data = pd.read_csv("housepricesdataset.csv",sep = ";")
print(data.head())
print(data.describe())

# 3. Declare dependencies/independencies

x = data[['area', 'roomcount', 'buildingage']]# this is independent variable or "feature"(input) in sklearn world. This we use to predict the target "y".
y = data['price'] # this is the dependent variable or "target"(output) in sklearn world. This is what we are trying to predict using "x".

# we can now proceed feeding them in our algo. sklearn takes full advantage of object-oriented capabilities of python such as Classes().
# we need to create an object or an instance of a given class. In this class we will create a "reg"

# 4. Create Linear Regression object

reg = LinearRegression() # now "reg" is an instance of the LinearRegression class.
# whats now left is to fit the regression.

# 5. Fit the model

reg.fit(x,y) # the order of the items is always first - input; and then target. (x,y). sklearn has different order vs statmodels.
# the result from above is something like
# LinearRegression(copy_x=True, fit_intercept=True, n_jobs=1, NORMALIZE=False)

# # ### STANDARDIZATION: the process of subtracting the mean and dividing by the standard deviation. ###
# # ### NORMALIZATION:  the process of subtracting the mean BUT divide by the L2-norm of the inputs. ###
# # ### COPY_X: when True it copies the inputs before fitting them. This is a safety net againts normalization and other transformations.
# # ### FIT_INTERCEPT: similar to statsmodel.add_constant(x1) this automatically add a constant. If we do not want an intercept, we can change to False
# # ### N-JOBS: is a parameter used when we want to parallelize routines.
# # # By default only 1(one) CPU is used. If we work on problems with lots of data and have more than 1 CPU, you can change it to 2.3.4.6 CPUs.

# 6. Find coefficients

reg.coef_ # they are ordered in the way we fed them.
# but when we get ot the multiple regressions, this array will be filled with the coeffcients of each of the features.

# 7. Find intercept

reg.intercept_

# How to make predictions in sklearn #

# 8. Create test_data and predict

test_data = pd.DataFrame(
    [
        [230, 4, 10],    # First house
        [230, 6, 0],     # Second house
        [355, 3, 20]     # Third house
    ],
    columns=['area', 'roomcount', 'buildingage']
)

# 9. Save predictions

predictions = reg.predict(test_data)

# 10. Create results DataFrame

results_df = pd.DataFrame(
    test_data,
    columns=['area', 'roomcount', 'buildingage']
)

# 12. Print results
results_df['price'] = predictions
print(results_df)
