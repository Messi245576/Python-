# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)
print(mydict["brand"])
print(mydict["model"])
print(mydict["year"])

print("Update the Val in Dictionary ")
mydict["brand"]=("Ford","Foord")
print("The values after update",mydict)

print("Add KEY to the Dictionary")
mydict["Prize"]=[1233332]
print("After Adding the KEYS to the Dictionary\n",mydict)

print("PoP the Element from the Dictionary")
mydict.pop("brand")
print("After Delecting the Element from the Dictionary\n",mydict)

print("Updating the Keys\n")

# new=mydict["Course"]
# del mydict["Course"]
# mydict["Learning"]=new
# print(mydict)








