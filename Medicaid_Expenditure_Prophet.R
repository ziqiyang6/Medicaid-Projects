install.packages("tidyverse")
install.packages("prophet")
install.packages("lubridate")

# Libraries
library(tidyverse)
library(prophet)
library(lubridate)

# Read the data
df <- read_csv("E:/some_files/Expenditure_Monthly_data_2010-2022.csv")

# Convert date to datetime object
df$ds <- ymd(df$Year)

# Renaming columns to match what Prophet expects
names(df)[names(df) == "Expenditures"] <- "y"

# Print head
print(head(df))

# Create the model and fit
model <- prophet(df)

# Create future dates
future <- make_future_dataframe(model, periods = 365 * 10)

# Make forecast
forecast <- predict(model, future)

# Plot the forecast
prophet_plot_components(model, forecast)

# Plot the components
plot(model, forecast)
