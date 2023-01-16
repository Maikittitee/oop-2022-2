#4
import math

result = 0;

input = int(input())
num = input
list =[]


for i in range (4):
    result += num
    list.append(num)
    num = num * 10 + input

print(result)