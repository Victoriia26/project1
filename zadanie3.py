num = int(input('Введите число: '))
a = [[abs(j - i) for i in range(num)] for j in range(num)]
print(a)
for b in a:
    print(' '.join([str(i) for i in b]))