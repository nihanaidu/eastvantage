-- Connect to the SQLite database
ATTACH DATABASE 'company_xyz.db' AS company;

SELECT c.customer_id, c.age, i.item_name, SUM(o.quantity) AS total_quantity
FROM company.Customer c
JOIN company.Sales s ON c.customer_id = s.customer_id
JOIN company.Orders o ON s.sales_id = o.sales_id
JOIN company.Items i ON o.item_id = i.item_id
WHERE c.age BETWEEN 18 AND 35
GROUP BY c.customer_id, i.item_name
HAVING total_quantity > 0;
