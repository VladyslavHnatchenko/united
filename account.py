def calculate_income(rate, money, month):
    if money <= 0:
        return 0

    for i in range(1, month+1):
        money = round(money + money * rate / 100 / 12, 2)
    return money


def main():
    rate = 5
    money = 1000
    period = 12

    result = calculate_income(rate, money, period)
    print("Account parameter:\n", "Amount: ", money, "\n", "Percent, %: ", rate, "\n",
          "Period: ", period, "\n", "Amount of the account at the end of the period: ", result)


if __name__ == "__main__":
    main()
