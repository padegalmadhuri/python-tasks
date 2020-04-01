employ_dict = [{"name":"ramesh","age":25, "dept":"engineering","designation"                 :"DB Engineer","salary":30000},
                 {"name":"leena","age":23, "dept":"engineering","designation":"Architect","salary":80000},
                 {"name":"sherlock","age":30, "dept":"sales","designation":"Sales Officer","salary":60000},
                 {"name":"lestrade","age":40, "dept":"sales","designation":"VP","salary":100000},
                 {"name":"bean","age":35, "dept":"support","designation":"VP","salary":200000},
                 {"name":"stapleton","age":20, "dept":"hr","designation":"Intern","salary":5000}]
for i in range(0,len(employ_dict)):
    dict1=employ_dict[i]
    for i in dict1.values():
        if i=='engineering':
            dict1['salary']+=int(dict1['salary']*15/100)
        if i=='VP':
            dict1['salary']+=int(dict1['salary']*25/100)
        if i=='sales':
            dict1['salary']+=int(dict1['salary']*10/100)
        if i=='support':
            dict1['salary']+=int(dict1['salary']*12.5/100)
for i in range(0,len(employ_dict)):
    print(employ_dict[i])
        
