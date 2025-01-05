from collections import defaultdict, Counter
from itertools import combinations
from typing import List
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: Sort by timestamp and group visits by username
        sorted_data = sorted(zip(timestamp, username, website))
        visit_map = defaultdict(list)
        for _, user, web in sorted_data:
            visit_map[user].append(web)

        # Step 2: Generate all 3-sequences and count their occurrences
        pattern_count = Counter()
        for visits in visit_map.values():
            # Use set to avoid counting duplicate patterns for a single user
            unique_patterns = set(combinations(visits, 3))
            for pattern in unique_patterns:
                pattern_count[pattern] += 1

        # Step 3: Sort by count (descending), then lexicographically
        sorted_patterns = sorted(pattern_count.items(), key=lambda x: (-x[1], x[0]))

        # Step 4: Return the most frequent pattern
        return list(sorted_patterns[0][0])
