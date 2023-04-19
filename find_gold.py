def is_prime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True

def get_steps(position, direction):
    steps = 0
    while True:
        steps += 1
        position += direction
        if is_prime(position):
            return steps

n = int(input())

forward_steps = get_steps(n, 1)
backward_steps = get_steps(n, -1)

if forward_steps <= backward_steps:
    gold_block = n + forward_steps
else:
    gold_block = n - backward_steps

print(gold_block)