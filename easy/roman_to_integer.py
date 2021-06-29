# transforms roman numbers to integers

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