class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort(reverse=True)

        left, right = 0, len(tokens) - 1
        score = 0

        while left <= right:
            while left <= right and power >= tokens[right]:
                power -= tokens[right]
                right -= 1
                score += 1

            if left == right or score == 0:
                break

            if left < right and power + tokens[left] >= tokens[right]:
                power += tokens[left]
                left += 1
                score -= 1
            else:
                break

        return score
