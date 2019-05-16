from random import randint

res = 0
for i in range(5, 0, -1):
    res += randint(0, 10)*10**i
while('3' not in str(res)):
    res = 0
    for i in range(5, 0, -1):
        res += randint(0, 10) * 10 ** i
print(res)
