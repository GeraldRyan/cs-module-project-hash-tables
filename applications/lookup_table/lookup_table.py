# Your code here
import random, math
from datetime import datetime
start=datetime.now()




cache = {}

def slowfun_is_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    h = hash((x,y))

    if h not in cache:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[h] = v

    return cache[h]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14) 
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

print(f'time is ${datetime.now()-start}')

