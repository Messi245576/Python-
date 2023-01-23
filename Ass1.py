#Assignment 1
#Create a two different examples for collective datatypes in python
# LIST INDEX:LEN:UPDATE:ADD:APPEND:INSERT:ADD TWO LIST:REMOVE:EXTEND ADD TWO LIST:DELECT
mylist=[10,"Messi",5.5,7,"Ronaldo",6]
#Print the Index of the List
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
print(mylist[5])
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])
print(mylist[-4])
print(mylist[-5])
print(mylist[-6])
print("Len of the mylist")
print(len(mylist))
print("Update values in the mylist")
mylist[2]="messi" 
print(mylist)
print("Add or append the values in the list")
mylist.append(59)
mylist.append("Tanishk")
mylist.append(6)
print(mylist)
print("Insert the element in the list")
mylist.insert(2,"Messi") #2 is the index of the mylist
print("TO add the list")
mylist2=["New Mylist"]
addlist=mylist+mylist2
print("Add of toe list ",addlist)
print("To Remove the element")
addlist.remove("New Mylist")
print("Remove the New List from List ",addlist)
print("Extend the mylist",mylist)
mylist.extend(mylist2)
print("The value of List",mylist)
dellist=[10,20,30,40,50]
print("Deleting the values",dellist)
del dellist[1]
print("Deleting the values",dellist)


