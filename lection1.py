cash = [13142, 43345, 534345, 42254, 45354, 453445, 445345]
rashod = 0.2
#chet = 0
#for i in cash:
 #   chet += i
#print(chet)
#prybl = chet - (chet * rashod)
#print(prybl)

#def get_cash(cash_list, rashod):
#    chet = 0
#    for i in cash_list:
#        chet += i
#    prybl = chet - (chet * rashod)
#    return prybl

#print(get_cash(cash, rashod))


#args, kwargs

# def get(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
#
# get(1, 'A', True, a=10, b=False)

# def kpi(**kwargs):
#     count = len(kwargs)
#     shet = 0
#     for x in kwargs.values():
#         shet += x
#
#     return shet / count
#
# print(kpi(mat=100, him=90))

# dict1 = {"k": 1, "h": 4}
# for x, y in dict1.items():
#     print(x, y)

def get_num(*args):
    a = 0
    for i in args:
        if type(i) == int:
            a += i
    return a

print(get_num(1, 12, 5, 4, 'True',['e']))