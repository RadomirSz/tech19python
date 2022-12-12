print('helo')
# suma = 0
# x = int(input())
# a = x
# while a>0:
#   suma = suma + a%10
#   x = x // 10
# print(suma)

# n = int(input())
# suma = 0
# while n>0:
#   suma = suma = n%10
#   n = n //10
# print(suma)

#zad3 6 28 496
# n = int(input())
# suma = 0 
# for i in range(1,n):
#   if n % i == 0:
#     suma = suma + i
# if suma == n:
#   print('jest')
# else:
#   print('nie')

# l = int(input())
# a, b = l, l
# x = a*b
# while b>0:
#   r = a%b
#   a = b
#   b = r
# if a != l/2 or a!=l/3:
#   print('nie jest pierwsza')
# else:
#   print('jest pierwsza')

n = int(input())
for i in range(10,20):
  x= n
  y = i
  while y>0:
    x, y = y, x%y
  if x == 1:
    print(f"para: {n}, {i}")


#zad 6 
a, b = int(input()), int(input())
c, d = a, b
x = a*b
while b>0:
  r = a%b
  a = b
  b = r
#a nwd

print(f"{c/a}{'/'}{d/a}")