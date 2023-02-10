WITH RECURSIVE dates_cte (date) AS (
  SELECT '2022-01-01' AS date
  UNION ALL
  SELECT DATE_ADD(date, INTERVAL 1 DAY)
  FROM dates_cte
  WHERE date < '2022-12-31'
)
SELECT date
FROM dates_cte;

WITH dates_cte (date) AS (
  SELECT DATE('2022-01-01')
  UNION ALL
  SELECT date + 1 DAY
  FROM dates_cte
  WHERE date < DATE('2022-12-31')
)
SELECT date
FROM dates_cte;