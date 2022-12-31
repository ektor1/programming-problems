# We need to identify 4 letters that will be different in a long sequence of letters
# When we find these 4 letters, we need to report how many letters appear from the beginning of the buffer
# until the end of the first 4-letter marker 

my_file = open("input6.txt", "r")
data = my_file.read()

# Part 1
def start_of_packet(data):
    """
    For every letter take that letter and the next three
    Then check if these four letters are unique - numpy unique function?
    print the range(len(data))+1 of the last letter of that 4-letter marker
    """
    for i in range(len(data)):
        for j in range(len(data[i:i+4])):
            if data[i:i+4][j] in data[i:i+4][j+1:]:
                break
            elif data[i:i+4][j] == data[i:i+4][-1]:
                return i+4

print(start_of_packet(data))

def start_of_message(data):
    """
    Same function as above - just changed number 4 to 14
    """
    for i in range(len(data)):
        for j in range(len(data[i:i+14])):
            if data[i:i+14][j] in data[i:i+14][j+1:]:
                break
            elif data[i:i+14][j] == data[i:i+14][-1]:
                return i+14

print(start_of_message(data))