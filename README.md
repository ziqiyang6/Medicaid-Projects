# Medicaid-Projects

##Background:
This project forecasts the future medicaid enrollment and expenditure of America for next decade. Medicaid is a joint federal and state program that helps cover medical costs for some people with limited income and resources. The federal government has general rules that all state Medicaid programs must follow, but each state runs its own program. Each year, Ferderal and state government need to consider the budget for Medicaid. By providing the forecasting, the primary customer, federal and state government, will have a clear idea about the growth of Medicaid Enrollment and Expenditure. 

##Source:
###Source Background:
Based on the sources from Kaiser Family Foundation (KFF), and 'Data.Medicaid.gov', the csv file 'data.csv' contains the number of Medicaid Enrollment from 2017 to 2023. In this file, the number of Medicaid Enrollment is counted monthly. 
Kaiser Family Foundation is the independent source for health policy research, polling, and journalism. It provides the data for most health systems in America objectively. 
'Data.Medicaid.gov' is an open data tool of CMS, Centers for Medicare & Medicaid Services, provides health coverage to more than 100 million people through Medicare, Medicaid, the Children’s Health Insurance Program, and the Health Insurance Marketplace.

###Instadeq
Instadeq is a website that can convert csv file to the chart under most requirements. Under the easy operation, the file can be filtered, grouped, and form multiple charts to satify different requirements.
'data.csv' have two different charts: (1) pie chart to show medicaid enrollment by states. (2) bar chart to show medicaid enrollment by month from 2017 to 2023. Both links are cited above. 

##Installation:
Inputing the data, editing data, creating and training the model, and ploting the model are the completed processes of forecasting the data. This project is completed by Python. The installation of Python and the specific libraries is required to run the script.
###Python Installation:
Version of Python: 3.8.1 or above
Website: www.python.org
###Libraries Installtion:
Three libraries are required.
**pandas:**
Version of pandas: 1.5.3
In the terminal,type
pip3 install pandas
**matplotlib:**
Version of maplotlib: 3.7.2
In the terminal, type
pip3 install matplotlib
**prophet:**
Version of prophet: 1.1.4
In the terminal, type
pip3 install prophet
**Version Check:**
pip list
 

