import os,re

file_name = str(input('Enter File Name : '))
file = open(file_name,'r+')

pattern = str(input('What You Want to Find in File : '))

pattern_list =  []

pattern_list.append(pattern)

# print(file.read())
# print(pattern_list)

i = 1
match = 0
for line in file:
    for pattern in pattern_list:
        if(re.search(pattern,line)):
            print(pattern,'found at Line',+i)
            match = match + 1
    i = i + 1

print(match,'Match Found')
