# Write your MySQL query statement below
SELECT f.followee AS follower, COUNT(*) as num
FROM Follow as f
WHERE f.followee in (
    SELECT DISTINCT follower
    FROM Follow
)
GROUP BY f.followee
ORDER BY f.followee