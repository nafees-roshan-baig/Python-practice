"""Use a while loop to print numbers from 10 to 1."""
i = 10
while i >= 1:
    print(i)
    i -= 1
"""Use a while loop to count how many numbers between 1 and 50 are divisible by 5."""
i = 1
count = 0
while i <= 50:
    if i % 5 == 0:
        count = count + 1
    i = i + 1
print(count)
"""Use a while loop to print the numbers from 1 to 20, but skip the number 10 using continue."""
i = 1
while i <= 20:
    if i == 10:
        i += 1
        continue
    print(i)
    i += 1
"""Use a while loop to print numbers from 1 to 20 and stop the loop when the number reaches 15 using break."""
i = 1
while i <= 20:
    if i == 15:
        break
    print(i)
    i += 1
"""Write a nested for loop where the inner loop stops using break when the value of j becomes 3."""
for i in range(4):
    for j in range(4):
        if j == 3:
            break
        print(i,j)