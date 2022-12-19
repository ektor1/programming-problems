import numpy as np

my_file = open("input4.txt", "r")

data = my_file.read()

data_clean = data.split("\n")

new_pairs = [[x.split(",")] for x in data_clean]

# Part 1
def overlaps(new_pairs):
    """Create arrays for each set, convert them to sets, and check if its a subset of the other
    by using the issubset() function"""
    total_overlaps = 0

    for i in range(0, len(new_pairs[:-1])):
        set_1_0 = int(new_pairs[i][0][0].split("-")[0])
        set_1_1 = int(new_pairs[i][0][0].split("-")[1])
        set_2_0 = int(new_pairs[i][0][1].split("-")[0])
        set_2_1 = int(new_pairs[i][0][1].split("-")[1])

        if set(np.array(range(set_1_0, set_1_1+1))).issubset(set(np.array(range(set_2_0, set_2_1+1)))) == True:
            total_overlaps += 1
        
        elif set(np.array(range(set_2_0, set_2_1+1))).issubset(set(np.array(range(set_1_0, set_1_1+1)))) == True:
            total_overlaps += 1
    
    return total_overlaps

print(overlaps(new_pairs))

############################################### - NOTES - ###############################################

# For each pair, find if one range of numbers fully overlaps the other
# Make some kind of arrays for each range given. Then check is the shorter array exists inside the longer array
# Take the length of the shorter array and find IF its first element exists in the longer array 
# Then IF the length of what's left of the longer array is larger or equal to the length of the shorter array
# add +1 to total_overlaps. (Doesn't sound very efficient)

# Find how to split each pair for every "," and "-" to make the arrays

# THIS DID NOT WORK
# First sequence of if loops 
# Or check if the 1st number of the 1st range is smaller or equal than the 1st number of the 2nd range
# Then check if the 2nd number of the 1st range is larger or equal than the 2nd number of the 2nd range

# Second sequence of if loops
# OR if the 1st number of the 1st range is larger or equal than the 1st number of the 2nd range
# Then check if the 2nd number of the 1st range is smaller or equal than the 2nd number of the 2nd range 

# I don't understand why this didn't work 
# def overlaps(new_pairs):

#     total_overlaps = 0
    
#     for i in range(0, len(new_pairs)):
#         print(new_pairs[i])
#         if int(new_pairs[i][0][0].split("-")[0]) <= int(new_pairs[i][0][1].split("-")[0]):
#             if int(new_pairs[i][0][0].split("-")[1]) >= int(new_pairs[i][0][1].split("-")[1]):
#                 total_overlaps += 1
#                 print("overlap1")

#         if int(new_pairs[i][0][0].split("-")[0]) >= int(new_pairs[i][0][1].split("-")[0]):
#             if int(new_pairs[i][0][0].split("-")[1]) <= int(new_pairs[i][0][1].split("-")[1]):
#                 total_overlaps += 1
#                 print("overlap2")


#     return total_overlaps

# 403 is incorrect
# 488 is incorrect