from src.customcsv import parse_to_str_dict, parse_to_int_dict
from src.apriori import Apriori


items = parse_to_str_dict('itens.data')
transactions = parse_to_int_dict('transacoes.data')

apriori = Apriori(items, transactions, 2/5, 1)
apriori.run()

# print(items)
# print(transactions)