#! Program bank account
import account


rate = int(input("Enter percent, %: "))
money = int(input("Enter amount: "))
period = int(input("Enter period for bank account, mounts: "))

result = account.calculate_income(rate, money, period)
print("Account parameter:\n", "Amount: ", money, "\n", "Percent, %: ", rate, "\n",
      "Period: ", period, "\n", "Amount of the account at the end of the period: ", result)
