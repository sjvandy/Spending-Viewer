# Spending Viewer
# Tracks how much you are spending on what with your Apple Card transaction CSV
import csv
from pathlib import Path
from decimal import *

transactions_path = Path('transactions.csv')

transaction_categories = {}
category_percentage = {}
total_spending = 0

# Terminal UI
print('Welcome to the Apple Card Spending Tracker!')
print('Here you can view what percentages you are spending in what categories on your Apple card.')

# Verifies transactions.csv is located in root folder
if transactions_path.is_file():
    print("We've found your transactions! Calculating transactions...")
    # Import Transactions
    with open('transactions.csv') as transactions_csv:
        all_transactions = csv.DictReader(transactions_csv)
        for row in all_transactions:
            # Verify transaction is a purchase        
            if row['Type'] == 'Purchase':
                #Create list of category transactions
                if row['Category'] not in transaction_categories:
                    transaction_categories[row['Category']] = 0
                total_spending += Decimal(row['Amount (USD)'])
                transaction_categories[row['Category']] += Decimal(row['Amount (USD)'])
else:
    print('transactions.csv not detected in folder, please add file, rename to "transactions.csv", then re-open the program.')                

#Calculating Percentages of Spending
for category, cost in transaction_categories.items():
    category_percentage[category] = round((Decimal(cost)/Decimal(total_spending)) * 100, 2)

#Summary
print('Here is your monthly spending habits:')
for category, percentage in category_percentage.items():
    print(f'You spent {percentage}% on {category}')


