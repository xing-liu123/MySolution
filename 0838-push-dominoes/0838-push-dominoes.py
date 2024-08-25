class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = []

        prev = "."
        last_done = -1
        for i, d in enumerate(dominoes):
            if not res:
                if d != ".":
                    if d == "L":
                        res += ["L"] * (i + 1)
                        prev = "L"
                    else:
                        res += ["."] * i
                        res.append("R")
                        prev = "R"
                    last_done = i
            else:
                if d != ".":
                    if last_done == i - 1:
                        res.append(d)

                    else:
                        if prev == "L" and d == "R":
                            res += ["."] * (i - last_done - 1)
                            res.append(d)

                        elif prev == "R" and d == "L":                            
                            res += ["R"] *  ((i - last_done - 1) // 2)
                            if (i - last_done) % 2 == 0:
                                res.append(".")
                            res += ["L"] *  ((i - last_done - 1) // 2 + 1)
                            
                        else:
                            res += [d] * (i - last_done)
                    prev = d
                    last_done = i

        if last_done != len(dominoes) - 1:
            
            if prev == "R":
                res += ["R"] * (len(dominoes) - last_done - 1)
            else:

                res += ["."] * (len(dominoes) - last_done - 1)

        return "".join(res)
                            



                    

            

