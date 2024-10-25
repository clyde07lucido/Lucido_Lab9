rows = int(input("Enter the numbers of rows: "))

num = 1

for a in range(1, rows + 1):
    for b in range(1, a + 1):
        print(num, end=" ")
        num += 1
    print()
