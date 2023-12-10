f = open("inputs/day1.txt")
e = f.read().split("\n")
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
reversed_numbers = [n[::-1] for n in numbers]
t = 0
for s in e:
    min_index = 10000
    start_number = None
    for i, n in enumerate(numbers):
        if n in s:
            index = s.index(n)
            if index < min_index:
                min_index = index
                start_number = (i % 9) + 1

    reversed_s = s[::-1]
    end_number = None
    min_index = 10000
    for i, n in enumerate(reversed_numbers):
        if n in reversed_s:
            index = reversed_s.index(n)
            if index < min_index:
                min_index = index
                end_number = (i % 9) + 1
    t += int(str(start_number) + str(end_number))
print(t)
