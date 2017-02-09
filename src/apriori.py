from itertools import combinations


class Apriori:
    def __init__(self, items, transactions, smin, cmin):
        self.items = items
        self.transactions = transactions
        self.smin = smin # valor mínimo de suporte admitido para uma regra
        self.cmin = cmin # valor mínimo de confiança admitido para uma regra

    def get_cif(self):
        k = 2
        cif_dict = {}
        candidates = list(self.items.keys())
        # candidates = list(combinations(self.items.keys(), 1))

        print("candidates",candidates)

        for candidate in candidates:
            # first attribution
            if (k - 1) not in cif_dict:
                cif_dict[k - 1] = []

            if self.suporte([candidate]) >= self.smin:
                newCif = cif_dict.get(k - 1)
                newCif.append(candidate)
                cif_dict = {k - 1: newCif}

        print("dict", cif_dict)

        while cif_dict.get(k - 1) != None:
            group_list = self.group(cif_dict.get(k - 1), k)
            # print("groups", k, group_list)

            for candidate in group_list:
                list_combinations = combinations(candidate, k - 1)

                for tuple in list_combinations:
                    if tuple not in cif_dict.get(k - 1):
                        pass
                        # groups.remove(c) # poda

            for candidate in group_list:
                # first attribution
                if k not in cif_dict:
                    cif_dict[k] = []

                if self.suporte(candidate) >= self.smin:
                    newCif = cif_dict.get(k)
                    newCif.append(candidate)
                    cif_dict[k] = newCif

            k += 1

            print("dict", cif_dict)


        # cif = {}
        #
        # for candidates in L:
        #     # first assignment
        #     if (k - 1) not in cif:
        #         cif[k - 1] = []
        #
        #     if self.suporte([candidates]) >= self.smin:
        #         newCif = cif.get(k - 1)
        #         newCif.append(candidates)
        #         cif = {k - 1: newCif}
        #
        # print("cif", cif)
        #
        # lista = list(combinations(cif.get(1), 2))
        # print(lista)
        # print(len(lista))

    def group(self, L, k):
        print("quero:")
        print("L", L)
        print("k", k)

        LC = list(combinations(L, 2))
        print("candidates", LC)
        resultSet = ()

        if k > 2:
            for tuple in L:
                resultSet = resultSet + tuple

            print("candidates", list(combinations(set(resultSet), k)))
            return list(combinations(set(resultSet), k))


        # if k > 2:
        #     for g in SC:
        #         lista = []
        #         for tuple in g:
        #             lista = lista + list(tuple)
        #         print("lista", lista)
        #         # resultSet.append(lista)
        #         resultSet.append(set(lista))


        return LC

    def suporte(self, rule):
        count = 0

        for key, value in self.transactions.items():
            if set(rule).issubset(set(value)):
                count += 1

        return count / len(self.transactions)
