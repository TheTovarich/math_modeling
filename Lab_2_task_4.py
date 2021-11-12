n = int(input('Введите кол-во членов'))
n1 = n-2

print(1)

for i in range(0, n1 + 1):
  if i == 0:
    print(1, ' ')
    b = 1
  if i == 1:
    print(2, ' ')
    c = 2
  if i != 0 and i != 1:
    a = b + c
    print(a, ' ')
    b = c
    c = a






