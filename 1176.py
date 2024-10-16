qtd = int(input())
fib = [0, 1]
res = []
for _ in range(qtd):
    entrada = int(input())
    for _ in range(len(fib), entrada + 1):
        fib.append(fib[_ - 1] + fib[_ - 2])
    res.append(entrada)
for _ in res:
    print(f"Fib({_}) = {fib[_]}")