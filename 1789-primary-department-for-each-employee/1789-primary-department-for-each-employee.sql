WITH cte AS (
  SELECT
    employee_id,
    department_id,
    primary_flag,
    COUNT(*) OVER (PARTITION BY employee_id) AS dept_cnt
  FROM Employee
)
SELECT employee_id, department_id
FROM cte
WHERE primary_flag = 'Y' OR dept_cnt = 1;
