# A program that puts 10 random numbers into a list, the program should output all the values in the queue, 
# then take the nums from the queue 1 at a time, print it and the current nums in the queue.
# queue is [17, 72, 31, 89, 42, 19, 83, 49, 62]
# Current num is 17 and the queue is now [71, 31, 89, 42, 19, 83, 49, 62] 
#......................................................
# Current numb is 62 and the queue is []
# The queue is now empty.

import random
x = []
while len(x) < 10:
    x.append(random.randint(1, 100))
print("queue is ", x)
y = x.pop(0)
while len(x) != 0:
    y = x.pop(0)
    print("current number is ", y, " and the queue now is ", x)

print("The queue is now empty")

# A program that reads in a students name, modules & grades until the user enters a blank.