
for y in range(7, -1, -1):
    print(y)

import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + ' . ')

