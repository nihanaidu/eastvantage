import pandas as pd
import sqlite3

# Connect to SQLite3 database
conn = sqlite3.connect('sales_database.db')

#SQL query
query = """
    SELECT c.customer_id, c.age, i.item_name, SUM(o.quantity) as total_quantity
    FROM Customer c
    JOIN Sales s ON c.customer_id = s.customer_id
    JOIN Orders o ON s.sales_id = o.sales_id
    JOIN Items i ON o.item_id = i.item_id
    WHERE c.age BETWEEN 18 AND 35 AND o.quantity IS NOT NULL
    GROUP BY c.customer_id, i.item_id
"""

df = pd.read_sql_query(query, conn)

# Filter out rows
df = df[df['total_quantity'] > 0]

df.to_csv('output.csv', sep=';', index=False)

conn.close()
