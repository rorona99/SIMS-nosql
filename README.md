# SIMS-nosql
# NoSQL Implementation

This directory contains scripts, sample data, and queries for the MongoDB implementation of the Inventory Management System
## Purpose
The NoSQL implementation leverages MongoDB's flexibility and scalability for:
- Document-based storage of hierarchical data.
- Simplifying data relationships without foreign keys.
- Efficient querying using aggregation pipelines and `$lookup`.

## Connection to previous steps
- This section focuses on implementing and demonstrating the system's functionality in a NoSQL environment.
- Highlights include:
  - Flexible schema design for collections.
  - Querying capabilities for data analysis and visualization.

## Files
1. **`setup_mongodb.py`**:  
   - Script to create and populate collections for `Products`, `Suppliers`, `SalesOrders`, and `Customers`.

2. **`queries.py`**:  
   - Examples of MongoDB queries for:
     - Aggregating product categories.
     - Identifying low-stock items.
     - Combining sales orders and customer details.
