'''**********************************************************************************
                                                                                    *
Project Name: Forcasting_for_Enrollment                                             *
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
NOTICE: For Line 37 about inputting the csv file, please use the correct path,      *
or the error will appear. According to different computer systems, the              *
encoding need to be changed, or deleted.                                            *
                                                                                    *
Version: 1.1                                                                        *
Line 60 to 62 were added to store the forecasted data in a csv file for             *
visualization. The visualization will be shown in Instadeq.                         *
                                                                                    *
**********************************************************************************'''

####    Scripts start below

#Libraries: Pandas, Prophet, and Matplot
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

#Setting the display size
pd.set_option('display.width', 300)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

#Input the data. Check your own Path!!!!!
df = pd.read_csv('../Medicaid-Projects/data.csv', encoding = 'unicode_escape')   #Note: data.csv is the csv file of Medicaid Enrollment

# Limit the rows that satisfy the requirements.
df = df[df['final_report'] == 'Y']   # Need rows that are the final report only
df = df[df['report_date'] != '09/01/2013']    # Remove the date 09/01/2013 since it was the only date before 06/01/2017
df.dropna(subset=['total_medicaid_enrollment'], inplace=True)   # removes the rows that are empty

# Columns editing
df = df[['report_date', 'total_medicaid_enrollment']]   # Limit the columns to two only: Report date, and medicaid enrollment
df = df.groupby('report_date').agg('sum').reset_index()     # This will sum the number of medicaid enrollment for every single date
df = df.rename(columns={'report_date':'ds','total_medicaid_enrollment':'y'})    # Rename columns to the ones that Prophet require. Note: Prophet requires the date to be named as 'ds', and targeted data as 'y'
print(df.head())

# Modeling
model = Prophet()  # Create the model
model.fit(df)      # Train the model

# Create a new dataframe for next ten years
future = model.make_future_dataframe(periods = 365 *10)

# Forecasting
forecast = model.predict(future)

# Store the forecasted data into a new csv file named 'forecast_data_Medicaid_Enrollment'
forecast_data = forecast.rename(columns = {'ds':'report_date'})
forecast_data.reset_index().to_csv('../Medicaid-Projects/forecast_data_Medicaid_Enrollment.csv', index=False)

# The graph of predicted result
fig1 = model.plot(forecast)
plt.title('Medicaid_Enrollment_Forecast')
plt.show()
#   Black Dots: Historical Data
#   Blue Line: Forecasted Trend
#   Blue Shadow: The Uncertain Intervals of the Forecast

fig2 = model.plot_components(forecast)      # The yearly and weekly effects
plt.show()

#   Top graph: Showing the roughly trending of medicaid enrollment in the future
#   Bottom graph: Showing the trending in the period of one year
