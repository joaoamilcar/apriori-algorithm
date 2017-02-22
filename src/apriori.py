from itertools import combinations


class Apriori:
    def __init__(self, items, transactions, min_s, min_c):
        self.items = items
        self.transactions = transactions
        self.frequent_itemset = {1: []}
        self.min_s = min_s # minimum support value for a rule
        self.min_c = min_c # minimum confidence value for a rule

    def get_frequent_itemset(self):
        k = 2
        candidates = list(self.items.keys())
        print("candidates", candidates)

        for c in candidates:
            if self.support([c]) >= self.min_s:
                new_list = self.frequent_itemset.get(k - 1)
                new_list.append(c)
                self.frequent_itemset = {k - 1: new_list}

        print("frequent itemset", self.frequent_itemset)

        while self.frequent_itemset.get(k - 1) != None:
            print("# -----------------------")
            candidates_list = group(self.frequent_itemset.get(k - 1), k)

            for c in candidates_list:
                frequent = True

                if k > 2:
                    frequent = self.is_frequent_candidate(c, k)

                if frequent:
                    # first attribution. initialize key k with an empty list
                    if k not in self.frequent_itemset:
                        self.frequent_itemset[k] = []

                    if self.support(c) >= self.min_s:
                        new_list = self.frequent_itemset.get(k)
                        new_list.append(c)
                        self.frequent_itemset[k] = new_list

            k += 1

            print("frequent itemset", self.frequent_itemset)

    # pruning
    def is_frequent_candidate(self, candidate, k):
        combinations_list = combinations(candidate, k - 1)
        print("for candidate", candidate)

        for tuple in combinations_list:
            print("tuple", tuple)

            if tuple not in self.frequent_itemset.get(k - 1):
                print("not in", self.frequent_itemset.get(k - 1))
                return False

        return True

    def support(self, rule):
        count = 0

        for key, value in self.transactions.items():
            if set(rule).issubset(set(value)):
                count += 1

        return count / len(self.transactions)


def group(tuples_list, k):
    if k > 2:
        result_tuple = ()

        for t in tuples_list:
            result_tuple = result_tuple + t

        print("candidates", list(combinations(set(result_tuple), k)))
        return list(combinations(set(result_tuple), k))

    print("candidates", list(combinations(tuples_list, 2)))
    return list(combinations(tuples_list, 2))
