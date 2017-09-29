#input from user:
'''
name = input('What is your name?: ')
print('hello', name)
'''

import statistics as s

exlist = [8, 1, 1, 7, 6, 3, 4]

x = s.mean(exlist)
print(x)

x = s.median(exlist)
print(x)

x = s.mode(exlist)
print(x)

x = s.stdev(exlist)
print(x)

x = s.variance(exlist)
print(x)