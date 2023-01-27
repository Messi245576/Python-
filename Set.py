# Set
# Sets are used to store multiple items in a single variable.
# Set -> unordered,unindexed collection of datatypes ,{},doesn't contain a duplicate value

myset = {"apple", "banana", "cherry"}
myset1 = {"apple","apple", "banana", "cherry"}
print(myset)
print("Will  not Print apple two Times.\n",myset1)
print("Sets cannot have two items with the same value.\n")
print("Get the number of items in a set:\n",len(myset))
print("Get the number of items in a set:\n",len(myset1))
set1 = {"apple","Messi", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3,"Messi"}
set3 = {True, False, False}
print("String, int and boolean data types:\n",set1)
print("String, int and boolean data types:\n",set2)
print("String, int and boolean data types:\n",set3)

print("What is the data type of a set?\n",type(myset))
print("What is the data type of a set?\n",type(myset1))
print("What is the data type of a set?\n",type(set1))
print("What is the data type of a set?\n",type(set2))
print("What is the data type of a set?\n",type(set3))

print("Add to set\n")
set4=set1.union(set2)
print("After adding\n",set4)
# It will also work
# set4=set1|set2
# print(set4)
# Intersection(common)
set5=myset1.intersection(set2)
print(" Intersection(common)\n",set5)
# common values
set6=set1&set2
print("Concatenation\n",set6)
# Difference
set7=set1.difference(set2)
print(set7)














