n = input("enter cutoff number")
n = int(n)

last = 1
current = 1
temp = 0
print(current)
for i in range(0,n):
    print(current)
    temp = current
    current += last
    last = temp
