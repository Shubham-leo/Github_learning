input_list= [1,4,3,4,3,2,2,2,1,6,7,8]


hashset = set()
lst2 = []
count = 0
for n in input_list:
    if n not in lst2:
        count+=1
        lst2.append(n)

print(count)

from collections import Counter

items = Counter(input_list).keys()

print(len(items))

print ("created conflict")
