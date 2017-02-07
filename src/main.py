from src.customcsv import parse_to_str_dict, parse_to_int_dict
from src.apriori import Apriori
from itertools import combinations


items = parse_to_str_dict('itens.data')
transactions = parse_to_int_dict('transacoes.data')

apriori = Apriori(items, transactions, 2/5, 1)
apriori.get_cif()

# print(items)
# print(transactions)


print("===")
a = (1, 3)
b = (1, 5)
c = (2, 3)
d = (2, 5)
e = (3, 5)


listaConcat = a + b + c + d + e

print("listaconcat", listaConcat)
print("listaconcatSET", set(listaConcat))
print("comb2", list(combinations(set(listaConcat), 3)))

#
# settest = set()
#
# settest.add(a)
# settest.add(b)
#
# print(settest)
# print(list(a), list(b))