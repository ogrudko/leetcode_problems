'''
Problem:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

# Solution

user_input = input("Bring your Roman number:")
transform_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
output = 0
result = []
if len(user_input) == 1:
    output = transform_dict[user_input]
else:
    for i in range(len(user_input)):
        output += transform_dict[user_input[i]]
        if i > 0:
            if user_input[i] == "M" and user_input[i - 1] == "C":
                output -= 200
            elif user_input[i] == "D" and user_input[i - 1] == "C":
                output -= 200
            elif user_input[i] == "C" and user_input[i - 1] == "X":
                output -= 20
            elif user_input[i] == "L" and user_input[i - 1] == "X":
                output -= 20
            elif user_input[i] == "X" and user_input[i - 1] == "I":
                output -= 2
            elif user_input[i] == "V" and user_input[i - 1] == "I":
                output -= 2

print(output)