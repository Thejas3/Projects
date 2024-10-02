principal_quest = input('Please enter the lean principle: ')
principal_quest = int(principal_quest)
loan_term = input('Please enter the loan term in months: ')
loan_term = int(loan_term)
annual_rate = input('Please enter hte annual interst rate of the laon in terms of a decimal: ')
annual_rate = float(annual_rate)
total_amount = principal_quest*(1+(annual_rate/12))**loan_term
final_amount = total_amount-principal_quest
print('${:.2f}'.format(final_amount))