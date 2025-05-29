import re
print(sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", open("day3_input.txt").read())))