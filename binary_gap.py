# Binary gap - Codility 

def solution(N):
    # write your code in Python 3.8.10
    if N == 0:
        return 0

    binary = list(bin(N)[2:]) # create list of binary representation
    old_gap = 0 # store current gap
    new_gap = 0 # store new gap if it is larger than old_gap

    for i, j in enumerate(binary):
        if j == "1":
            if "1" in binary[i+1:]:
                old_gap = binary[i+1:].index("1")
                if old_gap > new_gap:
                    new_gap = old_gap
            
    return max(0, new_gap)