# Write your MySQL query statement below
SELECT
  f.followee AS follower,         -- the user
  COUNT(*)    AS num   -- how many people follow them
FROM Follow AS f
WHERE f.followee IN (             -- they must follow someone
  SELECT DISTINCT follower
  FROM Follow
)
GROUP BY f.followee
ORDER BY follower;