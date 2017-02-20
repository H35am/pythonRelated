lijst = [[1,2],[3,4,5],[6,7,8,9]]
xix =  len(lijst) + len(lijst[-1])

x = 0
for i in range(3):
    for j in range(2):
        x += i * j
print (x)
