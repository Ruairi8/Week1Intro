# Experimenting with python
for y in range(7, -1, -1):
    print(y)

count = 0
x = []
while count < 10:
    x.append(count)
    count += 1
print(x)


import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + ' . ')

