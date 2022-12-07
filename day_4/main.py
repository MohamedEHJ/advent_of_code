# read file line by line
with open("input.txt") as f:
    lines = f.readlines()


def count_overlap(lines):

    cpt = 0
    for line in lines:
        line = line.strip().split(",")

        range_1 = line[0].split("-")
        range_2 = line[1].split("-")


        range_1 = [i for i in range(int(range_1[0]), int(range_1[1]) + 1)]
        range_2 = [i for i in range(int(range_2[0]), int(range_2[1]) + 1)]

        if set(range_1) <= set(range_2):
            cpt += 1
        elif set(range_2) <= set(range_1):
            cpt += 1

    return cpt


print(count_overlap(lines))