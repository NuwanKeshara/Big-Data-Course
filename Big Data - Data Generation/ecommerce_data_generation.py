import pandas as pd
import numpy as np
import os
import random
import math
import glob

# Set a seed for reproducibility
random.seed(42)
np.random.seed(42)

def generate_data(num_rows, table_name, customers=None):
    """Generates a DataFrame based on table_name and returns it."""
    if table_name == "customers":
        data = pd.DataFrame({
            'customer_id': np.arange(num_rows),
            'name': [f'Customer_{i}' for i in range(num_rows)],
            'city': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad'], num_rows),
            'state': np.random.choice(['Maharashtra', 'Delhi', 'Karnataka', 'Tamil Nadu', 'West Bengal', 'Telangana', 'Gujarat'], num_rows),
            'country': 'India',
            'registration_date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D'),
            'is_active': np.random.choice([True, False], num_rows)
        })
    elif table_name == "orders":
        if customers is None:
            raise ValueError("Customer data must be provided for generating orders.")
        data = pd.DataFrame({
            'order_id': np.arange(num_rows),
            'customer_id': np.random.choice(customers['customer_id'], num_rows),
            'order_date': pd.to_datetime('2024-01-01') + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D'),
            'total_amount': np.random.uniform(10, 1000, num_rows),
            'status': np.random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled'], num_rows)
        })
    elif table_name == "items":
        data = pd.DataFrame({
            'item_id': np.arange(num_rows),
            'order_id': np.random.randint(0, num_rows, num_rows),
            'item_name': [f'Item_{i}' for i in range(num_rows)],
            'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], num_rows),
            'price': np.random.uniform(5, 500, num_rows),
        })
    elif table_name == "payments":
        data = pd.DataFrame({
            'payment_id': np.arange(num_rows),
            'order_id': np.random.randint(0, num_rows, num_rows),
            'payment_date': pd.to_datetime('2024-01-01') + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D'),
            'amount': np.random.uniform(10, 1000, num_rows),
            'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'UPI'], num_rows)
        })
    elif table_name == "shippings":
        data = pd.DataFrame({
            'shipping_id': np.arange(num_rows),
            'order_id': np.random.randint(0, num_rows, num_rows),
            'shipping_date': pd.to_datetime('2024-01-01') + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D'),
            'shipping_address': [f'Address_{i}' for i in range(num_rows)],
            'shipping_method': np.random.choice(['Standard', 'Express'], num_rows)
        })
    else:
        return None
    return data

def write_csv(data, file_path):
    """Writes DataFrame to a CSV file."""
    data.to_csv(file_path, index=False)

def estimate_row_size(data):
    """Estimate the average row size in bytes."""
    buffer = data.head(10)  # Take the first 10 rows to estimate size
    tmp_file = "temp_estimation.csv"
    buffer.to_csv(tmp_file, index=False)
    file_size = os.path.getsize(tmp_file)
    os.remove(tmp_file)
    avg_row_size = file_size / len(buffer)
    return avg_row_size

def generate_ecommerce_data(file_sizes_mb, output_dir):
    """Generates multiple CSV files of specified sizes with e-commerce data."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    table_names = ["customers", "orders", "items", "payments", "shippings"]

    for size_mb in file_sizes_mb:
        size_dir = os.path.join(output_dir, f"{size_mb}MB")
        os.makedirs(size_dir, exist_ok=True)

        # Generate customers first for other tables to reference
        customers = generate_data(10000, "customers")
        avg_row_size = estimate_row_size(customers)
        target_size_bytes = size_mb * 1024 * 1024
        num_rows_customers = math.ceil(target_size_bytes / avg_row_size)

        # Generate the full dataset for customers
        customers = generate_data(num_rows_customers, "customers")
        write_csv(customers, os.path.join(size_dir, "customers.csv"))
        
        print(f"Generated customers CSV with actual size: {os.path.getsize(os.path.join(size_dir, 'customers.csv')) / (1024 * 1024):.2f}MB")
        
        # Now generate other tables using the customer data
        for table_name in table_names[1:]:  # skip 'customers'
            if table_name == "orders":
                orders = generate_data(num_rows_customers, table_name, customers=customers)
                write_csv(orders, os.path.join(size_dir, "orders.csv"))
            else:
                orders = pd.read_csv(os.path.join(size_dir, "orders.csv"))
                orders_count = len(orders)
                table_data = generate_data(orders_count, table_name)
                write_csv(table_data, os.path.join(size_dir, f"{table_name}.csv"))
            
            print(f"Generated {table_name} CSV with actual size: {os.path.getsize(os.path.join(size_dir, f'{table_name}.csv')) / (1024 * 1024):.2f}MB")

# Example usage
file_sizes_mb = [1,10,150,300,500,1100]  # Adjust as needed
output_directory = "/content/ecommerce_data"

generate_ecommerce_data(file_sizes_mb, output_directory)
print(f"Data files generated in {output_directory}")

# Display a sample
sample_file = glob.glob(os.path.join(output_directory, "**/*.csv"), recursive=True)[0]
print(f"\nSample data from: {sample_file}")
print(pd.read_csv(sample_file).head())
