import matplotlib.pyplot as plt
import numpy as np
import csv
import urllib2
import numpy as np
import matplotlib.pyplot as plt

#define arrays
arr_groceries = []
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
flat_groceries = [item for sublist in arr_groceries for item in sublist]

#get unique items
unique_groceries = list(set(flat_groceries))
groceries_count=[]


for i in range(0,len(unique_groceries)):
    count = flat_groceries.count(unique_groceries[i])
    groceries_count.append(count)

#Plot histogram
plt.figure(1)
h = plt.bar(xrange(len(unique_groceries)), groceries_count, label=unique_groceries)
plt.subplots_adjust(bottom=0.2)

xticks_pos = [0.65*patch.get_width() + patch.get_xy()[0] for patch in h]
print(xticks_pos)

plt.xticks(np.arange(1,len(unique_groceries)+1), unique_groceries,  ha='right', rotation=90, fontsize=8)
plt.xlabel('Items')
plt.ylabel('Frequency')
plt.suptitle('Histogram of Groceries', fontsize=20)
plt.show()


