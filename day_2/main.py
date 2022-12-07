# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
loses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}

pts = {'A': 1, 'B': 2, 'C': 3}
pts_you = {'X': 1, 'Y': 2, 'Z': 3}

# read file line by line
with open("input.txt") as f:
    lines = f.readlines()

def score(rounds):
    score = 0

    for round in rounds:
        # if you draw, you get the point of your choice and 3 extra points
        if draw[round[0]] == round[2]:
            score += pts_you[round[2]] + 3
            continue

        # if you win, you get the point of your choice and 6 extra points
        if wins[round[0]] == round[2]:
            score += pts_you[round[2]] + 6
            continue

        # if you lose, you get only the point of your choice
        score += pts_you[round[2]]


    return score

print(score(lines))