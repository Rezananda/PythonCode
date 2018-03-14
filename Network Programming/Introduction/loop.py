
print("Odd Number Betweeen 1 and 10")
result1 = []
i = 1
while i < 10:
    if i % 2 == 1:
        result1.append(i)
    i += 1
print(result1)
result2 = [i for i in list(range(1,10,2))]
print(result2)

list = ['Learn', 'Network', 'Programming' , 2018]
list2 = ['Compational' , 'Based' , 'Network']

print ("Value of 2nd list : ", list[2])
print (list.pop())
list.extend(list2)
list.reverse()

print (list)
