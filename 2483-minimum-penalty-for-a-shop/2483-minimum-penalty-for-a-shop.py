class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        counts = [0] * n

        n_count = 0
        y_count = 0

        for i, c in enumerate(customers):
            if c == "N":
                n_count += 1
            else:
                y_count += 1

            counts[i] = n_count

        min_count = n_count
        h = n
        y_count2 = 0

        for i in range(n - 1, 0, -1):
            if customers[i] == "Y":
                y_count2 += 1
            if y_count2 + counts[i - 1] <= min_count:
                h = i
                min_count = y_count2 + counts[i - 1]

        return h if min_count < y_count else 0


        