# Sample data
item_prices = [2.50, 1.75, 3.00, 1.25]  # Prices of individual items in INR
quantities = [3, 2, 4, 1]               # Quantities of each item
discount_rate = 10                      # Discount rate in percentage
tax_rate = 8                            # Tax rate in percentage

# Step 1: Calculate the total cost before any discounts or taxes
subtotal = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))

# Step 2: Calculate the discount amount
discount_amount = (discount_rate / 100) * subtotal

# Step 3: Calculate the subtotal after applying the discount
subtotal_after_discount = subtotal - discount_amount

# Step 4: Calculate the tax amount
tax_amount = (tax_rate / 100) * subtotal_after_discount

# Step 5: Calculate the final total cost
total_cost = subtotal_after_discount + tax_amount

# Display the results in Indian Rupees
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount: ₹{discount_amount:.2f}")
print(f"Subtotal after discount: ₹{subtotal_after_discount:.2f}")
print(f"Tax: ₹{tax_amount:.2f}")
print(f"Total Cost: ₹{total_cost:.2f}")
