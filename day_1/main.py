# read file line by line
with open("input.txt") as f:
    lines = f.readlines()
    

def max_calories_elf(input):
    elves = []
    sum = 0

    # loop through lines
    for line in lines:
        # if line is empty, add sum to elves and reset sum
        if line.strip() == "":
            elves.append(sum)
            sum = 0

        # if line is not empty, add line to sum of a single elf
        else:
            sum += int(line.strip())
    return elves, max(elves)

elves, max_calories_elf = max_calories_elf(lines)
print(max_calories_elf)

    
def top_three_elves(elves):
    elves = sorted(elves, reverse=True)
    return elves[:3]

top_three_elves = top_three_elves(elves)
print(sum(top_three_elves))