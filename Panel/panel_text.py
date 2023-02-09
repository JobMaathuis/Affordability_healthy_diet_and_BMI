from panel.pane import Markdown

homepage = '''
In Europe and Northern America 17.3 billion people can not afford a healthy diet.  
It is known that prices rise with the increase in the level of diet quality.  
In general, a healthy diet is 60% more expensive than an energy sufficient diet.  
Therfore it can be speculated that the affordability of a healthy diet may lead to poor dietery decisions.  
These poor dietery decisions may be reflected on body mass index (BMI).  
In this project the relationship between the affordability of a healthy diet and BMI was studied.  \n

In this dashboard the visualisation made durining this project can be explored.  
The following sections are included:

* Data exploration 
* Geo map
* Statistics

However, this is only a quick overview of the project.   
For the full the project, see the ipython notebook.  
'''

homepage = Markdown(homepage)  # markdown for the summation points

exploration1 = '''
In this section the graphs obtained from the data explorations are shown.\n
'''

exploration2 = '''
The distribution of the affordability of a healthy diet dataset can be visualised using a barplot.\n
'''

exploration3 = '''
There are a lot of outliers in the upper range.  
This means that in certain countries the healthy diet is very unaffordable.  
All of these countries are poor countries located in Africa.  
Since there is a lot of poverty in Africa, it makes sense that a healthy diet is also very unaffordable, just like all the other food.  
The same problem may also occur in other poor countries outside Africa.  
Because of this reason and the intention of this project the decision is made to only include countries located in Europe, where no real poor countries are located.  
There are 43 countries left after selecting European countries.  
Because a lot of data is removed we can again have a look at the distribution of the data.\n
'''

exploration4 = '''
The distribution of the data is now better.  
There are two outliers (Bulgaria and Serbia), because there is no reason to remove them they are not removed.\n
'''

exploration5 = '''
The distribution of the BMI dataset can be visualised using a barplot.\n
'''

exploration6 = '''
The mean BMI data shows a nice distribution for both genders.  
The data of men is a bit higher in all quartiles, and therefor also has a higher median.  
The women data has a higher spread in the dsitrbution compared to men, and also has an outlier on both sides.
The outliers are the Mean BMI of Turkey (upper outier) and Switserland (lower outlier), since there again is no reason to remove these outliers so they are not removed from the dataset. \n
Next we can have a look at each mean BMI per country per sex.  
A barplot is chosen where also the 95% confidence interval is shown, with whiskers.  
Since there are a lot of country, and each country has a mean BMI for each gender it is almost impossible to show this all at once.  
Therefore, panel widgets are used in which the user can select which data is shown.  
(multiple values can be selected by holding ctrl or shift and clicking mutlitple countries or genders or by clicking and dragging the mouse)
'''

exploration7 = '''
As can be explored above, most of the countries have similar BMI's.  
When taking the error or 95% confidince intervals into account not much variation can be seen between most of the countries.
'''

geomap = '''
Below a geographical overview of the Affordability of a healthy diet and the BMI data can be seen.  
You can choose between the two datasets using the toggle on the top right of the geomap. \n
'''

statistics = '''
Satistical analysis is used to see wheter or not there is a significant relationship between the affordability of a healthy diet and the BMI in European countries.  
This is done with two statitstical approaches: regression and correlation.  \n
'''

regression1 = '''
As can be seen in the summary, the fit has a very low R-squared (and adjusted R-squared).
This means that the amount of variance explained by this model is very small.
Therefore the quality of the fit is not good. We can visualise the fitted model, where it is expected that there is not a good fit.
The p-value of the intercept is 0.000 and thus a significant parameter to the model.
However, the p-value of the slope is 0.188 and not significant to the model. If the slope is not significant to the model it can be removed.
This results in a straight horizontal line, and therefore there will not be a significant relationship  \n
'''

regression2 = '''
As can be seen, the fited line is not a good fit through the datapoints.
The data it self has a lot of variance at most of the different x values. 
This is also the reason the R-squared is so low, it is almost impossible to create a fit that explains this variance.
In conclusion, the BMI does not seem to be affected by the affordability of a healthy diet. \n
'''

correlation1 = '''
To know which correlation tests to use, we need to know if the data is normally distrubted.  
First we look at both datasets using a histogram to see if we can visually see if it follows a normal distribution or not.  
After that we can use a Q-Q plot (Quantile-Quantile plot) to confirm or deny the normallity of the datasets.  \n
'''

correlation2 = '''
The left histogram does somewhat follow a normal distrubtion, but it contains a more data than expected in the tails and will probably be not normally distributed when checked with a Q-Q plot.  
However, the mean BMI data does seem to be normally distributed since it nicely follows the red line, which is the normal distribution approximation.  
We can check if they are normally distributed using a Q-Q plot.  \n
'''

correlation3 = '''
The left Q-Q plot does show some points out of the 95% confidence interval.  
However, it is expected that four points are outside this confidence interval and there are about four points outside, but this is hard to see in the plot.  
It also does not really follow the diagonal line perfectly.  
In the right Q-Q plot the data does seem to follow the diagonal line nicely in the middle, but in the lower quantiles it has 4 points outside the confidence interval, but this is the same amount as expected.
Since it is still not very clear if the data is normally distributed or not, a normality test is used. The Shapiro-Wilk test is chosen, with the following hypothesis:  

* H0: the data is normally distributed
* H1: the data is not normally distributed   
(It will be tested using an alpha of 0.05)  

The obtained p-values of this test are as follows:  
 
* p-value Affordability of a healthy diet: 0.009157
* p-value Mean BMI: 0.495638

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

* H0: The correlation is not different from 0 (correlation = 0)
* H1: The correlation is bigger than 0 (correlation > 0)

The Spearman rank-order correlation test gave back the following results:   
 
* A correlation of 0.1471  
* A p-value of 0.0883  

The correlation obtained is approximately 0.1471, which is a small positive correlation.  
This means that when the affordability of a healthy diet increases the mean BMI also increases.  
However, the obtained p-value is approximatly 0.0883 and above an alpha of 0.05.  
Therfore, we can not reject H0 and this means that there is no significant correlation between the mean BMI and affordability of a healthy diet.
'''

correlation3 = Markdown(correlation3)  # markdown for the summation dots