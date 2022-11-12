#zad1
# n = int(input())
# for i in range(n):
#   print("*-|", end=" ")
#zad2
# n = int(input())
# for i in range(1, n+1):
#   print("*"*i,end="")
#   if i%2:
#     print("||",end="")
#   else:
#     print("--",end="")
#zad3
# n = int(input())
# for i in range(1,n+1):
#   print("*", end=" ")
#   if i%2==1:
#     print("|"*i,end=" ")
#   else:
#     print("-"*i, end=" ")
#PRE - tabliczka mnożenia
# \t to tabulator wyrównuje
# for i in range(1,11):
#   for j in range(1,11):
#     print(i*j,end="\t")
#   print()
#zad4
# n = int(input())
# for i in range(1,n+1):
#   for j in range(1,n+1,-1):
#     print("*")
#pre

# *
# **
# ***
# ****
# n = int(input())
# for i in range(n): #ilość wierszy
#   for j in range(i+1): #ilość kolumn
#     print("*", end=" ")
#   print()

#*
#**
#***
#****
#
#****
#***
#**
#*
# n = int(input())
# for i in range(n):  #ilość wierszy
#   for j in range(i + 1):  #ilość kolumn
#     print("*", end=" ")
#   print()

# print()
# print()

# for i in range(n):  #ilość wierszy
#   for j in range(n - i):  #ilość kolumn
#     print("*", end=" ")
#   print()

#    *
#   **
#  ***
# ****
#
# ****
#  ***
#   **
#    *

# n = int(input())

# for i in range(n):
#     for j in range(i + 1):
#         print("*", end="")
#     print()

# print()
# print()

# for i in range(n):
#     for j in range(n - i):
#         print("*", end="")
#     print()

# print()
# print()

# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for k in range(n - i - 1, n):
#         print("*", end="")
#     print()

# print()
# print()

# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(i, n):
#         print("*", end="")
#     print()
# n=int(input())
# for i in range(n):
#   for j in range(n):
#     if i >=j:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print()
# #*****
# #****
# #***
# #**
# #*
# for i in range(n):
#   for j in range(n):
#     if j >=i:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print() 
#n = int(input())
# for i in range(n):
#   for j in range(n):
#     if i==n-j-1 or i>j:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()


# for i in range(n):
#   for j in range(n):
#     if i+j >= n - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()
  
# print()

# for i in range(n):
#   for j in range(n):
#     if i <= j:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

#zad5
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     if j == n//2:
#       print("*", end="")
#     elif(i== n//2):
#       print("-", end="")
#     else:
#       print(" ", end="")
#   print()

#zad6
n = int(input())
for i in range(n):
  for j in range(n):
    if i+j == n-1:
      print("?", end=" ")
    elif i-j == 0:
      print("*", end=" ")
    else:
      print("", end=" ")
  print()