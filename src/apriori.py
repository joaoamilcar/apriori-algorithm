from itertools import combinations, chain
from builtins import print


class Apriori:
    def __init__(self, items, transactions, min_s, min_c):
        self.items = items
        self.transactions = transactions
        self.frequent_itemset_dict = {1: []}
        self.min_s = min_s # minimum support value for a rule
        self.min_c = min_c # minimum confidence value for a rule

    def run(self):
        frequent_itemset = self.get_frequent_itemset()

        self.get_association_rules(frequent_itemset);

    def get_frequent_itemset(self):
        k = 2
        candidates = list(self.items.keys())
        print("candidates", candidates)

        for c in candidates:
            if self.support([c]) >= self.min_s:
                new_list = self.frequent_itemset_dict.get(k - 1)
                new_list.append(c)
                self.frequent_itemset_dict = {k - 1: new_list}

        print("frequent itemset dict", self.frequent_itemset_dict)

        while self.frequent_itemset_dict.get(k - 1) != None:
            print("# -----------------------")
            candidates = group(self.frequent_itemset_dict.get(k - 1), k)

            for c in candidates:
                frequent = True

                if k > 2:
                    frequent = self.is_frequent_candidate(c, k)

                if frequent:
                    if k not in self.frequent_itemset_dict:
                        self.frequent_itemset_dict[k] = [] # initialize key k with an empty list

                    if self.support(c) >= self.min_s:
                        new_list = self.frequent_itemset_dict.get(k)
                        new_list.append(c)
                        self.frequent_itemset_dict[k] = new_list

            print("frequent itemset dict", self.frequent_itemset_dict)
            k += 1

        return self.frequent_itemset_dict.get(k - 2)

    # pruning
    def is_frequent_candidate(self, candidate, k):
        combinations_list = combinations(candidate, k - 1)
        print("for candidate", candidate)

        for tuple in combinations_list:
            print("tuple", tuple)

            if tuple not in self.frequent_itemset_dict.get(k - 1):
                print("not in", self.frequent_itemset_dict.get(k - 1))
                return False

        return True

    def get_association_rules(self, itemset):
        partitions = lambda tup: chain.from_iterable(combinations(tup, x) for x in range(1, len(tup))) # proper item not included

        for item in itemset:
            print("# -----------------------")
            print(list(partitions(item)))
            for p in partitions(item):
                if self.confidence(item, p) >= self.min_c:
                    print("rule", p, "->", tuple(set(item) - set(p)))
                    print("confidence", self.confidence(item, p))
                    print("lift", self.lift(item, p, set(item) - set(p)))

    def support(self, rule):
        count = 0

        for key, value in self.transactions.items():
            if set(rule).issubset(set(value)):
                count += 1

        return count / len(self.transactions)

    def confidence(self, rule, antecedent):
        return self.support(rule) / self.support(antecedent)

    def lift(self, rule, antecedent, consequent):
        return self.support(rule) / (self.support(antecedent) * self.support(consequent))


def group(tuples_list, k):
    if k > 2:
        result_tuple = ()

        for t in tuples_list:
            result_tuple = result_tuple + t

        print("candidates", list(combinations(set(result_tuple), k)))
        return list(combinations(set(result_tuple), k))

    print("candidates", list(combinations(tuples_list, 2)))
    return list(combinations(tuples_list, 2))
