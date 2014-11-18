dataset = [4,12,21,28,28,29,30,32,34,35,35,36,38,39,40,40,42,44,45,46,47,49,50,53,55,56,59,63,80,191]

q1_idx = len(dataset) / 4
q2_idx = 2*len(dataset) / 4
q3_idx = 3*len(dataset) / 4

q1 = dataset[q1_idx]
q2 = dataset[q2_idx]
q3 = dataset[q3_idx]

iqr = q3 - q1

lowest = q1 - (1.5 * iqr)
highest = q3 + (1.5 * iqr)

outlier = [x for x in dataset if x < lowest or x > highest]

print outlier
