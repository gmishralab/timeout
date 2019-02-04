--By Product
SELECT
       TotalRevenue = SUM(s.quantity * p.price)
       ,s.product
FROM Sales1 AS s
CROSS APPLY
(
       SELECT TOP (1) * FROM Prices AS p
       WHERE p.product = s.product
       AND p.price_effective_date <= s.sales_date
       ORDER BY p.price_effective_date DESC
) AS p
group by s.product;
 
--Total Revenue
SELECT
       TotalRevenue = SUM(s.quantity * p.price)
FROM Sales1 AS s
CROSS APPLY
(
       SELECT TOP (1) * FROM Prices AS p
       WHERE p.product = s.product
       AND p.price_effective_date <= s.sales_date
       ORDER BY p.price_effective_date DESC
) AS p;
 