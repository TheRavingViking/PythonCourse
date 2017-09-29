#input from user:
'''
name = input('What is your name?: ')
print('hello', name)
'''

import statistics

exlist = [8, 1, 1, 7, 6, 3, 4]

x = statistics.mean(exlist)
print(x)

x = statistics.median(exlist)
print(x)

x = statistics.mode(exlist)
print(x)

x = statistics.stdev(exlist)
print(x)

x = statistics.variance(exlist)
print(x)