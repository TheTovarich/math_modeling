a = int(input('Введите первую сторону '))
b = int(input('Введите вторую сторону '))
c = int(input('Введите третью сторону '))

if a + b < c:
  print('Треугольник не существует')
else:
  if a == b and a == b and c == b:
    print('Треугольник равносторонний')
  elif a == b or a == c or b == c:
    print('Треугольник равнобедренный')
  else:
    print('Треугольник разносторонний')