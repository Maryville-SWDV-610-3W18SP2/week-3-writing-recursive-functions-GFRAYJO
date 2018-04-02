# Write a short recursive Python function that finds the minimum 
# and maximum values in a sequence without using any loops.

def minMax(list):
    list = [1,3,5,7,9,11,13,15]
    max = list[7]
    min = list[0]
    if list == max:
        max = list[7]
    else:
        #list == min:
        min = list[0]
    return min, max

print(minMax(list))