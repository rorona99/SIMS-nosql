# Access or create a database
db = client["InventoryManagement"]

# Access or create a collection
products = db["Products"]
suppliers = db["Suppliers"]
salesorders = db["SalesOrder"]
customers = db["Customers"]

print("Connected to MongoDB!")

product_list = [
    { "_id": 101, "ProductID":521, "Name": "mind", "Type": "Clothing", "AvailableQuantity": 80, "PurchasePrice": 487.8, "RestockLeadTime":12, "SupplierID": 629 },
    { "_id": 102, "ProductID":254, "Name": "participant", "Type": "Clothing", "AvailableQuantity": 96, "PurchasePrice": 442.9, "RestockLeadTime":7, "SupplierID": 259 },
    { "_id": 103, "ProductID":605, "Name": "word", "Type": "Electronics", "AvailableQuantity": 71, "PurchasePrice": 383.29, "RestockLeadTime":8,"SupplierID": 529 },
    { "_id": 104, "ProductID":182, "Name": "operation", "Type": "Furniture", "AvailableQuantity": 92, "PurchasePrice": 421.6, "RestockLeadTime":8,"SupplierID": 699 },
    { "_id": 105, "ProductID":244, "Name": "hair", "Type": "Clothing", "AvailableQuantity": 37, "PurchasePrice": 185.34, "RestockLeadTime":5,"SupplierID": 751 },
    { "_id": 106, "ProductID":419, "Name": "new", "Type": "Electronics", "AvailableQuantity": 56, "PurchasePrice": 488.03, "RestockLeadTime":2,"SupplierID": 629 },
    { "_id": 107, "ProductID":980, "Name": "catch", "Type": "Toys", "AvailableQuantity": 73, "PurchasePrice": 160.49, "RestockLeadTime":1,"SupplierID": 683 },
    { "_id": 108, "ProductID":759, "Name": "force", "Type": "Toys", "AvailableQuantity": 42, "PurchasePrice": 111.0, "RestockLeadTime":11,"SupplierID": 208 },
    { "_id": 109, "ProductID":944, "Name": "nice", "Type": "Electronics", "AvailableQuantity": 57, "PurchasePrice": 457.58, "RestockLeadTime":1,"SupplierID": 365},
    { "_id": 110, "ProductID":425, "Name": "American", "Type": "Toys", "AvailableQuantity": 37, "PurchasePrice": 443.42, "RestockLeadTime":1,"SupplierID": 231 },
    { "_id": 111, "ProductID":850, "Name": "performance", "Type": "Toys", "AvailableQuantity": 7, "PurchasePrice": 173.63, "RestockLeadTime":11,"SupplierID": 365 },
    { "_id": 112, "ProductID":367, "Name": "on", "Type": "Toys", "AvailableQuantity": 62, "PurchasePrice": 15.36, "RestockLeadTime":11,"SupplierID": 144 },
    { "_id": 113, "ProductID":278, "Name": "dinner", "Type": "Clothing", "AvailableQuantity": 2, "PurchasePrice": 209.47, "RestockLeadTime":11,"SupplierID": 699 },
    { "_id": 114, "ProductID":10, "Name": "project", "Type": "Furniture", "AvailableQuantity": 73, "PurchasePrice": 221.29, "RestockLeadTime":14,"SupplierID": 933 },
    { "_id": 115, "ProductID":528, "Name": "hear", "Type": "Toys", "AvailableQuantity": 78, "PurchasePrice": 362.56, "RestockLeadTime":4,"SupplierID": 259 }
]

# Insert documents with duplicate check
for product in product_list:
    if products.find_one({"_id": product["_id"]}):
        print(f"Document with _id {product['_id']} already exists. Skipping insertion.")
    else:
        products.insert_one(product)
        print(f"Document with _id {product['_id']} inserted successfully!")

supplier_list = [
    {"_id": 201, "SupplierID":365, "Name": "Taylor, Rose and Chavez", "Address": "29097 Rodney Points Suite 681 West Isaacmouth, SC 88782", "Location": "Kristenbury"},
    {"_id": 202, "SupplierID":935, "Name": "Martin LLC", "Address": "50396 Garcia Station Port Tylershire, CT 35914", "Location": "East Amymouth"},
    {"_id": 203, "SupplierID":832, "Name": "Mullen-Martin", "Address": "572 Sanchez Centers South Matthew, MN 90445", "Location": "Brianstad"},
    {"_id": 204, "SupplierID":998, "Name": "Atkinson-Roman", "Address": "3208 John Harbor Lake Tina, OR 80456", "Location": "North Denise"},
    {"_id": 205, "SupplierID":683, "Name": "Steele-Riley", "Address": "19014 Ward Manor New Ashleyland, DC 63955", "Location": "New Tammy"},
    {"_id": 206, "SupplierID":44, "Name": "Adams and Sons", "Address": "65010 Samuel Ridge Suite 682 Annetown, PW 91042", "Location": "Port Shannon"},
    {"_id": 207, "SupplierID":529, "Name": "Leonard and Sons", "Address": "049 Elizabeth Stravenue Apt. 734 Watkinsfurt, DC 66443", "Location": "East Charles"},
    {"_id": 208, "SupplierID":699, "Name": "Nelson, Fletcher and Graves", "Address": "4393 Jonathan Curve Apt. 178 Clarkburgh, MS 49119", "Location": "Walshborough"},
    {"_id": 209, "SupplierID":629, "Name": "Ramirez PLC", "Address": "89423 Jennifer Land Bakerbury, IL 73283", "Location": "Lake David"},
    {"_id": 210, "SupplierID":186, "Name": "Woods, Martinez and Baldwin", "Address": "788 Matthew Courts Brucemouth, MA 78854", "Location": "Lake Brettmouth"},
    {"_id": 211, "SupplierID":751, "Name": "Glenn Inc", "Address": "85831 Brian Row Suite 721 North Michaelshire, NM 09947", "Location": "South Henryfort"},
    {"_id": 212, "SupplierID":208, "Name": "Hansen Inc", "Address": "8078 Anthony Row Suite 732 Jasmintown, FM 66346", "Location": "East Gregory"},
    {"_id": 213, "SupplierID":933, "Name": "Williams-Hoffman", "Address": "60196 James Curve Lake Brittanyberg, VT 02810", "Location": "Amytown"},
    {"_id": 214, "SupplierID":950, "Name": "Smith Ltd", "Address": "03047 Hernandez Passage South Diane, LA 29249", "Location": "Lydiaberg"},
    {"_id": 215, "SupplierID":231, "Name": "Mccoy, Craig and Blake", "Address": "9699 Richardson Loop Clarkview, ME 56047", "Location": "Moranshire"}
] 

for supplier in supplier_list:
    # Check for duplicate based on `_id` or `SupplierID`
    if suppliers.find_one({"_id": supplier["_id"]}) or suppliers.find_one({"SupplierID": supplier["SupplierID"]}):
        print(f"Document with _id {supplier['_id']} or SupplierID {supplier['SupplierID']} already exists. Skipping insertion.")
    else:
        suppliers.insert_one(supplier)
        print(f"Document with _id {supplier['_id']} inserted successfully!")

salesorder_list = [
    {"_id": 301, "SalesOrderID":376, "OrderDate": "2024-06-21", "TotalAmount": 313.98, "CustomerID": 485},
    {"_id": 302, "SalesOrderID":560, "OrderDate": "2024-04-21", "TotalAmount": 212.2, "CustomerID": 214},
    {"_id": 303, "SalesOrderID":74, "OrderDate": "2024-10-20", "TotalAmount": 742.26, "CustomerID": 584},
    {"_id": 304, "SalesOrderID":229, "OrderDate": "2024-02-10", "TotalAmount": 46.15, "CustomerID": 414},
    {"_id": 305, "SalesOrderID":332, "OrderDate": "2024-03-02", "TotalAmount": 709.89, "CustomerID": 134},
    {"_id": 306, "SalesOrderID":888, "OrderDate": "2024-04-11", "TotalAmount": 657.33, "CustomerID": 227},
    {"_id": 307, "SalesOrderID":430, "OrderDate": "2024-08-8", "TotalAmount": 413.05, "CustomerID": 984},
    {"_id": 308, "SalesOrderID":778, "OrderDate": "2024-03-31", "TotalAmount": 989.20, "CustomerID": 809},
    {"_id": 309, "SalesOrderID":822, "OrderDate": "2024-02-09", "TotalAmount": 979.60, "CustomerID": 834},
    {"_id": 310, "SalesOrderID":705, "OrderDate": "2024-12-17", "TotalAmount": 356.37, "CustomerID": 667},
    {"_id": 311, "SalesOrderID":999, "OrderDate": "2024-11-28", "TotalAmount": 868.88, "CustomerID": 834},
    {"_id": 312, "SalesOrderID":593, "OrderDate": "2024-04-23", "TotalAmount": 145.05, "CustomerID": 405},
    {"_id": 313, "SalesOrderID":2, "OrderDate": "2024-04-14", "TotalAmount": 34.68, "CustomerID": 411},
    {"_id": 314, "SalesOrderID":885, "OrderDate": "2024-08-07", "TotalAmount": 921.14, "CustomerID": 984},
    {"_id": 315, "SalesOrderID":417, "OrderDate": "2024-08-17", "TotalAmount": 638.69, "CustomerID": 225}
]

for salesorder in salesorder_list:
    # Check for duplicate based on `_id` or `SalesorderID`
    if salesorders.find_one({"_id": salesorder["_id"]}) or suppliers.find_one({"SalesOrderID": salesorder["SalesOrderID"]}):
        print(f"Document with _id {salesorder['_id']} or SalesOrderID {salesorder['SalesOrderID']} already exists. Skipping insertion.")
    else:
        salesorders.insert_one(salesorder)
        print(f"Document with _id {salesorder['_id']} inserted successfully!")

customer_list = [
    {"_id": 401, "CustomerID":803, "Name": "Andrea Fleming", "ContactDetails": "+1-475-454-7266"},
    {"_id": 402, "CustomerID":162, "Name": "Laurie Bennett", "ContactDetails": "(440)257-8485x5112"},
    {"_id": 403, "CustomerID":584, "Name": "Jennifer Arnold", "ContactDetails": "758.424.8703"},
    {"_id": 404, "CustomerID":438, "Name": "Jennifer Rodriguez", "ContactDetails": "001-517-389-5879x592"},
    {"_id": 405, "CustomerID":227, "Name": "Brian Cooper", "ContactDetails": "(466)940-4004x31664"},
    {"_id": 406, "CustomerID":405, "Name": "Nicole Gonzalez", "ContactDetails": "(793)337-5971"},
    {"_id": 407, "CustomerID":485, "Name": "Gina Cole", "ContactDetails": "386.917.4536x06449"},
    {"_id": 408, "CustomerID":214, "Name": "Melinda Moore", "ContactDetails": "973-843-3613x1132"},
    {"_id": 409, "CustomerID":893, "Name": "Ronald Williams", "ContactDetails": "(798)271-6935"},
    {"_id": 410, "CustomerID":140, "Name": "Robert Mason", "ContactDetails": "967.456.4614"},
    {"_id": 411, "CustomerID":491, "Name": "Kevin Simpson", "ContactDetails": "+1-270-509-0780x705"},
    {"_id": 412, "CustomerID":667, "Name": "Beth Fuller", "ContactDetails": "001-504-602-9290x476"},
    {"_id": 413, "CustomerID":484, "Name": "Julie Hobbs", "ContactDetails": "485-841-0743"},
    {"_id": 414, "CustomerID":411, "Name": "Donald Petersen", "ContactDetails": "001-619-690-4793x32416"},
    {"_id": 415, "CustomerID":483, "Name": "James Villanueva", "ContactDetails": "275-903-2518x67448"}
]

for customer in customer_list:
    # Check for duplicate based on `_id` or `SalesorderID`
    if customers.find_one({"_id": customer["_id"]}) or customers.find_one({"CustomerID": customer["CustomerID"]}):
        print(f"Document with _id {customer['_id']} or CustomerID {customer['CustomerID']} already exists. Skipping insertion.")
    else:
        customers.insert_one(customer)
        print(f"Document with _id {customer['_id']} inserted successfully!")





