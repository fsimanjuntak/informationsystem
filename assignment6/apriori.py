import csv
from itertools import chain, combinations

min_support = 0.001
min_confidence = 0.8

#open the file and read the data
input_file = open('groceries.txt', 'r')

#global array to store each transaction, which is a list => list of lists
transactions_list = []

#read file
raw_data = csv.reader(input_file)
#get rid off backslash
char_to_erase = set('\\')
#create a transaction containing the element from a single line in the input file.  transaction is a list
for row in raw_data:
    new_transaction = [''.join('' if char in char_to_erase else char for char in entry) for entry in row]
    transactions_list.append(new_transaction)

#compute list of items from the transactions list
def itemset_from_transactions():
    itemset = set()
    for row in transactions_list:
        for item in row:
            if item:
                #frozen set is immutable and hashsable. Each element is converted to such set and added to the itemset list once
                itemset.add(frozenset([item]))
    return itemset

#join elements in the input itemset at phase k-1 to obtain the candidates for the k phase
def selfjoin(itemset, k):
    #create a set by joining each i and j (i!=j) whose union has length k
    # a set is an unordered collection of unique elements
    return set([i.union(j) for i in itemset for j in itemset if len(i.union(j)) == k])

def itemset_support(itemset, min_support):
    #compute support for each item in the input itemset and store in a list of tuples (item, item_support)
    support_list = [ (item, float(sum(1 for row in transactions_list if item.issubset(row)))/len(transactions_list)) for item in itemset ]

    #return tuples containing the item and their corresponding support, for the items that have min_support
    return dict([(item, support) for item, support in support_list if support >= min_support])

#compute all the frequent itemsets by applying apriori algorithm
def apriori_frequent_itemset(candidates_list, min_support):
    f_itemset = dict()

    k = 1
    while True:
        #Join Step: for the next phases, generate candidates by self joining the L_itemset from the previous phase (k-1)
        if k > 1:
            candidates_list = selfjoin(L_itemset, k)
        #Prune Step: get the itemset that contains the items that have minimum support
        L_itemset = itemset_support(candidates_list, min_support)
        if not L_itemset:
            break
        f_itemset.update(L_itemset)
        k += 1

    return f_itemset

def subsets(itemset):
    return chain(*[combinations(itemset, i + 1) for i, a in enumerate(itemset)])

def generate_association_rules(min_support, min_confidence):
    #get the list of items
    itemset = itemset_from_transactions()
    # Get the frequent itemset
    freq_itemset = apriori_frequent_itemset(itemset, min_support)

    # Association rules part
    rules = list()
    # for all frequent itemsets
    for item, support in freq_itemset.items():
        #there should be at least a pair of items
        if len(item) > 1:
            #check for non empty subsets
            for obj1 in subsets(item):
                obj2 = item.difference(obj1)
                if obj2:
                    obj1 = frozenset(obj1)
                    obj_join = obj1 | obj2
                    confidence = float(freq_itemset[obj_join]) / freq_itemset[obj1]
                    if confidence >= min_confidence:
                        rules.append((obj1, obj2, confidence))
    return rules, freq_itemset

association_rules, freq_itemset = generate_association_rules(min_support, min_confidence)
print association_rules.__sizeof__()
