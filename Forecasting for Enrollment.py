#Libraries: Pandas, Prophet, and Matplot
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

#Setting the display size
pd.set_option('display.width', 300)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

#Input the data. Check your own Path!!!!!
df = pd.read_csv('E:/一些文件/data.csv', encoding = 'unicode_escape')   #Note: data.csv is the csv file of Medicaid Enrollment

# Limit the rows that satisfy the requirements.
df = df[df['final_report'] == 'Y']   # Need rows that are the final report only
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
