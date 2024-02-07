current_month=0
current_year=0
current_days=0
# Get the date of today and store it in a variable called "today"
import datetime  # Import the datetime module
today = datetime.date.today()  # Call the today method from the date class to get the current date
print("Today's Date:", today)   # Print out the value of the variable "today"

# Extracting month, day and year from the date object using methods provided by the date class
current_month = today.month    # The month is a property of the date object
current_day = today.day      # The day is also a property of the date object
current_year = today.year     # The year is another property of the date object

# Calculate how many days are there in this month?
