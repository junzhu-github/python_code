# hello

# i'm home coding

### note

time_gap_percent = time_gap.value_counts(normalize = True)

	0	1
0	478	0.272987
1	114	0.065106
2	81	0.046259
3	77	0.043975
5	66	0.037693

  
 
 # assert function
 def my_func(x):
 	assert x > 0, "Error!"
	print(x)

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

double = lambda x: x * 2
print(double(7)) == print((lambda x: x * 2)(7))


#sets
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

#takewhile
from itertools import takewhile
nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x%2==0, nums)
print(list(a))
print('vs')
print(list(filter(lambda x: x%2==0, nums)))

#count
from itertools import count

for i in count(3):
  print(i)
  if i >=11:
    break

#product,permutations
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters))) 