class Solution:
    def myPow(self, x: float, n: int) -> float:
        # isNeg = n < 0
        # n = abs(n)

        # def modular_exponentation(base, exp):
        #     res = 1

        #     while exp > 0:
        #         if exp % 2 == 1:
        #             res *= base
        #         base *= base
        #         exp //= 2

        #     return res

        # res = modular_exponentation(x, n)

        # return 1 / res if isNeg else res

        is_negative = n < 0
        n = abs(n)

        def modular_exponentation(base, exp):
            res = 1

            while exp > 0:
                if exp % 2 == 1:
                    res *= base
                base *= base
                exp //= 2

            return res

        res = modular_exponentation(x, n)

        return 1 / res if is_negative else res 