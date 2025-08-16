#Question 1
#an empty list caled my_list 
my_list = []

#Question2
#append the follwing elements to my_list:10, 20, 30,40.
for value in [10, 20, 30, 40]:
  my_list.append(value)
print(my_list)

#Question 3
#Insert the value 15 at the second position
my_list.insert(2, 15)
print(my_list)

#Question 4
#Extend my_list with another list: [50, 60,70]
Extended_values = [50, 60, 70]
my_list.extend(Extended_values)
print(my_list)

#Question 5
#Remove the last element from my_list
my_list.remove(70)
print(my_list)

#Question 6
#Sort my_list in ascending order
my_list.sort()
print(my_list)

#Question 7
#Find and print the index of the value 30 in my_list
index = my_list.index(30)
print(index)