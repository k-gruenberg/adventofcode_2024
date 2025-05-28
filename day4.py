lines = open("day4_input.txt").read().splitlines()
cols = ["".join(line[i] for line in lines) for i in range(len(lines[0]))]
diags = ["".join(c for i, line in enumerate(lines) for j, c in enumerate(line) if i + j == s) for s in range(2*len(lines)-1)] +\
        ["".join(c for i, line in enumerate(lines) for j, c in enumerate(line) if i - j == d) for d in range(-len(lines)+1, len(lines))]
h_words = [line[i:i+4] for line in lines for i in range(len(line)-3)]
v_words = [col[i:i+4] for col in cols for i in range(len(col)-3)]
d_words = [diag[i:i+4] for diag in diags for i in range(len(diag)-3)]
print(sum(len([word for word in group if word in ["XMAS", "SAMX"]]) for group in [h_words, v_words, d_words]))