import time

num = int(input('digite o numero da sua tabuada: '))
for c in range(1, 11):
    print(10*'_',end=' ')
    time.sleep(0.5)
    print('{} x {} = {} '.format(num, c,num*c))

for p in range(0, 1):
    time.sleep(0.5 )
    print(10*'_', end=' ')
