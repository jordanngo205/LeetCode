# Write your MySQL query statement below
SELECT 
(Select DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1)
As SecondHighestSalary;