with open("input.txt") as f:
    lines = f.readlines()


lowercase = {chr(i): i - 96 for i in range(97, 123)}
uppercase = {chr(i): i - 38 for i in range(65, 91)}

both = {**lowercase, **uppercase}


def priority(lines):
    sum_priority = 0
    shared = set()

    for line in lines:
        line = line.strip()
        first = set(line[: len(line) // 2])
        second = set(line[len(line) // 2 :])

        # intersection of two sets
        shared = first.intersection(second)

        for letter in shared:
            sum_priority += both[letter]

    return sum_priority


print(priority(lines))

# part 2


def badges_priority(lines):

    s = 0
    # read file by chunks of 3 lines
    for i in range(len(lines)):
        if i % 3 == 0:
            line1 = lines[i].strip()
            line2 = lines[i + 1].strip()
            line3 = lines[i + 2].strip()

            # intersection of two sets
            shared = set(line1).intersection(set(line2), set(line3))

            s += sum(both[letter] for letter in shared)

    return s


print(badges_priority(lines))
