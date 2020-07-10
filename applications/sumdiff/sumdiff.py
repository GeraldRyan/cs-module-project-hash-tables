"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""


q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6

# Your code here
computed_values = {}

def sum_diff(tup):
    for t in tup:
        if t not in computed_values:
            computed_values[t] = f(t)
    return computed_values

computed_values = sum_diff(q)
print(computed_values)

for c in computed_values:
    print(c, computed_values[c])

