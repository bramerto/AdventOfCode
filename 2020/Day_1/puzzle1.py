with open("day1_input.txt", "r") as f:
    numbers = list(map(int, f.readlines()))

for i in numbers:
    if (i > 1000 and i < 2000):
        for j in numbers:
            if (i + j == 2020):
                print(i * j)