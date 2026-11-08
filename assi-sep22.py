# 1. Print numbers from 1 to 10

for i in range(1, 11):
    print(i)
# 2. Print numbers from 2 to 20, stop at 15

for i in range(2, 21):
    if i == 15:
        break
    print(i)
# 3. Print numbers from 10 to 20, skip 15

for i in range(10, 21):
    if i == 15:
        continue
    print(i)
# 4. Print numbers from 1 to 5 and use else

for i in range(1, 6):
    print(i)
else:
    print("Loop completed")