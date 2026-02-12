k, n, w = map(int, input().split())
for i in range(1, w + 1):
    n -= k * i  
print(abs(n) if n < 0 else 0)
