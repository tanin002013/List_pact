num=[1,2,3,4,5,6]
n=1
while n<=len(num): 
    print(num) 
    num=num[1:]+num[:1]
    # x=rot[1:]+rot[:1]
    n=n+1
    # print(x)


