#!/usr/bin/env python3

# data elements in an array are referenced with an index or key

# create a list of numbers
print("\n\ncreating a list:")
student_pet_list = [0, 1, 0, 4, 4, 7, 4, 2, 1, 1, 0, 4, 6, 3, 1, 2, 0]
print(student_pet_list)


# to retrieve the 4th item which is 4
print("\n\nretrieving data from a list:")
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


# mutate a list in python (modifying)
# when you add a new element at the end of an existing linked list, the pointer of that new element is a null value
print("\n\nmutate/modify a list:")
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


# multidimensional list
# also known as a nested list allowing us to store multiple lists within a single list
# eg: in a 2 dimensional array with length (4, 7), there are 4x7=28 elements
print("\n\nmultidimensional list:")

seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

# to access second student in the third row "lauren"
print("second student sitting in the third row is: ", seating_chart[2][1], "\n")

# to display all student in each row
for i, row in enumerate(seating_chart):
    print(f"row {i+1}. students {row}") # row +1 beacuse we wwant to start printing from 1 not from default 0

print("\n")
# printing out all students and their individual row and seat numbers
for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} is in row {i+1}, seat{j+1}") 


# tuples
# array-like structure that is cannot be modified.
# useful for strong a collection of values that do not change
print("\n\ntuples:")

point = (5,2)

x = point[0]
y = point[1]

def calculate_sqaure(side_length):
    area = side_length * side_length
    perimeter = 4 * side_length
    return (area, perimeter)

result = calculate_sqaure(5)
print("area: ", result[0])
print("perimeter", result[1])


# searching for array like structures
print("\n\nsearching for array like structures:")

# linear search
# it will take some time to check as it will check every thing
# time taken to search will increase linearly with the size of the input.
# time complexity for this is O(n)
my_list = [8, 5, 6, 9, 1]
ITEM = 9 

def search(item, listy):
    for element in listy:
        if element == item:
            return True
    return False

print("what we are searching for is in the list: ", search(ITEM, my_list))

# to return the index of the first occurance of the element in  the list
ITEM_INDEX = my_list.index(ITEM)
print("the index is: ", ITEM_INDEX) # will show 3 but note that it starts from 0


# sorting array like structures
print("\n\nsorting array like structures:")

my_list = [1, 7, 3, 10, 2]
print("my sorted list in ascending order is: ", sorted(my_list)) 

print("my sorted list in descending order is: ", sorted(my_list, reverse=True)) 

# this is a list of tuples
student_grades = [('jack', 60), ('michael', 75), ('lauren', 100), ('bratt', 31)]
print("this will print ascending alphabetically: ", sorted(student_grades))
print("this will print descending by score: ", sorted(student_grades, key=lambda x:x[1], reverse=True)) # this taking the second element which is the score
print("this will print descending by alphabetically: ", sorted(student_grades, key=lambda x:x[0], reverse=True)) # this taking the first element which is the name


# finding the second smallest
# this is called timsort due to the python's sorted()
# hybrid between merch sort and insertion sort
# time complexity is O(n log n)
print("\n\nfinding the second smallest:")

def find_second_smallest(my_list):
    new_list = sorted(my_list)
    print(new_list[1])
    return new_list[1]
    
print("second smallest is: ", find_second_smallest([5, 8, 3, 2, 6]))


