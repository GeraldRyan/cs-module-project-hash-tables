"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import math
import itertools

q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6

# Variations with repitition, order important 
def get_num_combinations(tup, cap):
    return int(math.pow(len(tup),cap))

def get_combinations(tup, cap):
    return itertools.product(tup, repeat=cap)
    



# Your code here
computed_values = {}

def sum_diff(tup):
    for t in tup:
        if t not in computed_values:
            computed_values[t] = f(t)
    return computed_values

computed_values = sum_diff(q)
print(computed_values)

for index, c in enumerate(computed_values):
    print(index, c, computed_values[c])
    # for range(len(computed_values)):
    #     pass
        





print(f(1)+f(1) == f(12) - f(7))
print("Number of combos with repitition order important", get_num_combinations(q,4))
for el in get_combinations(q,4):
    print(el)