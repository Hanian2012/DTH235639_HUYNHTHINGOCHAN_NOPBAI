list1 = [x for x in range(100) if x % 3 == 0]
list2 = [x**2 for x in range(20)]
list3 = [ "1" + "0"*i for i in range(10) ]
list4 = [ "0"*i + "1" + "0"*(9-i) for i in range(10) ]
print(list1)
print(list2)
print(list3)
print(list4)
