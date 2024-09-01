actual_cost = float(input("Enter The Actual Product Price: "))
sale_amount = float (input("Enter The Sales Amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("NO PROFIT !!!!")