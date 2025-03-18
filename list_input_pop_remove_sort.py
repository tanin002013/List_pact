# num=[12,11,25,12,14,20,12,12,12]
# while 12 in num:
#     num.remove(12)
#     print(num)
# print(num)


# num=[12,11,25,12,14,20,12,12,12]
# x=[]
# for i in num:
#     print(i)
#     if i!=12:
#         x.append(i)
#         print(x)    
# print(x) 

# num=[10,20,30,40,50,20]
# print(sum(num))
# print(max(num))
# print(min(num))
# print(num.count(20))
# print(len(num))
# num.sort()
# print(num)
# print(sorted(num))
# num.sort(reverse=True)
# print(num)
# num.reverse()
# print(num)
# reverse_list=num[::-1]
# print(reverse_list)

# num=[1,2,3,4,2,3,5,6]
# unique_num=list(set(num))
# print(unique_num)
# print(num)

# list1=[1,2,3,4]
# list2=[3,4,5,6]
# mar_list=list1+list2
# print(mar_list)
# make_set=set(mar_list)
# print(make_set)
# make_list=list(make_set)
# print(make_list)
# marge_list=list(set(list1+list2))
# print(marge_list)





x=[]
while True:
    country_name=input("Enter the country name:").title()
    if country_name=="exit".title():
        break

    elif country_name=="pop".title():
        x.pop()
        print(x)

    elif country_name=="remove".title():
        remove=input(("Enter a country name want remove:")).title()
        x.remove(remove)
        print(x)

    elif country_name=="sort".title():
        x.sort()
        print(x)

    elif country_name=="remove_dup".title():
        unique=list(set(x))
        print(unique)
    
    elif country_name=="clear".title():
        x.clear()
        print(x)

    elif country_name=="copy".title():
        copy=x.copy()
        print(copy)

    elif country_name=="revsort".title():
        rev= x[::-1]
        print(rev)

    elif country_name=="for".title():
        for i in range(len(x)):
            print(i, x[i])   

    else:
        x.append(country_name)
        print(x)


