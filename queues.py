#!/usr/bin/env python3

'''
a queue has a front and back
fifo - first in first out

enqueue - add an item to the end


dequeue - (double ended queue)
    - remove an item from the front
    - allows storage and ability to manipulate data as a queue in python

peek() see the first item in the queue

time complexity is O(n)
'''

from collections import deque

# using deque as a queue
print("using deque as a queue:")

printer_queue = deque()
printer_queue.append("james_artur_tickets.pdf")
printer_queue.append("how_to_pass_exams.docx")
printer_queue.append("how_to_get_away_with_murder.docx")

while len(printer_queue) > 0:
    document = printer_queue.popleft()
    print(f"printing {document}")


# challenge
'''
use a queue to generate the first n binary numbers

take not of decimal to binary
'''
print("\n\nchallenge:")

def decimal2binary(num):
    if num <=0 :
        print("not valid. must be more than 0")
        return None

    queue = deque()
    queue.append(1)

    for i in range(num):
        binary = queue.popleft()
        print(binary)
        queue.append(binary * 10)
        queue.append(binary * 10 + 1)
        

print("binary for 5: ")
print(decimal2binary(5))
print()
print("binary for -9: ")
print(decimal2binary(-9))
print()
print("binary for 10: ")
print(decimal2binary(10))
print()
print("binary for 0: ")
print(decimal2binary(0))
print()
print("binary for 7: ")
print(decimal2binary(7))
print()