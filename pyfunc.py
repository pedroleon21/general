x = list()

for i in range (0,100):
    x.append(i)
print(x)
i=1
while len(x) and i>=0:
    i=int(input())
    if i == -1 :
        while len(x):
            print(x.pop())
    else:
        if i in x:
            x.remove(i)
        else:
            print('null')

