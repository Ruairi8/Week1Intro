import random
x = ['apple', 'pear', 'coconut', 'papaya']
# Need a random number between 0 and length -1
index = random.randint(0, len(x)-1)
y = x[index]
print("A random fruit: {}".format(y))