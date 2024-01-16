# 0x09. Python - Everything is object
## Who am I?
What function would you use to get the type of an object?

Write the name of the function in the file, without ().
##  Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().
## Right count
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100
## Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a
## Right count =+
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

## Is equal
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

## Is the same
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

 ## Is really equal
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

## Is really the same
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

## And with a list, is it equal
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

 ## And with a list, is it the same
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

 ## And with a list, is it really equal
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

## And with a list, is it really the same
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

## List append
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

 ## List add
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

## Integer incrementation
What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

