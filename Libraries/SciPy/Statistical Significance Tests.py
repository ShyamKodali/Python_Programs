
# =============================================================================
# Statistical Significance Test : In statistics, statistical significance means that the result that was produced has a reason behind it, it was not produced randomly, or by chance.
# 
# Hypothesis : Hypothesis is an assumption about a parameter in population.
#     Null Hypothesis : It assumes that the observation is not statistically significant.
#     Alternate Hypothesis : It assumes that the observations are due to some reason. It's alternate to Null Hypothesis.
#     
# One tailed test : When our hypothesis is testing for one side of the value only
# Two tailed test : When our hypothesis is testing for both side of the values.
# 
# Alpha value : Alpha value is the level of significance.
# P value : P value tells how close to extreme the data actually is.
#     P value and alpha values are compared to establish the statistical significance.
#     If; p value <= alpha we reject the null hypothesis and say that the data is statistically significant. 
#         p value > alpha  we accept the null hypothesis.
# 
# Normality Tests : Normality tests are based on the skewness and kurtosis.
# 
# Skewness : A measure of symmetry in data.
#     For normal distributions it is 0.
#     If it is negative, it means the data is skewed left.
#     If it is positive it means the data is skewed right.
#     
# Kurtosis : A measure of whether the data is heavy or lightly tailed to a normal distribution.
#     Positive kurtosis means heavy tailed.
#     Negative kurtosis means lightly tailed.
# =============================================================================





# T-Test [Two Tailed Test] : Used To determine if there is significant deference between means of two variables 
#                                 And also lets us know if they belong to the same distribution.

# KS-Test : Used To check if given values follow a distribution.
#           A CDF can be either a string or a callable function that returns the probability.
#           It can be used as a one tailed or two tailed test.
#           By default it is two tailed.

# Normal-Test : Normality tests are based on the skewness and kurtosis.
#               Returns p value for the null hypothesis:


import numpy as np 
from scipy.stats import ttest_ind, kstest, normaltest, skew, kurtosis, describe

v = np.random.normal(size=1000)
v1 = np.random.normal(size=1000)
v2 = np.random.normal(size=1000)


print('T-Test for the values v1 and v2 are : ' + str(ttest_ind(v1, v2)))
print('**************************************************************************************************')
print('KS-Test for the values v to check if it is norm dist : ' + str(kstest(v, cdf='norm')))
print('**************************************************************************************************')
print('Normal-Test for the values v are : ' + str(normaltest(v)))
print('**************************************************************************************************')
print('Summary of values are :' + str(describe(v)))
print('**************************************************************************************************')
print('Skewness of values are :' + str(skew(v)))
print('******************************************')
print('Kurtosis of values are :' + str(kurtosis(v)))
print('******************************************')
