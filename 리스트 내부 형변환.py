list1 = ['1', '100', '33']
list2 = []
for i in list1:
    list2.append(int(i))


list1 = ['1', '100', '33']
list2 = list(map(int, list1))


mylist = [[1], [2]]

answer = list(map(len, mylist))

print(answer)
