first_list = [1, 2, 3]
second_list = [2]
new_list = []
max_len = 0
if len(first_list) >= len(second_list):
    max_len = len(first_list)
else:
    max_len = len(second_list)
for i in range(max_len):
    if i >= len(first_list):
        new_list.append(second_list[i])
    elif i >= len(second_list):
        new_list.append(first_list[i])
    else:
        if first_list[i] > second_list[i]:
            new_list.append(second_list[i])
            new_list.append(first_list[i])
        else:
            new_list.append(first_list[i])
            new_list.append(second_list[i])
print(new_list)