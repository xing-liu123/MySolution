class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        total_even = (n + 1) // 2
        total_odd = n // 2

        def modular_exponentation(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod

                base = (base * base) % mod
                exp //= 2
            
            return result

        power_of_5 = modular_exponentation(5, total_even, MOD)
        power_of_4 = modular_exponentation(4, total_odd, MOD)

        return (power_of_5 * power_of_4) % MOD