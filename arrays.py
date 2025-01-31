#!/usr/bin/env python3

''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

# create a list of numbers
student_pet_list = [0, 1, 0, 4, 4, 7, 4, 2, 1, 1, 0, 4, 6, 3, 1, 2, 0]
print(student_pet_list)


# to retrieve the 4th item which is 4
item_at_index_three = student_pet_list[3]
print("item at index 3: ", item_at_index_three)

# to retrieve the 3rd item from the back which is 1
item_three_from_back = student_pet_list[-3]
print("item at index 3 from the back: ",item_three_from_back)

# this will show many students are in the data structure
num_of_students = len(student_pet_list)
print("nummber of students: ",num_of_students)


sum = 0
for individual_pet_count in student_pet_list:
  sum += individual_pet_count

print("sum: ",sum)

# average = sum / number of items
average_pet_count = sum / num_of_students
print("average pet count: ",average_pet_count)
print("\n\n")

# mutate a list in python (modifying)
student_pet_list[2] = 7 # this means like the value at index 2 will change form 0 to 7
student_pet_list[3] = student_pet_list[3] + 1 # adding 1 to the value in that index
student_pet_list[-1] = student_pet_list[-1] + 2 # adding to the first value from the back

# adding more to the list
student_pet_list.append(4) # adding a new value 4 to the back of the list

print(student_pet_list)

# this will show many students are in the data structure
num_of_students = len(student_pet_list)
print("nummber of students: ",num_of_students)


sum = 0
for individual_pet_count in student_pet_list:
  sum += individual_pet_count

print("sum: ",sum)

# average = sum / number of items
average_pet_count = sum / num_of_students
print("average pet count: ",average_pet_count)