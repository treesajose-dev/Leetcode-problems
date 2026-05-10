# Write your MySQL query statement below


SELECT MAX(num) AS num
FROM MyNumbers where num in (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
);