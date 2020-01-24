test = ['a', 'b', 'c', 'a', 'd', 'e', 'a', 'f', 'g', 'a', 'h', 'i']
a_items = []
for i in range(len(test)):
    if test[i] == 'a':
       a_items.append(i)
print(a_items)