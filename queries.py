low_stock_products = products.find({"AvailableQuantity": {"$lt": 20}})
for product in low_stock_products:
    print(product)

supplier_products = products.find({"SupplierID": 1})
for product in supplier_products:
    print(product)

average_price_by_supplier = products.aggregate([
    {"$group": {"_id": "$SupplierID", "AveragePurchasePrice": {"$avg": "$PurchasePrice"}}}
])
for result in average_price_by_supplier:
    print(result)

sales_orders_with_customers = salesorders.aggregate([
    {"$lookup": {
        "from": "Customers",  # Collection to join
        "localField": "CustomerID",  # Field in SalesOrder
        "foreignField": "CustomerID",  # Field in Customers
        "as": "CustomerDetails"  # Output array field
    }}
])
for sales_order in sales_orders_with_customers:
    print(sales_order)

products_by_type = products.aggregate([
    {"$group": {"_id": "$Type", "Count": {"$sum": 1}}}
])
for result in products_by_type:
    print(result)

