import pandas as pd

start_date = pd.to_datetime('2022-01-01')
end_date = pd.to_datetime('2023-05-28')
# Generate a date range using pandas date_range function
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Create a DataFrame for the date/calendar table
calendar_table = pd.DataFrame({'Date': date_range})

# Extract additional date components if needed
calendar_table['Year'] = calendar_table['Date'].dt.year
calendar_table['Month'] = calendar_table['Date'].dt.month
calendar_table['Day'] = calendar_table['Date'].dt.day

calendar_table['Date'] = pd.to_datetime(calendar_table['Date'])

# Extract the month name and assign it to a new column 'Month_Name'
calendar_table['Month_Name'] = calendar_table['Date'].dt.strftime('%B')

# Extract the day of the week and assign it to a new column 'Day_of_Week'
calendar_table['Day_of_Week'] = calendar_table['Date'].dt.day_name()

#print(calendar_table)

# Export the calendar table to Excel without the DataFrame's index
calendar_table.to_excel('calendar_table.xlsx', index=False)
