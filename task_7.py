_list = [1, 11, 2, 22, 3, 33, 22, 11]
list_2 = []
for repit in _list:
    if _list.count(repit) > 1:
        list_2.append(repit)
print(list_2)
