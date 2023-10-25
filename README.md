# Medicaid-Projects
  <a href="https://emrts.us" target="_blank"> ![image](https://github.com/tmwang7324/Medicaid-Analysis/assets/121271571/16e51d9d-e2f7-4e49-b407-1005281d932a) </a>

## Introduction:    
Medicaid is an insurance program that covers the medical costs of qualifying individuals. Medicaid is a federal/state system and administered by states. It is essential to have data about its usage to make accurate budgets in advance. We address this using existing data to predict Medicaid enrollment and expenditure for the next decade. This process of forecasting is also called Time Series Analysis. Terminologically, time series analysis is a specific way of analyzing a sequence of data points collected over an interval of time.

Our aim is to make a time series analysis of Medicaid expenditures. This work is backed by [EMRTS](https://emrts.us/) (EMR Techincal Solution), which provides technical solutions in the Medicaid space. The original project is discussed in [Reflections on Medicaid Enrollment for the Next Decade](https://emrts.us/2021/07/31/reflections-on-medicaid-enrollment-for-the-next-decade/). Since this work should be done continuously to provide the latest analysis with the latest data, we’ve added more information and data about Medicaid expenditure and have made graphs using Instadeq, which will be introduced later.

## Source:
### Source Background:
#### Enrollment:
Our data sources are obtained from the [Kaiser Family Foundation (KFF)](https://www.kff.org/other/state-indicator/medicaid-and-chip-monthly-enrollment/?currentTimeframe=0&sortModel=%7B%22colId%22:%22Location%22,%22sort%22:%22asc%22%7D) and [Data.Medicaid.gov](https://data.medicaid.gov/dataset/6165f45b-ca93-5bb5-9d06-db29c692a360/data). The CSV file _data.csv_ contains the number of Medicaid Enrollments from 2017 to 2023. In this file, the number of Medicaid Enrollments is counted monthly. Kaiser Family Foundation is an independent health policy research, polling, and journalism source. It provides objective data for most health systems in the United States. _Data.medicaid.gov_ is an open data tool from CMS, or Centers for Medicare & Medicaid Services, which provides health coverage to more than 100 million people.
#### Expenditure:
The [U.S. Department of Health and Human Service](https://oig.hhs.gov/fraud/medicaid-fraud-control-units-mfcu/) is the primary source of Medicaid expenditure. This project uses the charts showing Medicaid expenditures from 2010 to 2022, listed under _Expenditure & Statistics_. The pie chart of Medicaid expenditure mentioned later uses data from 2022, listed in the _FY 2022 Chart_. The file [_Medicaid_Expenditure_2010-2022.csv_](https://github.com/ziqiyang6/Medicaid-Projects/blob/main/Medicaid_Expenditure_2010-2022.csv) is the CSV file containing the total Medicaid expenditures from 2010 to 2022.

## Instadeq:
[Instadeq](https://instadeq.com/) converts CSV files into a chart. Under the easy operation, files can be filtered and grouped to form multiple charts to satisfy different requirements. _Data.csv_ has two charts:
1. [Pie chart to show medicaid enrollment by states.](https://mmiscloud.us/s/@zyang/medicaid-enrollment-pie/) 
2. [Bar chart to show medicaid enrollment by month from 2017 to 2023.](https://mmiscloud.us/s/@zyang/medicaid-enrollment-layout-by-report-date/).   
_Medicaid_Expenditure_2010-2022.csv_ also has three graphs from Instadeq:
1. [Pie chart to show medicaid expenditure by states in 2022](https://mmiscloud.us/s/@zyang/medicaid-expenditure-pie/)
2. [Bar chart to show medicaid expenditure yearly from 2010 to 2022](https://mmiscloud.us/s/@zyang/medicaid-expenditure-bar-yearly/)
3. [Bar chart to show medicaid expenditure by month from 2010 to 2022](https://mmiscloud.us/s/@zyang/medicaid-expenditure-bar-monthly/).

Number 3 is graphed by CSV file _Expenditure_Monthly_data_2010-2022.csv_, and Python file _Expenditure_Forecasting_Monthly.py_. 
_Expenditure_Monthly_data_2010-2022.csv_ is a file that uses linear interpolation by _Expenditure_Yearly_data-2010-2022.csv_. The trends of numbers 2 and 3 are identical, but number 3 lists specific months.

With two CSV files containing the forecasted data, there are also two Instadeq graphs: 
1. [Bar chart of **medicaid enrollment yearly** forecasting from 2023 to 2033.](https://mmiscloud.us/s/@zyang/layout-of-bar-graph-of-forcasted-medicaid-enrollment/)
2. [Bar chart of **medicaid expenditure yearly** forecasting from 2023 to 2032.](https://mmiscloud.us/s/@zyang/medicaid-forecast-expenditure-from-2023-to-2032/)

## Prophet:
Prophet, an open-source tool from Facebook used for forecasting time series data, is a library designed for **Python** and **R** to help businesses understand and predict the market. It is based on a decomposable additive model where non-linear trends fit with seasonality, even considering the effects of holidays. [Here](https://facebook.github.io/prophet/) is the official Prophet website, and [here](https://github.com/facebook/prophet) is the GitHub. The official website can provide some basic ideas about Prophet, while its GitHub provides more detailed information. Prophet is the primary tool we use for forecasting.

## Installation:
Inputting and editing data, creating and training the model, and plotting the model are the data forecasting processes. This project is completed using **Python** and **R**. Installing Python, R, and the specified libraries are required to run the script.

### Python Installation:
**Version of Python:** 3.8.1 or above

**Website:** www.python.org
#### Python Libraries Installtion:
Three libraries are required.
##### **pandas:**
**Version of pandas:** 1.5.3
In the terminal,type
```
pip3 install pandas
```
##### **matplotlib:**
**Version of maplotlib:** 3.7.2
In the terminal, type
```
pip3 install matplotlib
```
##### **prophet:**
**Version of prophet:** 1.1.4
In the terminal, type
```
pip3 install prophet
```
##### **Version Check:**
```
pip list
```
Type this command in terminal
### R Installation:
**Version of R:** 4.3.1 or above

**Website:** www.R-project.org
#### R Packages Installtion:
To install the packages of R, **you will need to open the console of R**.
##### **prophet:**
**Version of prophet:** 1.0.0
```
install.packages("prophet")
```
##### **tidyverse:**
**Version of tidyverse:** 2.0.0
```
install.packages("tidyverse")
```
##### **lubridate:**
**Version of lubridate:** 1.9.3
```
install.packages("lubridate")
```
##### **Version Check in R:**
In R console, type
```
packageVersion("packagename")
```
'packagename' is the name of the package

## Usage:
To use python and R file in the system, open the PowerShell of the system. 

Before running the scripts, please type command:
```
pip3 install --upgrade pip
```

```
pip3 freeze
```
### Python:
For Medicaid Enrollment, Type 
``` 
python 'Forecasting_for_Enrollment.py'
``` 
For Medicaid Expenditure, Type
```
python 'Expenditure_Forecasting.py'
```
### R:
For Medicaid Enrollment, Type
```
Rscript "Medicaid_Enrollment_Prophet.R"
```
For Medicaid Expenditure, Type
```
Rscript "Medicaid_Expenditure_Prophet.R"
```






