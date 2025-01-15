class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        transaction_map = {}

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")

            if not name in transaction_map:
                
                transaction_map[name] = []

            transaction_map[name].append((int(time), city, int(amount), transaction))

        for transaction_list in transaction_map.values():
            invalid_set = []

            for i in range(len(transaction_list)):
                time1, city1, amount1, transaction1 = transaction_list[i]
                isInvalid = False

                if amount1 > 1000:
                    isInvalid = True

                for j in range(len(transaction_list)):
                    if isInvalid:
                        break

                    if i == j:
                        continue

                    time2, city2, _, transaction2 = transaction_list[j]

                    if abs(time2 - time1) <= 60 and city1 != city2:
                        isInvalid = True                        

                if isInvalid:
                    invalid_set.append(transaction1)

            res.extend(invalid_set)

        return res

            