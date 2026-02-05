# sum of even no's between 20 & 40 (both included)

sum = 0
for i in range(20,41):
    if i % 2 == 0:
        sum += i
print(sum)