memo = {0: 1, 1: 1}


def fib(n, memo):
    if n == 0 or n == 1:
        k = 1
        print("first")
    elif n in memo.keys():
        k = memo[n]
        print("taken from dict")
    else:
        k = fib(n - 1, memo) + fib(n - 2, memo)
        print("counted")
    memo[n] = k
    return k


for n in range(1000):
    print(fib(n, memo))
print(memo)
