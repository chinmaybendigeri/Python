my_num_list = [1,3,7,9,4]
print(my_num_list) # lists are mutable where as strings are immutable

new_list = [1,"Chinmay","bendigeri",150000.00,4]
print(new_list)

my_num_list = my_num_list + [10] # we can only concate list to list and not an element

print(my_num_list)

new_list = new_list + ["test"] # better approach of adding an element to a list is use append method
new_list.pop() # remove an element for the end of the list
new_list.append("new element inserted")
print(new_list)

my_num_list.sort()
print(my_num_list)

my_num_list.reverse()
print(my_num_list)

print(my_num_list[2]) # list supports indexing of the element
print(my_num_list[-3:-1]) # slicing is supported by lists in python
