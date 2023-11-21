import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate random data for demonstration
np.random.seed(42)
customer_ids = np.random.randint(1, 6, 50)
order_dates = pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, 50), unit='D')
product_names = np.random.choice(['Product_A', 'Product_B', 'Product_C'], 50)
order_quantities = np.random.randint(1, 10, 50)

# Create the DataFrame
order_data = pd.DataFrame({
    'customer_id': customer_ids,
    'order_date': order_dates,
    'product_name': product_names,
    'order_quantity': order_quantities
})

# Display the generated data
print("Generated Order Data:")
print(order_data)

# Now, perform the analysis
total_orders_by_customer = order_data.groupby('customer_id')['order_date'].count()
average_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

# Displaying the results
print("\nTotal Orders by Each Customer:\n", total_orders_by_customer)
print("\nAverage Order Quantity for Each Product:\n", average_quantity_per_product)
print("\nEarliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
