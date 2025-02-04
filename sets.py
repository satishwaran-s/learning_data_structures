#!/usr/bin/env python3

'''
sets is an abstract data type and is a non linear data structure

O(1) or constant time complexity

a set is a collection of uniqie elements and it is unordered

there are no duplicate elements

sets is to group things with common properties

in sets:
- order does not matter
- check for compatibility
    - number
    - character
    - string

in a set, the key is the value

cons of sets:
    - sets are unordered and lack indexing
'''
# creating a set list
print("creating a set list:")

primary_colours = set(["red", "blue","yellow"])

colour = "green"

if colour in primary_colours:
    print(colour, " is a primary colour")
else:
    print(colour, " is NOT a primary colour")


letters = set(["a", "b"])
print("\nold letters: ", letters)
letters.add('c')
print("new letters: ", letters)


# operations on sets
print("\n\noperations on sets:")

set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

# this will only print the common item once
combined_set = set_A.union(set_B)
print("combined set is: ", combined_set)

# this wil print items that are in both sets
intersection_set = set_A.intersection(set_B)
print("intersection set is: ", intersection_set)
      
# subtract contents from set_b from set_a
difference_set_AB = set_A.difference(set_B)
print("difference set AB is: ", difference_set_AB)

difference_set_BA = set_B.difference(set_A)
print("difference set BA is: ", difference_set_BA)

symmetric_difference_set = set_A.symmetric_difference(set_B)
print("symmetruc difference is: ", symmetric_difference_set)


# immutable sets
print("\n\nimmutable sets:")

primary_colours = frozenset(["red", "blue", "yellow"])

if "blue" in primary_colours:
    print("yes there is")

'''
will get error when running the line below:
AttributeError: 'frozenset' object has no attribute 'add'

this is beacuse frozensets cannot be changed
'''
#primary_colours.add("green")

# challenge
print("\n\ncreate a program that determines whether a piece of text has unique characters:")

def has_unique_characters(data):
    unique_data = set(data)
    # print(unique_data)
    unique_data_length = len(unique_data)
    # print(unique_data_length)

    data_length = len(data)
    # print(data_length)

    if data_length == unique_data_length:
        print(data)
        print("same same\n")
    else:
        print("different :(\n")

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
