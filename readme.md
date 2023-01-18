# Relationship between the affordability of a healthy diet and body mass index

## The project
In Europe and Northern America 17.3 billion people can not afford a healthy diet. It is known that prices rise with the increase in the level of diet quality. In general, a healthy diet is 60% more expensive than an energy sufficient diet `[1][2]`. Therfore it can be speculated that the affordability of a healthy diet may lead to poor dietery decisions. These poor dietery decisions may be reflected on body mass index (BMI) In this project the relationship between the affordability of a healthy diet and BMI is studied. 

## Data acquisition

The data used in this project is obtained from two different data sources. The BMI data is obtained from https://www.ncdrisc.org/data-downloads-adiposity.html and downloaded in the csv format. This data contains out of all of the mean BMI's (with 95% confidence intervals) per country per sex, ranging from the year 1975 to 2016. In addition, the dataset contains the prevalence of certain BMI ranges (with 95% confidence intervals). For example, a person is classified as obese if the BMI is higher or equal to 30.

The affordability of a healthy diet is obtained from https://databank.worldbank.org/source/food-prices-for-nutrition (select all under country, select 'Affordability of a healthy diet: ratio of cost to food expenditures' under series, select 2017 under year) and downloaded in the csv format. In this dataset the affordability of a healthy diet is defined as the ratio of the cost of a healthy diet to food expenditures. This ratio is given by country and by sex in the year 2017.

Keep in mind that the BMI dataset is from the year 2017 and the healthy diet affordability dataset is from 2016. At this point in time, the global BMI data is only available up to 2016 and the healthy diet data from 2017 until 2020. In this project the 2017 and 2016  will be compared. The mean BMI and heatlhy diet affordability are unlikely to change a lot from year to year and therefor are compared. However, when 2017 BMI data is available it is better to use that instead of the 2016 data.

## Installation
In this project python (`3.10.8`) is used. The used packages are listed below and be installed using conda with the following command:

`conda install {package}=={version}`

### Packages:

| Package          | Version  |
| -----------------| :------: |
| numpy            | `1.23.3` |
| pandas           | `1.4.4`  |
| matplotlib       | `3.5.2`  |
| bokeh            | `2.4.3`  |
| folium           | `0.13.0` |
| statsmodels      | `0.13.2` |


## Usage
* Firstly, the data needs to be downloaded/

* Secondly, the filepaths of these files need to be configred in the `config.yaml` file.

* Thirdly, python and the used packages maybe need to be installed.

* Lastly, open the final_assignment.ipynb and run all the cells.

## References
`[1]` https://www.fao.org/3/cb4474en/cb4474en.pdf

`[2]` https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-016-2996-y

## Contact
The owner of this repository can be contacted by emailting to:

j.maathuis@st.hanze.nl

## License



