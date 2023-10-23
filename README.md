# Medicaid-Projects
  <a href="https://emrts.us" target="_blank"> ![image](https://github.com/tmwang7324/Medicaid-Analysis/assets/121271571/16e51d9d-e2f7-4e49-b407-1005281d932a) </a>

## Introduction:    
Medicaid, one of the major insurance programs in the United States, is a joint federal and state program that helps cover partial medical costs for some people with limited income and resources. It is similar to another major health insurance program, Medicare. However, Medicare is federal health insurance for people 65 or older, and some people under 65 with certain disabilities or conditions. The main target of Medicare is the group of old people or kids, but for Medicaid, it focus on the group with low income. In other words, Medicaid and Medicare are different program for different groups of people. [Here](https://www.hhs.gov/answers/medicare-and-medicaid/what-is-the-difference-between-medicare-medicaid/index.html) is the comparison of Medicaid and Medicare provided by HHS (U.S. Department of Health and Human Service). However, Medicaid is a program that financed by federal government but administrated by states. Therefore, Every states will have individual medicaid programs. Since state and federal government will pay the bills together, it is essential to have future data for future budgets. This is the significance of this project. By using the exsiting data of Medicaid Enrollment and Expenditure, we will forecasat the Medicaid Enrollment and Expenditure for next decade to the governments, to help them adjust the budget. This process of forecasting, is also called "Time Series Analysis". Terminologically, time series analysis is a specific way of analyzing a sequence of data points collected over an interval of time. The essence of this project is to make time series analysis over Medicaid. 

This project is assigned by [EMRTS](https://emrts.us/) (EMR Techincal Solution), a company provides professional analysis about Medicaid. The original full name of this project is "Reflections on Medicaid Enrollment for the Next Decade", which is one of the blogs from the website. However, in providing the newest analysis with newest data, this project should be done continuously. [Here](https://emrts.us/2021/07/31/reflections-on-medicaid-enrollment-for-the-next-decade/) is the last blog page. For this project, we added more information and data than the one from the blog, which the expenditure of Medicaid would be covered as well. More than that, the form of graph changed to new tool, Instadeq, which will be introduced later. 


## Source:
### Source Background:
#### Enrollment:
Based on the sources from [Kaiser Family Foundation (KFF)](https://www.kff.org/other/state-indicator/medicaid-and-chip-monthly-enrollment/?currentTimeframe=0&sortModel=%7B%22colId%22:%22Location%22,%22sort%22:%22asc%22%7D), and ['Data.Medicaid.gov'](https://data.medicaid.gov/dataset/6165f45b-ca93-5bb5-9d06-db29c692a360/data), the csv file 'data.csv' contains the number of Medicaid Enrollment from 2017 to 2023. In this file, the number of Medicaid Enrollment is counted monthly. 
Kaiser Family Foundation is the independent source for health policy research, polling, and journalism. It provides the data for most health systems in America objectively. 
'Data.Medicaid.gov' is an open data tool of CMS, Centers for Medicare & Medicaid Services, provides health coverage to more than 100 million people through Medicare, Medicaid, the Children’s Health Insurance Program, and the Health Insurance Marketplace.
#### Expenditure:
The main source for Medicaid Expenditure is the [U.S. Department of Health and Human Service](https://oig.hhs.gov/fraud/medicaid-fraud-control-units-mfcu/). Under the section of "Expenditure&Statistics", the charts of specific expenditures of medicaid from 2010 to 2022 are listed. The data is from the ferderal government of the U.S., which is reliable. This project will only use the expenditures of total medicaid. The pie chart of medicaid expenditure that will be mentioned later uses the data of year 2022, listed in the "FY 2022 Chart". The file 'Medicaid_Expenditure_2010-2022.csv' is the csv file containing the total expenditures of medicaid from 2010 to 2022. 

## Instadeq:
[Instadeq](https://instadeq.com/) is a website that can convert csv file to the chart under most requirements. Under the easy operation, the file can be filtered, grouped, and form multiple charts to satify different requirements.
'data.csv' have two different charts: [(1): pie chart to show medicaid enrollment by states.](https://mmiscloud.us/s/@zyang/medicaid-enrollment-pie/) [(2) bar chart to show medicaid enrollment by month from 2017 to 2023.](https://mmiscloud.us/s/@zyang/medicaid-enrollment-layout-by-report-date/).   
'Medicaid_Expenditure_2010-2022.csv' also has three graphs from Instadeq:[(1): pie chart to show medicaid expenditure by states in 2022](https://mmiscloud.us/s/@zyang/medicaid-expenditure-pie/) [(2) bar chart to show medicaid expenditure yearly from 2010 to 2022](https://mmiscloud.us/s/@zyang/medicaid-expenditure-bar-yearly/) [(3) bar chart to show medicaid expenditure by month from 2010 to 2022](https://mmiscloud.us/s/@zyang/medicaid-expenditure-bar-monthly/).

**Notice:** (3) is graphed by csv file 'Expenditure_Monthly_data_2010-2022.csv', and this file is created by python file 'Expenditure_Forecasting_Monthly.py'. 'Expenditure_Monthly_data_2010-2022.csv' is a file that used linear interpolation by 'Expenditure_Yearly_data-2010-2022.csv'. The trend of both (2) and (3) is same, but (3) lists specific months. 

As two csv files containing the forecasted data, there are two Instadeq graphs of these two forecasting: [(1): Bar chart of **medicaid enrollment yearly** forecasting from 2023 to 2033.](https://mmiscloud.us/s/@zyang/layout-of-bar-graph-of-forcasted-medicaid-enrollment/) [(2): Bar chart of **medicaid expenditure yearly** forecasting from 2023 to 2032.](https://mmiscloud.us/s/@zyang/medicaid-forecast-expenditure-from-2023-to-2032/)

## Prophet:
Prophet, a library designed for time series analysis for both **Python** and **R** language. Prophet is an open-source tool from Facebook used for forecasting time series data which helps businesses understand and possibly predict the market. It is based on a decomposable additive model where non-linear trends fit with seasonality, it also takes into account the effects of holidays. [Here](https://facebook.github.io/prophet/) is the official website of Prophet. Also, the github site about Prophet is [here](https://github.com/facebook/prophet). The official website can provide some basic ideas about Prophet, which is more general, but the github site of Prophet is more professional, and it provides more detailed and directed information, which is more helpful for a learner. The site provides detailed version of Prophet, so the users can choose suitable version. 

Prophet is the primary tool we use for forecasting, in which both forecasting will apply Prophet. 

## Installation:
Inputing the data, editing data, creating and training the model, and ploting the model are the completed processes of forecasting the data. This project is completed by Python and R. The installation of Python and R ,and the specific libraries are required to run the script.
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






