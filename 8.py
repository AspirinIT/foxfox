n = int(input())
p = int(input())
A = []
for i in range(n, p):
    if i%2 != 0:
        A.append(i**3)
print(A)
