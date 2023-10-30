class TrialBalance:
    def __init__(self, account_name, debit=0, credit=0):
        self.account_name = account_name
        self.debit = debit
        self.credit = credit

    def __str__(self):
        return f"{self.account_name:30} Debit: {self.debit:12,.2f}  Credit: {self.credit:12,.2f}"


# Unadjusted Trial Balance
accounts = [
    TrialBalance("Cash", debit=10200),
    TrialBalance("Accounts Receivable", debit=34750),
    TrialBalance("Prepaid Insurance", debit=6000),
    TrialBalance("Supplies", debit=1725),
    TrialBalance("Land", debit=50000),
    TrialBalance("Building", debit=155750),
    TrialBalance("Accumulated Depreciation--Building", credit=62850),
    TrialBalance("Equipment", debit=45000),
    TrialBalance("Accumulated Depreciation--Equipment", credit=13650),
    TrialBalance("Accounts Payable", credit=3750),
    TrialBalance("Unearned Rent", credit=3600),
    TrialBalance("Unearned Fees", credit=4000),
    TrialBalance("Wages Payable", credit=0, debit=4190),
    TrialBalance("Sebastian Smith, Withdrawals", debit=8000),
    TrialBalance("Sebastian Smith, Capital", credit=153550),
    TrialBalance("Legal Fees Revenue", credit=158600),
    TrialBalance("Advertising Expense", debit=7500),
    TrialBalance("Depreciation Expense", debit=0, credit=0),
    TrialBalance("Repairs Expense", debit=6100),
    TrialBalance("Supplies Expense", debit=0, credit=0),
    TrialBalance("Utilities Expense", debit=14100),
    TrialBalance("Miscellaneous Expense", debit=4025),
    TrialBalance("Wages Expense", debit=56850),
]

# Adjusting entries
adjusting_entries = [
    ("Legal Fees Revenue", 0, 2240),  # Fees earned but unbilled
    ("Supplies", 875, 0),  # Supplies on hand
    ("Depreciation Expense", 6180, 0),  # Depreciation of equipment
    ("Unearned Fees", 2200, 0),  # Services provided
    ("Wages Expense", 0, 4190),  # Unpaid wages accrued
    ("Depreciation Expense", 7180, 0),  # Depreciation of the Building
]

# Apply adjusting entries
for entry in adjusting_entries:
    account_name, debit, credit = entry
    for account in accounts:
        if account.account_name == account_name:
            account.debit += debit
            account.credit += credit

# Print adjusted trial balance
print("{:30} {:>15} {:>15}".format("Account", "Debit", "Credit"))
print("=" * 60)
for account in accounts:
    print(account)
