install.packages("tidyverse")
install.packages("prophet")
install.packages("lubridate")

# Libraries
library(tidyverse)
library(prophet)
library(lubridate)

# Read the data
df <- read_csv("E:/some_files/data.csv")

# Filter rows and columns
df <- df %>% 
  filter(final_report == 'Y', 
         report_date != '09/01/2013') %>%
  drop_na(total_medicaid_and_chip_enrollment) %>% 
  select(report_date, total_medicaid_and_chip_enrollment)

# Aggregate data
df <- df %>% 
  group_by(report_date) %>% 
  summarise(y = sum(total_medicaid_and_chip_enrollment)) %>% 
  rename(ds = report_date)
df$ds <- mdy(df$ds)

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

