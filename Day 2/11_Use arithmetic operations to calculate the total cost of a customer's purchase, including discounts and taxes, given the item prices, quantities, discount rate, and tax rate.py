# Sample data
item_prices = [2.5, 1.0, 3.0]  # Prices of items
quantities = [3, 2, 1]         # Quantities of items
discount_rate = 10             # Discount rate in percentage
tax_rate = 5                   # Tax rate in percentage

# Step 2: Calculate the total cost before any discounts or taxes
total_cost_before_discount = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))

# Step 3: Apply the discount to the total cost
discount_amount = (discount_rate / 100) * total_cost_before_discount
discounted_total = total_cost_before_discount - discount_amount

# Step 5: Apply taxes to the discounted total
tax_amount = (tax_rate / 100) * discounted_total
total_cost_after_tax = discounted_total + tax_amount

# Step 6: Calculate the final total cost after applying both discounts and taxes
final_total_cost = round(total_cost_after_tax, 2)  # Rounding to two decimal places

# Display the result
print("Total cost of the purchase: ₹", final_total_cost)
