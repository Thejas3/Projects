hourly_wage = input('PLease enter your hourly wage: ')
hourly_wage = int(hourly_wage)
hours_worked = input('Please enter the number of hours worked per week: ')
hours_worked = int(hours_worked)
weeks_worked = input('Please enter the number of weeks worked in a year: ')
weeks_worked = int(weeks_worked)
total_amount = (hourly_wage*hours_worked)*weeks_worked
print('Your salary so far this year is', '$', total_amount)
