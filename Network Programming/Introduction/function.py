def in_range(start, end, increment=1):
    print([i for i in range(start, end, increment)])


in_range(1, 100, 2)


def firsthalf(mystr):
    return mystr[:int(len(mystr) / 2)]

def reverse(mystr):
    return mystr[::-1]

s1 = "Network Programming"
s2 = "Informatics"
s3 = "Faculty Of Computer Science"

print(firsthalf(s2))
print(reverse(s1))
