from itertools import combinations


class Apriori:
    def __init__(self, items, transactions, smin, cmin):
        self.items = items
        self.transactions = transactions
        self.frequent_items_dict = {}
        self.smin = smin # valor mínimo de suporte admitido para uma regra
        self.cmin = cmin # valor mínimo de confiança admitido para uma regra

    def get_cif(self):
        k = 2
        candidates = list(self.items.keys())
        # candidates = list(combinations(self.items.keys(), 1))

        print("candidates", candidates)

        for candidate in candidates:
            # first attribution
            if (k - 1) not in self.frequent_items_dict:
                self.frequent_items_dict[k - 1] = []

            if self.suporte([candidate]) >= self.smin:
                newCif = self.frequent_items_dict.get(k - 1)
                newCif.append(candidate)
                self.frequent_items_dict = {k - 1: newCif}

        print("dict", self.frequent_items_dict)

        while self.frequent_items_dict.get(k - 1) != None:
            candidates_list = self.group(self.frequent_items_dict.get(k - 1), k)
            # print("groups", k, group_list)

            for candidate in candidates_list:
                frequent_candidate = True

                if k > 2:
                    frequent_candidate = self.is_frequent_candidate(candidate, k)

                if frequent_candidate:
                    # first attribution
                    if k not in self.frequent_items_dict:
                        self.frequent_items_dict[k] = []

                    if self.suporte(candidate) >= self.smin:
                        newCif = self.frequent_items_dict.get(k)
                        newCif.append(candidate)
                        self.frequent_items_dict[k] = newCif

            k += 1

            print("dict", self.frequent_items_dict)

    # poda
    def is_frequent_candidate(self, candidate, k):
        list_combinations = combinations(candidate, k - 1)
        # print("listcomb",list(list_combinations))

        for tuple in list_combinations:
            # print("tuple", set(tuple), "subset of", set(frequent_items_dict.get(k - 1)), set(tuple).issubset(set(frequent_items_dict.get(k - 1))))

            if tuple not in self.frequent_items_dict.get(k - 1):
                print("for candidate", candidate, "tuple", tuple, "not in", self.frequent_items_dict.get(k - 1))
                return False

        return True

    def group(self, L, k):
        # print("quero:")
        # print("L", L)
        # print("k", k)

        LC = list(combinations(L, 2))

        if k > 2:
            resultSet = ()

            for tuple in L:
                resultSet = resultSet + tuple

            print("candidates k>2", list(combinations(set(resultSet), k)))
            return list(combinations(set(resultSet), k))

        print("candidates k<=2", LC)

        return LC

    def suporte(self, rule):
        count = 0

        for key, value in self.transactions.items():
            if set(rule).issubset(set(value)):
                count += 1

        return count / len(self.transactions)
