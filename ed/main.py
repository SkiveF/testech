def fibonacci(n):
    fib_ = [0, 1]
    while len(fib_) < n:
        net_n = fib_[-1] + fib_[-2]
        fib_.append(net_n)
    return fib_
        
        
        