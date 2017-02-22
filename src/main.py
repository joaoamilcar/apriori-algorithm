from src.customcsv import parse_to_str_dict, parse_to_int_dict
from src.apriori import Apriori


items = parse_to_str_dict('items.data')
transactions = parse_to_int_dict('transactions.data')

apriori = Apriori(items, transactions, 2/5, 1)
apriori.get_frequent_itemset()