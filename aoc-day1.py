
# advent of code day 1
# Input: Number of calories each elf is carrying
# each elf's inventory is separated by a line and each block is the calories of the items that an elf has brought 
# Find how many calories are carried by the elf carrying the most calories

# open file in read mode
my_file = open("input1.txt", "r")

# read the file
    
data = my_file.read()

# split the data for each vertical space
calories = data.split("\n")

def max_calories(calories):    
    # store each elfs inventory in current. If current is larger than max
    # set max equal to current   
    current = 0
    max = 0
    for i in calories:
        if len(i) != 0:
            current += int(i)

        else:
            if current > max:
                max = current
            current = 0

    return max

# print(max_calories(calories))

def top_3_calories(calories):
    current = 0
    top_1 = 0
    top_2 = 0
    top_3 = 0

    for i in calories:
        if len(i) != 0:
            current += int(i)

        else:
            if current > top_1:
                top_2 = top_1
                top_1 = current
            elif current > top_2 and current < top_1:
                top_3 = top_2
                top_2 = current
            elif current > top_3 and current < top_2:
                top_3 = current
            current = 0
    return top_1 + top_2 + top_3

print(top_3_calories(calories))
