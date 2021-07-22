'''
Prolbem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''


# Solution

user_string = input("Input your parentheses:\n")
left_brackets = ["(", "[", "{"]
right_brackets = [")", "]", "}"]
stack = []
correct_parentheses = True
for char in user_string:
    if char in left_brackets:
        stack.append(char)
    elif char in right_brackets:
        if len(stack) <= 0:
            correct_parentheses = False
            break
        if left_brackets.index(stack.pop()) != right_brackets.index(char):
            correct_parentheses = False
            break
if len(stack) != 0:
    correct_parentheses =  False

print(correct_parentheses)

