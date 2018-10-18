# hello

# i'm home coding

### note
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

i[photo_test](https://raw.githubusercontent.com/junzhu-github/python_code/master/pic/1.png)

i[photo_test](pic/1.png)

