lines = [line.split() for line in open("day1_input.txt").read().splitlines()]
xs, ys = [int(line[0]) for line in lines], [int(line[1]) for line in lines]
print(sum(abs(x-y) for x, y in zip(sorted(xs), sorted(ys))))