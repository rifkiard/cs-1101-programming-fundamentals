# Equivalent operator will return the True when the both side variables or values has the same values, no maters where the values is come from. In other hand, identical operator will do the same if the value is non-object. But if the values is objects, it will return True only when both variable has the same origin or blueprint.

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
list3 = list1
list4 = [1,2,3,4,6]

string1 = "Good Morning"
string2 = "Good Morning"
string3 = string1
string4 = "Good Afternoon"

print(list1 == list2)
# output: 
# True

print(list1 == list3)
# output: 
# True

print(list1 == list4)
# output: 
# False

print(string1 == string2)
# output: 
# True

print(string1 == string3)
# output: 
# True

print(string1 == string4)
# output: 
# False


#

print(list1 is list2)
# output: 
# False

print(list1 is list3)
# output: 
# True

print(list1 is list4)
# output: 
# False

print(string1 is string2)
# output: 
# True

print(string1 is string3)
# output: 
# True

print(string1 is string4)
# output: 
# False