import csv
import random
from datetime import datetime, timedelta
import numpy as np

# Define the CSV file name
file_name = "sample_data.csv"

# Define the header
header = [
    "As of Date", "Company", "Account", "AU", "Currency",
    "Primary Account", "Secondary Account", "GL Balance",
    "IHub Balance", "Balance Difference", "Match Status"
]

# Parameters
num_days = 400                 # Number of days in the time series
num_accounts = 10              # Number of distinct accounts
avg_transaction_rate = 0.6     # ~60% of days will have transactions
max_transactions_per_day = 4   # Max transactions per day

# Sample companies and currencies
companies = ["Alpha Corp", "Beta Ltd", "Gamma Inc", "Delta LLC", "Zeta Group"]
currencies = ["USD", "EUR", "GBP", "JPY", "CAD"]

# Predefined mapping of Accounts to AU, Primary, and Secondary Accounts
account_mapping = {
    "10001": (5, "LOANS", "DEFERRED COSTS"),
    "10002": (3, "CASH", "ACCOUNTS PAYABLE"),
    "10003": (7, "INVESTMENTS", "ACCOUNTS RECEIVABLE"),
    "10004": (2, "EQUITY", "RETAINED EARNINGS"),
    "10005": (6, "REVENUE", "EXPENSES"),
    "10006": (4, "FIXED ASSETS", "DEPRECIATION"),
    "10007": (8, "BONDS", "INTEREST PAYABLE"),
    "10008": (1, "INVENTORY", "COST OF GOODS SOLD"),
    "10009": (9, "PREPAID EXPENSES", "UNBILLED REVENUE"),
    "10010": (10, "TAXES", "ACCRUED LIABILITIES")
}

# Normal distribution parameters for mismatched balances
mu, sigma = 1000, 200  # Mean and standard deviation for mismatch differences

# Generate random financial time series data
data = []

# Start date
start_date = datetime.today() - timedelta(days=num_days)

# Generate time series data
for day in range(num_days):
    current_date = (start_date + timedelta(days=day)).strftime('%Y-%m-%d')

    for account, (au, primary_account, secondary_account) in account_mapping.items():
        if random.random() < avg_transaction_rate:
            
            transactions_today = random.randint(1, max_transactions_per_day)

            for _ in range(transactions_today):
                company = random.choice(companies)
                currency = random.choice(currencies)

                # 90% chance of matching balances
                if random.random() < 0.9:
                    gl_balance = round(random.uniform(1000, 100000), 2)
                    ihub_balance = gl_balance  # Matching case
                else:
                    gl_balance = round(random.uniform(1000, 100000), 2)
                    diff = round(abs(np.random.normal(mu, sigma)), 2)

                    if random.random() < 0.5:
                        ihub_balance = round(gl_balance + diff, 2)
                    else:
                        ihub_balance = round(gl_balance - diff, 2)

                    ihub_balance = max(0, ihub_balance)

                # Calculate Balance Difference
                balance_difference = round(gl_balance - ihub_balance, 2)

                # Match status
                match_status = "Match" if balance_difference == 0 else "Break"

                # Add row with fixed AU, Primary, and Secondary Account
                data.append([
                    current_date, company, account, au, currency,
                    primary_account, secondary_account, gl_balance,
                    ihub_balance, balance_difference, match_status
                ])

# Write the data to CSV
with open(file_name, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)  # More efficient writing

# Print the output with f-string
print(f"CSV file '{file_name}' created successfully with {len(data):,} rows of time series data! ✅")
