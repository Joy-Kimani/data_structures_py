#create an empty list
my_list = []

#append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#print(my_list)#output [10, 20, 30, 40]
#insert the value 15 at the second position
my_list.insert(1, 15)
#print(my_list)# output [10, 15, 20, 30, 40]

#extend the list with another list
my_list.extend([50, 60, 70])
#print(my_list) output [10, 15, 20, 30, 40, 50, 60, 70]

#remove the last element
my_list.pop()
#print(my_list) output [10, 15, 20, 30, 40, 50, 60]

#sort the list in ascending order
my_list.sort()
#print(my_list) output [10, 15, 20, 30, 40, 50, 60]

#find and print the index of the value 30
index_of_30 = my_list.index(30)
print(index_of_30)
#ouput (3)