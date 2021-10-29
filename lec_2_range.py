'''
по умолчанию: start = 0, step = 1
Диапозон генерирования: [start, stop] от 0 до 9 (10 занчений)
'''

a = range(0, 10, 2)
print(a)#выведет a = range(0, 10, 2)
print(type(a)) #<class 'range'>
print(a[3])#6 т.к. досчитал до 3 элемента

a = 'Good'
for i in range(0, 10, 1):
  if i < len(a):
    print(a[i] + ' - Bad ')
  else:
    print(f'{i}' + ' - Good')
