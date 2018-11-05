# bubble sort

# my
import numpy as np

x = 10
l = np.random.permutation(x)
print('before:',l)

# n = len(l) - 1

# while n:
#     n = len(l) - 1
#     for i in range(len(l)-1):
#         if l[i] >= l[i+1]:
#             l[i],l[i+1] = l[i+1],l[i]
#         else:
#             n -= 1

# print('after:',l)

# ----------------------------------------------

# book
def bubble_sort(l):
  for passnum in range(len(l)-1,0,-1):
    for j in range(passnum):
      if l[j]>l[j+1]:
        l[j], l[j+1] = l[j+1], l[j]

bubble_sort(l)

print('after:',l)