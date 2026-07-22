num_items_str = input("Enter number of items: ")
num_items = int(num_items_str)

item_price_str = input("Enter item price: ")
item_price = float(item_price_str)

customer_cash_str = input("Enter Customer Cash: ")
customer_cash = float(customer_cash_str)

total_cost = round(item_price * num_items, 2)

change_due = round(customer_cash - total_cost, 2)

if change_due < 0:
    print("Customer didn't provide enough cash to cover transaction.")
else:
    running_change_due = change_due
    dollars_due = running_change_due // 1
    running_change_due -= dollars_due
    quarters_due = running_change_due // 0.25
    running_change_due -= quarters_due * 0.25
    dimes_due = running_change_due // 0.1
    running_change_due -= dimes_due * .1
    nickels_due = running_change_due // 0.05
    running_change_due -= nickels_due * 0.05
    pennies_due = round(running_change_due * 100, 2)
    summary = f"""
summary:
    total: {total_cost}
    change due: {change_due}
    dispense as:
        dollars:  {dollars_due}
        quarters: {quarters_due}
        dimes:    {dimes_due}
        nickels:  {nickels_due}
        pennies:  {pennies_due}
"""
print(summary)