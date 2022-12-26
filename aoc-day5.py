
# We need to find which crate will end up at the top of each stack
# So we could have a dictionary where the KEYS represent each stack and the VALUES represent each crate in the corresponding stacks

# Part 1 ###############################################

my_file = open ("input5.txt", "r")

data = my_file.read()

data_clean = data.split("\n")

stacks = data_clean[0:8] # separate stacks from moves

stacks_dict = dict() 

def vintage_crane(data_clean):
    # Creates keys equal to the number of stacks in the data 
    for i in range(1, len(data_clean[0][1:-1][::4])+1):
        stacks_dict[i] = []

    # keys represent each stuck and their values which items are in each stack
    for i in stacks:
        for i, j in enumerate(i[1:-1][::4]):
            if j != " ":
                stacks_dict[i+1] += [j]

    moves = data_clean[10:-1] # separate moves from the text file

    for i in moves:
        # Split each move for every space so we can get the numbers indicating the stacks
        i = i.split(" ")

        # Get the items from the top of the stack, reverse order, then add items at the beginning of the stack indicated
        stacks_dict[int(i[5])] = stacks_dict[int(i[3])][:int(i[1])][::-1] + stacks_dict[int(i[5])]  

        # Remove items from the first stack
        del stacks_dict[int(i[3])][:int(i[1])]

    answer = "" # empty string to store the answer

    # add the top element of each stack to the answer 
    for i in range(1, len(stacks_dict)+1):
        answer += stacks_dict[i][0]

    return answer

# print(vintage_crane(data_clean))
# JRVNHHCSJ

# Part 2 ###############################################

def eva_unit_05(data_clean):
    """Same as above - just removed "[::-1]" from line 72"""
    # Creates keys equal to the number of stacks in the data 
    for i in range(1, len(data_clean[0][1:-1][::4])+1):
        stacks_dict[i] = []

    # keys represent each stuck and their values which items are in each stack
    for i in stacks:
        for i, j in enumerate(i[1:-1][::4]):
            if j != " ":
                stacks_dict[i+1] += [j]

    moves = data_clean[10:-1] # separate moves from the text file

    for i in moves:
        # Split each move for every space so we can get the numbers indicating the stacks
        i = i.split(" ")

        # Get the items from the top of the stack, reverse order, then add items at the beginning of the stack indicated
        stacks_dict[int(i[5])] = stacks_dict[int(i[3])][:int(i[1])] + stacks_dict[int(i[5])]  

        # Remove items from the first stack
        del stacks_dict[int(i[3])][:int(i[1])]

    answer = "" # empty string to store the answer

    # add the top element of each stack to the answer 
    for i in range(1, len(stacks_dict)+1):
        answer += stacks_dict[i][0]

    return answer

print(eva_unit_05(data_clean))