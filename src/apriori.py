from itertools import combinations


class Apriori:
    def __init__(self, items, transactions, smin, cmin):
        self.items = items
        self.transactions = transactions
        self.smin = smin # valor mínimo de suporte admitido para uma regra
        self.cmin = cmin # valor mínimo de confiança admitido para uma regra

    def run(self):
        self.cif()

    # conjunto de itens frequentes
    def cif(self):
        k = 2

        cif = [[0 for x in range(2)] for y in range(len(self.items))]

        for key in self.items:
            cif[key - 1][0] = key
            cif[key - 1][1] = self.suporte([key])

        lista = list(combinations(self.items.keys(), 2))
        print(lista)

        # for e in lista:
        #     self.suporte(e)

        print(cif)

    def suporte(self, rule):
        count = 0

        for key, value in self.transactions.items():
            if set(rule).issubset(set(value)):
                count += 1

        return count
