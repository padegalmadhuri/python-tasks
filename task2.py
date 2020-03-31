list1=['a','b','c']
list2=[1,2,3]
dict1={list1[i]:list2[i] for i in list1 for i in range(0,len(list2))}
print(dict1)
