# First column is what the opponent is going to play where: A = rock, B = paper, C = scissors
# Second column is what I'm supposed to play where: X = rock, Y = paper, Z = scissors
# score for each round is the score for the shape you selected: rock = 1, paper = 2, scissors = 3 plus
# the score for the outcome of the round: lost = 0, 3 = draw, 6 = win

myfile = open("input2.txt", "r")

data = myfile.read()

rounds = data.split("\n")

item_values = {"X":1, "Y":2, "Z":3}
item_match = {"A":"X", "B":"Y", "C":"Z"}


# Part 1
def score(rounds):
    total_score = 0

    for i in range(len(rounds[:-1])):
        # Draw
        if item_match[rounds[i][0]] == rounds[i][2]:
            total_score += 3 + item_values[rounds[i][2]]
        # Win
        elif rounds[i][0] == "A" and rounds[i][2] == "Y":
            total_score += 6 + item_values[rounds[i][2]]
        # Win
        elif rounds[i][0] == "B" and rounds[i][2] == "Z":
            total_score += 6 + item_values[rounds[i][2]]
        # Win
        elif rounds[i][0] == "C" and rounds[i][2] == "X":
            total_score += 6 + item_values[rounds[i][2]]
        # Lose
        else:
            total_score += item_values[rounds[i][2]]
    return total_score

print(score(rounds))
    