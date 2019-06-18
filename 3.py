import math
n = int(input())
if n < 2:
    print("Никакое")
    quit()
elif n == 2:
    print("Простое")
    quit()
i = 2
limit = int(math.sqrt(n))
while i <= limit:
    if n % i == 0:
        print("Не простое")
        quit()
    i += 1
print("Простое")
