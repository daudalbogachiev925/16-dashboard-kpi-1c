SELECT c.name, SUM(s.amount) AS revenue
FROM sales s JOIN customers c ON c.id = s.customer_id
GROUP BY c.id
ORDER BY revenue DESC
LIMIT 10;
