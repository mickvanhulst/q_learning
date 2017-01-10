walls = [(1, 1), (1, 2), (2, 1), (2, 2)]

#print(walls[1][1])

i = 2
j = 2

walls = [e for e in walls if i == e[0] and j == e[1]][0]

print(walls)