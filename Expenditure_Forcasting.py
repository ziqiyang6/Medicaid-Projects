'''**********************************************************************************
                                                                                    *
Project Name: Expenditure_Forcasting_Monthly                                        *
                                                                                    *
Programming Language: Python 3.8                                                    *
                                                                                    *
Libraries: Pandas 2.1.0    Prophet 1.1.4     Matplotlib 3.7.2                       *
                                                                                    *
Creater Name: Ziqi Yang                                                             *
                                                                                    *
Published Date: 09/19/2023                                                          *
                                                                                    *
Version: 1.0                                                                        *
                                                                                    *
                                                                                    *
                                                                                    *
                                                                                    *
                                                                                    *
                                                                                    *
**********************************************************************************'''

####    Scripts start below

import pandas as pd

# Creates a new DataFrame to contain the data from 2010 to 2022
data = {'Year': ['2010/12/31', '2011/12/31', '2012/12/31', '2013/12/31', '2014/12/31', '2015/12/31', '2016/12/31', '2017/12/31', '2018/12/31', '2019/12/31', '2020/12/31', '2021/12/31', '2022/12/31'],
        'Expenditures': [397000000000, 424000000000, 429000000000, 453000000000, 488000000000, 548000000000, 571000000000, 596000000000, 612000000000, 615000000000, 679000000000, 740000000000, 824000000000]}
df = pd.DataFrame(data)

# Convert the "Year" column to datetime objects, accommodating the "xxxx/xx/xx" format
df['Year'] = pd.to_datetime(df['Year'], format='%Y/%m/%d')

# Set "Year" as the index
df.set_index('Year', inplace=True)

# Resample the data to monthly frequency and use linear interpolation to fill in the values
df_monthly = df.resample('M').asfreq()  # Convert to monthly data
df_monthly.interpolate(method='linear', inplace=True)  # Perform linear interpolation

# Store the monthly data in a csv file, named 'Expenditure_Monthly_data_2010-2022.csv'
df_monthly.reset_index().to_csv('Expenditure_Monthly_data_2010-2022.csv', index=False)

from prophet import Prophet
import matplotlib.pyplot as plt

#Setting the display size
pd.set_option('display.width', 300)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

# Columns Editing
df_monthly = df_monthly.reset_index()  # Reset the index
df_monthly = df_monthly.rename(columns={'Year':'ds','Expenditures':'y'}) # Rename columns to the ones that Prophet require.
# Note: Prophet requires the date to be named as 'ds', and targeted data as 'y'
print(df_monthly.head())

# Modeling
model = Prophet()  # Create the model
model.fit(df_monthly)      # Train the model

# Create a new dataframe for next ten years
future = model.make_future_dataframe(periods = 365 *10)

# Forecasting
forecast = model.predict(future)

# The graph of predicted result
fig1 = model.plot(forecast)
plt.title('Medicaid_Expenditure_Forecast')
plt.show()
#   Black Dots: Historical Data
#   Blue Line: Forecasted Trend
#   Blue Shadow: The Uncertain Intervals of the Forecast

fig2 = model.plot_components(forecast)      # The yearly and weekly effects
plt.show()

#   Top graph: Showing the roughly trending of medicaid enrollment in the future
#   Bottom graph: Showing the trending in the period of one year
