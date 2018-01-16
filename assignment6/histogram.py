import matplotlib.pyplot as plt
import numpy as np
import csv

#define arrays
arr_groceries = []
arr_groceries_number = []
#read csv file
writer = csv.writer(open('groceries.csv', "wb"), delimiter=',')
writer2 = csv.writer(open('items.csv', "wb"), delimiter=',')

with open("groceries.txt", "rb") as infile:
    reader = csv.reader(infile)
    conversion = set('\\')
    for row in reader:
        newrow = [''.join('' if c in conversion else c for c in entry) for entry in row]
        writer.writerow(newrow)
        arr_groceries.append(newrow)

# #convert arr groceries to flat list
# flat_groceries = [item for sublist in arr_groceries for item in sublist]
#
# #get unique items
# unique_groceries = list(set(flat_groceries))
#
# #change all groceries to number
# for i in range(0,len(flat_groceries)):
#     idx_item = unique_groceries.index(flat_groceries[i])
#     arr_groceries_number.append(idx_item)
#
# # for i in range(0,len(unique_groceries)):
# #     item = (i,unique_groceries[i])
# #     print(item)
# #     writer2.writerow(item)
#
# #plot the histograms
# plt.hist(arr_groceries_number, bins=30, range=(0, 169))
# plt.title("Histogram of groceries")
# plt.xlabel('Items')
# plt.ylabel('Frequency')
# plt.show()

print(arr_groceries)
