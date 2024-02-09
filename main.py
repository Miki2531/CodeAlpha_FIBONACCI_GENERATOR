"""
Project Name: FIBONACCI GENERATOR

Authors: Mikiyas shemelis

Descriptions: Fibonaicci generators is a programe or function that generate the fibonaicci sequence.
"""

def fibonacci_generator(n):
    fib_num = [0, 1]
    for i in range(2, n):
        next_fib = fib_num[-1] + fib_num[-2]
        fib_num.append(next_fib)
    return fib_num

n = int(input("Number of fibonacci numbers you want to generate: "))
fib_seq =fibonacci_generator(n)
print(fib_seq)