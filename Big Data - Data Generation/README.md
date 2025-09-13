# Big-Data-Course


E-commerce Data for Spark Operations
====================================

This repository contains a set of **e-commerce data** CSV files designed for teaching purposes. The data is modeled to simulate a real-world e-commerce business, and it is structured in a way that allows you to demonstrate various **Spark operations** and data manipulations.

The data covers multiple entities like **customers**, **orders**, **items**, **payments**, and **shippings**, and is available in multiple sizes to allow for different use cases in Spark processing.

Table of Contents
-----------------

1.  [Overview]
2.  [Data Schema]
3.  [Data Generation]
4.  [File Structure and Sizes]
5.  [Spark Block Partitioning]
6.  [Real-World Data Modeling]
7.  [How to Use]
8.  [Learning Goals]

* * * * *

Overview
--------

The data in this repository simulates a **real-world e-commerce system** with multiple interconnected tables. This data has been intentionally designed with the following goals:

-   **Large-scale Data**: Files are generated in different sizes to test and demonstrate Spark's ability to scale and partition data.
-   **Multiple Joins**: Tables are designed with key relationships (e.g., `customer_id`, `order_id`) to demonstrate joins and other Spark operations.
-   **Data Partitioning**: The data size is controlled to mimic real-world scenarios where files are large but can be divided into multiple blocks in a distributed system.

By using these datasets, you can demonstrate Spark's capabilities in handling distributed data processing, partitioning, joining, and aggregating across large datasets.

* * * * *

Data Schema
-----------

### Customers Table

The `customers.csv` file contains details about the customers, including:

-   `customer_id`: Unique identifier for each customer.
-   `name`: Customer's name.
-   `city`: The city where the customer resides.
-   `state`: The state of the customer.
-   `country`: Country of the customer (set to India for all customers).
-   `registration_date`: Date when the customer registered.
-   `is_active`: Whether the customer is currently active or not.

### Orders Table

The `orders.csv` file contains information about customer orders:

-   `order_id`: Unique identifier for each order.
-   `customer_id`: Link to the `customers` table to indicate which customer placed the order.
-   `order_date`: The date the order was placed.
-   `total_amount`: The total amount of the order.
-   `status`: The current status of the order (e.g., "Pending", "Shipped", "Delivered", "Cancelled").

### Items Table

The `items.csv` file contains details about the items in each order:

-   `item_id`: Unique identifier for each item.
-   `order_id`: Link to the `orders` table to indicate which order the item belongs to.
-   `item_name`: Name of the item.
-   `category`: Category of the item (e.g., "Electronics", "Clothing").
-   `price`: The price of the item.

### Payments Table

The `payments.csv` file contains payment-related information:

-   `payment_id`: Unique identifier for each payment.
-   `order_id`: Link to the `orders` table to indicate which order the payment is for.
-   `payment_date`: The date the payment was made.
-   `amount`: The payment amount.
-   `payment_method`: The method of payment (e.g., "Credit Card", "Debit Card", "UPI").

### Shippings Table

The `shippings.csv` file contains shipping details:

-   `shipping_id`: Unique identifier for each shipping.
-   `order_id`: Link to the `orders` table to indicate which order the shipping is associated with.
-   `shipping_date`: The date the shipping was made.
-   `shipping_address`: Address where the order was shipped.
-   `shipping_method`: The method used for shipping (e.g., "Standard", "Express").

* * * * *

Data Generation
---------------

The data was generated with the following assumptions:

1.  **Realistic Customer Distribution**: Customers are distributed across different cities and states in India. The registration date is randomized within a one-year period.
2.  **Order and Item Relationships**: Each order is linked to a customer, and each item is linked to an order.
3.  **Payment and Shipping**: Payments and shippings are linked to orders, and their dates are also randomized within the same time frame.
4.  **File Size Control**: Files are generated to meet specific size requirements (e.g., 1MB, 10MB, 150MB, 300MB, 500MB, 1100MB) for Spark demonstration purposes.

* * * * *

File Structure and Sizes
------------------------

The dataset is organized in the following directory structure:

```
ecommerce_data/
├── 1MB/
│   ├── customers.csv  (1.1MB)
│   ├── orders.csv     (844KB)
│   ├── items.csv      (817KB)
│   ├── payments.csv   (835KB)
│   └── shippings.csv  (752KB)
├── 10MB/
│   ├── customers.csv  (11MB)
│   ├── orders.csv     (8.3MB)
│   ├── items.csv      (8.2MB)
│   ├── payments.csv   (8.2MB)
│   └── shippings.csv  (7.6MB)
├── 150MB/
│   ├── customers.csv  (161MB)
│   ├── orders.csv     (133MB)
│   ├── items.csv      (135MB)
│   ├── payments.csv   (132MB)
│   └── shippings.csv  (126MB)
├── 300MB/
│   ├── customers.csv  (328MB)
│   ├── orders.csv     (271MB)
│   ├── items.csv      (276MB)
│   ├── payments.csv   (269MB)
│   └── shippings.csv  (257MB)
├── 500MB/
│   ├── customers.csv  (545MB)
│   ├── orders.csv     (451MB)
│   ├── items.csv      (459MB)
│   ├── payments.csv   (447MB)
│   └── shippings.csv  (428MB)
├── 1100MB/
│   ├── customers.csv  (1.1GB)
│   ├── orders.csv     (1GB)
│   ├── items.csv      (1.1GB)
│   ├── payments.csv   (978MB)
│   └── shippings.csv  (1.0GB)

```

-   **1MB to 1100MB folders**: These represent different target file sizes, used to simulate real-world data sizes.
-   **CSV files**: Each folder contains CSV files corresponding to the tables described in the schema above.

* * * * *

Spark Block Partitioning
------------------------

In Spark, data is distributed across **blocks** during processing. Each block typically corresponds to a portion of the data stored in HDFS (Hadoop Distributed File System) or another distributed storage system.

-   **Spark Partitioning**: When working with large datasets, Spark splits the data into smaller **partitions** or **blocks** to ensure parallel processing.
-   The default block size in Spark is **128MB**. If a file exceeds this size, it is split into multiple blocks.

In this dataset:

-   **1MB - 10MB files** will fit into **1 block** each.
-   **150MB - 500MB files** will span **1 to 2 blocks**.
-   **1100MB files** will span **8 to 9 blocks**.

The file size distribution allows you to demonstrate how Spark processes data across multiple partitions and blocks.

* * * * *

Real-World Data Modeling
------------------------

### Customer-Order Relationship:

-   **Customers and Orders** are linked by `customer_id`. Each order has one customer, but a customer can have multiple orders.
-   This relationship allows you to demonstrate **joins** and **grouped aggregations** (e.g., total sales per customer).

### Orders-Item Relationship:

-   **Orders and Items** are linked by `order_id`. Each order can contain multiple items, making this a **one-to-many** relationship.
-   Demonstrate **inner joins** to fetch items associated with an order.

### Payment and Shipping:

-   **Payments and Shippings** are linked to **Orders**. Each order can have one payment and one shipping, which helps demonstrate **join operations** across multiple tables.

* * * * *

How to Use
----------

1.  Clone the repository:

    ```
    git clone <repository-url>

    ```

2.  Load the data into Spark: You can load any of these files into **Spark DataFrames** for analysis. Example code to load data into Spark:

    ```
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("EcommerceData").getOrCreate()

    # Example to load the customers file
    customers_df = spark.read.option("header", "true").csv("path/to/ecommerce_data/150MB/customers.csv")

    # Show the data
    customers_df.show(5)

    ```

3.  Perform operations: Use Spark's **DataFrame API** to demonstrate various operations like **filtering**, **aggregations**, **joins**, and more.

* * * * *

Learning Goals
--------------

1.  **Data Partitioning in Spark**: Understand how Spark splits data into blocks/partitions based on file size. 
2. **Spark Joins**: Practice performing joins between related tables, such as joining `orders` with `items` and `payments`. 
3. **Scalable Data Processing**: Work with large datasets and understand how Spark handles data across a distributed system. 
4. **Optimizing Spark Jobs**: Learn how to optimize job execution by understanding partitioning and parallel processing.

