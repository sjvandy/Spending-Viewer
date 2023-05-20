# Spending Viewer
# Tracks how much you are spending on what with your Apple Card transaction CSV
import csv
from decimal import *

transaction_categories = []
total_spending = 0

#Import Transactions
with open('transactions.csv') as transactions_csv:
    all_transactions = csv.DictReader(transactions_csv)
    for row in all_transactions:
        # Verify transaction is a purchase        
        if row['Type'] == 'Purchase':
            #Create list of category transactions
            if row['Category'] not in transaction_categories:
                transaction_categories.append(row['Category'])
            total_spending += Decimal(row['Amount (USD)'])
print(transaction_categories)