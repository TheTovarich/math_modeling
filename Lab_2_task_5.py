a = int(input('Введите делимое '))
b = int(input('Введите делитель '))
c = a // b
d = a % b

if b == 0:
  print('На ноль делить нельзя(Ну ты и тупой конечно в делитель пихнул 0)')
else:
  print(f'{a} : {b} = {c}')
  print(f'Остаток {d}')


  
  

  

