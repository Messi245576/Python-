# Tuple Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

mytuple = ("1:apple", "2:banana", "3:cherry")
mytuple2=("4:Messi","5:Ronaldo")
print(mytuple)
print(len(mytuple))
print(type(mytuple))
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[-1])
print(mytuple[-2])
print(mytuple[-3])
# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
print('"mytuple[0]="Messi"')
print("TypeError: 'tuple' object does not support item assignment")
print('mytuple.append(59)')
print("AttributeError: 'tuple' object has no attribute 'append'")
print('mytuple.insert(1,"Messi")')
print("AttributeError: 'tuple' object has no attribute 'insert'")
print("We can Add two Tuples")
addtuple=mytuple+mytuple2
print(addtuple)
print('mytuple.remove("4:Messi")')
print("AttributeError: 'tuple' object has no attribute 'remove'")
print("mytuple.extend(mytuple2)")
print("AttributeError: 'tuple' object has no attribute 'extend'")
print("del mytuple[0]")
print("TypeError: 'tuple' object doesn't support item deletion")

