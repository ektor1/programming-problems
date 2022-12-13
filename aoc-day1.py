
# advent of code day 1
# Input: Number of calories each elf is carrying
# each elf's inventory is separated by a line and each block is the calories of the items that an elf has brought 
# Find how many calories are carried by the elf carrying the most calories

def max_calories(my_file):
    # open file in read mode
    my_file = open(my_file, "r")

    # read the file
    
    data = my_file.read()

    # split the data for each vertical space
    calories = data.split("\n")
    
    # store each elfs inventory in current. If current is larger than max
    # set max equal to current   
    max = 0
    current = 0
    for i in calories:
        if len(i) != 0:
            current += int(i)

        elif len(i) == 0:
            if current > max:
                max = current
            current = 0

    return max


