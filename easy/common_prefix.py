'''
Problem:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

# Solution

words = [""]
current_letter = words[0][0]
common = True
prefix = ""
shortest_word = min(words, key=len)
for j in range(len(shortest_word)):
    for i in range(len(words)):
        current_letter = words[0][j]
        if current_letter != words[i][j]:
            common = False
    if common:
        prefix += current_letter
    common = True
print(prefix)