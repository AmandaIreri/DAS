# Creating a tuple
my_tuple = (10,20,50,"Hello","AkiraChix","Amanda",80,True)

#Using Indexing
print(my_tuple[0])
print(my_tuple[-1])

#Using slicing
print(my_tuple[2:5])

#accessung through iteration(looping)
for item in my_tuple:
    print(item)

#adding items
list1 = list(my_tuple)
list1.append("student")
print(list1)
my_tuple = tuple(list1)
print(my_tuple)

#removing items
list1.remove("AkiraChix")
my_tuple = tuple(list1)
print(my_tuple)