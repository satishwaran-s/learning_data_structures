#!/usr/bin/env python3

'''
a stack is an ordered series of objects that pushes objects
onto the stack and pops objects off of the stack

- add and remove from the top of the stack
- last in first out (LIFO)
    - push is to add to the stack
    - pop is to remove from the stack

similar to a list but slightly different

if need to index data, stacks are not ideal
'''

# using a list as a stack
print("using a list as a stack:")

stack_of_cards = []

stack_of_cards.append("jack of hearts")
stack_of_cards.append("2 of diamonds")
stack_of_cards.append("10 of spades")

# front will be the bottom and back will be the top
# meaning jack of hearts is bottom and 10 of spades is top
print("the current stack of cards:")
print(stack_of_cards)

top_card = stack_of_cards.pop()
print("\nthe updated stack of cards after popping the top card:")
print(stack_of_cards)
print("now the new top card is: ", stack_of_cards[-1])

if not stack_of_cards:
    print("\ncard stack is empty")
else:
    print("\nthe number of cards in the stack now: ", len(stack_of_cards))


from collections import deque

# using a deque as a stack
# deque is a double ended queue
print("\n\nusing a deque as a stack:")

history_stack = deque()
history_stack.append("www.google.com")
history_stack.append("www.youtube.com")
history_stack.append("www.miniclip.com")

print("the current history stack is: ", history_stack)

print("\nlast element in the stack: ", history_stack[-1])

print("\npopping the last element in the stack: ", history_stack.pop())


# challenge
'''
develop a function that determines if a piece of text
has matching parenthses

eg: 
matching:
- ()
- (hi there)
- (hell)o
- ((help)) me

not matching:
- (hi( there
- ()ok)
- ((increment)
- )michaelo()
'''
print("\n\nchallenge:")

def check_matching_parentheses(s):
    my_phrase = deque()
    for char in s:
        if char == "(":
            my_phrase.append(char)
        elif char == ")":
            if not my_phrase:
                return False
            my_phrase.pop()
    return len(my_phrase) == 0

print(check_matching_parentheses("()"))
print(check_matching_parentheses("(hi there)"))
print(check_matching_parentheses("(hell)o"))
print(check_matching_parentheses("((linkedin)) learning"))

print(check_matching_parentheses("(hi(there"))
print(check_matching_parentheses("()ok)"))
print(check_matching_parentheses("((increment)"))
print(check_matching_parentheses(")linkedin()"))
