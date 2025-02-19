print(list(range(10)))
print(list(range(1,10)))
print(list(range(0,10,2)))

i = 10
while i > 0:
    print(i)
    i = i-1
print('done')

for i in range(10):
    if i ==5:
        break
    print(i)
    print("Break Statement")

for i in range(10):
    if i ==3:
        continue
    print(i)
    print("Continue Statement")

