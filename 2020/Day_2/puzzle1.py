with open("day2_input.txt", "r") as f:
    passwordLines = map(str, f.readlines())

amountValidated = 0

for line in passwordLines:
    [policy, password] = line.split(':')

    [range, char] = policy.split(" ")
    [min, max] = range.split('-')

    count = 0

    for letter in password:
        if (letter == char): 
            count += 1
    
    if (count >= int(min) and count <= int(max)):
        amountValidated += 1

print(amountValidated)