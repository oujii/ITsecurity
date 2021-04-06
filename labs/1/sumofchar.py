import fileinput

sum = 0
x = int(input())

for y in range(x):
    char = input()
    sum += ord(char)

print(sum)
