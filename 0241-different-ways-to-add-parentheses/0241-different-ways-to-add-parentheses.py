class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(expression):
            if expression in memo:
                return memo[expression]

            results = []

            for i, c in enumerate(expression):
                if c in "+-*":
                    left_results = compute(expression[:i])
                    right_results = compute(expression[i + 1:])

                    for left in left_results:
                        for right in right_results:
                            if c == "+":
                                results.append(left + right)
                            elif c == "-":
                                results.append(left - right)
                            else:
                                results.append(left * right)

            if not results:
                results.append(int(expression))

            memo[expression] = results
            return results

        return compute(expression)
                    