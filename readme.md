# Relationship between the affordability of a healthy diet and body mass index

## The project


## Data acquisition

The data used in this project is obtained from two different data sources. The BMI data is obtained from https://www.ncdrisc.org/data-downloads-adiposity.html and downloaded in the csv format. This data contains out of all of the mean BMI's (with 95% confidence intervals) per country per sex, ranging from the year 1975 to 2016. In addition, the dataset contains the prevalence of certain BMI ranges (with 95% confidence intervals). For example, a person is classified as obese if the BMI is higher or equal to 30.

The affordability of a healthy diet is obtained from https://databank.worldbank.org/source/food-prices-for-nutrition (select all under country, select 'Affordability of a healthy diet: ratio of cost to food expenditures' under series, select 2017 under year) and downloaded in the csv format. In this dataset the affordability of a healthy diet is defined as the ratio of the cost of a healthy diet to food expenditures. This ratio is given by country and by sex in the year 2017.

Keep in mind that the BMI dataset is from the year 2017 and the healthy diet affordability dataset is from 2016. At this point in time the global BMI data is only available up to 2016 and the healthy diet data from 2017 until 2020. In this project the 2017 and 2016 will be compared. The mean BMI and heatlhy diet affordability are unlikely to change a lot from year to year and therefor are compared. However, when 2017 BMI data is available it is better to use that instead of the 2016 data.


## Dependecies
| Package          | Version  |
| -----------------| :------: |
| numpy            | `1.23.3` |
| pandas           | `1.4.4`  |
| matplotlib       | `3.5.2`  |
| bokeh            | `2.4.3`  |
| folium           | `0.13.0` |
| statsmodels      | `0.13.2` |


## License


