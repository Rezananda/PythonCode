from sys import argv
from math import sqrt
from itertools import count, islice

list=[]
for i in range(int(argv[1]),int(argv[2]),1):
    if(i > 1 and all(i%x for x in islice(count(2), int(sqrt(i)-1)))):
        list.append(i)
print (list)
