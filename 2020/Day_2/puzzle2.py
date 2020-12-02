with open("day2_input.txt", "r") as f:
    passwordLines = map(str, f.readlines())

amountValidated = 0

for line in passwordLines:
    [policy, password] = line.split(":")

    [positions, char] = policy.split(" ")
    [pos1, pos2] = list(map(int, positions.split("-")))

    pArr = list(password)
    # apparently this gives the right answer without providing support for index zero
    # I'm going to leave it like this, since this apparently provided the correct answer: 352.
    # Adding index zero support sets the answer to 397, interesting...
    if (pArr[pos1] == char and pArr[pos2] != char or pArr[pos1] != char and pArr[pos2] == char): 
        amountValidated += 1

print(amountValidated)