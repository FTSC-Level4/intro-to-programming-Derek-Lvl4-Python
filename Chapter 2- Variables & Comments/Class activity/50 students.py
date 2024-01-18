# List: an object that contains multiple data items 
# Element - An iem in a list
# list () function can convert certain types of objects to lists

# INDEXING
# Index - the address of your data member in your list
# Index of first element in the list is 0, second element is 1 and n'th element is -1

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

my_list = ['yo','hey','go','yep','sup',1,2,'geng',3,4]
print('insert')
my_list.insert(1, "20")

print(my_list)

print('\nreverse')
my_list.reverse()
print(my_list)

print('\nremove')
my_list.remove('sup')
print(my_list)

