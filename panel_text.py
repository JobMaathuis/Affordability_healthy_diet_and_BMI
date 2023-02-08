statistics = '''
Satistical analysis is used to see wheter or not there is a significant relationship between the affordability of a healthy diet and the BMI in European countries.  
This is done with two statitstical approaches: regression and correlation.  
'''

regression1 = '''
As can be seen in the summary, the fit has a very low R-squared (and adjusted R-squared).  
This means that the amount of variance explained by this model is very small.   
Therefore the quality of the fit is not good. We can visualise the fitted model, where it is expected that there is not a good fit.  
The p-value of the intercept is 0.000 and thus a significant parameter to the model.  
However, the p-value of the slope is 0.188 and not significant to the model. If the slope is not significant to the model it can be removed.  
This results in a straight horizontal line, and therefore there will not be a significant relationship.
'''

regression2 = '''
As expected, the fit is not good.  
The data it self has a lot of variance at most of the different x values.  
This is also the reason the R-squared is so low, it is almost impossible to create a fit that explains this variance.  
In conclusion, the BMI does not seem to be affected by the affordability of a healthy diet.
'''

correlation1 = '''
To know which correlation tests to use, we need to know if the data is normally distrubted.  
First we look at both datasets using a histogram to see if we can visually see if it follows a normal distribution or not.  
After that we can use a Q-Q plot (Quantile-Quantile plot) to confirm or deny the normallity of the datasets.
'''

correlation2 = '''
The left histogram does somewhat follow a normal distrubtion, but it contains a more data than expected in the tails and will probably be not normally distributed when checked with a Q-Q plot.  
However, the mean BMI data does seem to be normally distributed since it nicely follows the red line, which is the normal distribution approximation.  
We can check if they are normally distributed using a Q-Q plot.
'''

correlation3 = '''
The left Q-Q plot does show some points out of the 95% confidence interval.  
However, it is expected that four points are outside this confidence interval and there are about four points outside, but this is hard to see in the plot.  
It also does not really follow the diagonal line perfectly.  
In the right Q-Q plot the data does seem to follow the diagonal line nicely in the middle, but in the lower quantiles it has 4 points outside the confidence interval, but this is the same amount as expected.
Since it is still not very clear if the data is normally distributed or not, a normality test is used. The Shapiro-Wilk test is chosen, with the following hypothesis:  

H0: the data is normally distributed
H1: the data is not normally distributed

It will be tested using an alpha of 0.05.  

The obtained p-values of this test are as follows:

p-value Affordability of a healthy diet: 0.009157
p-value Mean BMI: 0.495638

The p-value of the Affordability of a healthy diet is below the set alpha.  
Therefore H0 is rejected and H1 is accepted, the data is not normally distributed.  
On the other hand the p-value of the mean BMI is above the alpha, and is thus normally distributed.  
Because one of the datasets is not normally distributed a the non-parametric correlation test is going to be used.  

In order to see if there is a significant correlation between the two variables a Spearman rank-order correlation test is used.  
This tests calculated the correlation between two variables.   
If there is a strong positive correlation, the correlation will increase as well (up to 1).   
If there is a negative correlation the correlation will go down (up to -1).   
With this statistical test, you test if the correlation obtained is significantly different from 0.  
Because it is hypothesised that there might be a positive correlation the following hypothesis for this can be madecan be made:

H0: The correlation is not different from 0 (correlation = 0)
H1: The correlation is bigger than 0 (correlation > 0)

The Spearman rank-order correlation test gave back a correlation of 0.1471 with a p-value of 0.0883  

The correlation obtained is approximately 0.1471, which is a small positive correlation.  
This means that when the affordability of a healthy diet increases the mean BMI also increases.  
However, the obtained p-value is approximatly 0.0883 and above an alpha of 0.05.  
Therfore, we can not reject H0 and this means that there is no significant correlation between the mean BMI and affordability of a healthy diet.
'''