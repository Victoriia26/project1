stroka = '8 101 5 15 1 42 55'
list_1 = stroka.split(' ')
lists = [int(x) for x in list_1]
print(stroka)

list_sqrt = [pow(x, 2) for x in lists]
print(list_sqrt)
list_ost = [x % 11 for x in lists]
print(list_ost)
list_chet = [x for x in lists if x % 2 == 0]
print(list_chet)
list_nechet = [x for x in lists if len(str(x)) % 2 != 0]
print(list_nechet)
list_len = [int(str(x) * 2) for x in lists if len(str(x)) == 2]
print(list_len)
list_index = [lists[x] for x in range(len(lists)) if x % 3 == 0]
print(list_index)
