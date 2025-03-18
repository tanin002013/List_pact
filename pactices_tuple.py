# my_tuple=(1,2,3,4,5)
# # print("Tuple",my_tuple)
# print("1st element:",my_tuple[0])
# print("2nd element:",my_tuple[1])

# my_list=[10,20,30,40]
# # if 20 in my_tuple:
# #     print("20 is in the tuple")
# # else:
# #     print("20 is not in the tuple")
# # print("Length of tuple:", len(my_tuple))
# my_tuple=tuple(my_list)
# print(my_tuple)

# my_tuple=("a","b","c","d")
# print(my_tuple.index("c"))

# my_tuple=(1,2,3,4,2,5,2)
# count=my_tuple.count(2)
# print(count)
# print(my_tuple[3])

# my_tuple=(10,20,30,40,50)
# slice_tuple=my_tuple[1:4]
# print(slice_tuple)

# my_tuple=("Tanin",31,1993)
# name,age,birth_year=my_tuple
# print(name)
# print(age)
# print(birth_year)

# single_tuple=(5,)
# print(single_tuple)
# print(type(single_tuple))

# empty_tuple=()
# if not empty_tuple:
#     print("The tuple is empty")
# print(type(empty_tuple))    

# my_string="hello i am tanin"
# my_tuple=tuple(my_string)
# print(my_tuple)

# my_tuple=(1,2,3)
# repeted_tuple=my_tuple*3
# print(repeted_tuple)

# my_tuple=(10,20,5,12,80)
# print(max(my_tuple))
# print(min(my_tuple))

# my_tuple=(1,2,3,4,5)
# reversed_tuple=my_tuple[::-1]
# print(reversed_tuple)
# print(my_tuple[::-1])

# tup=(5,2,8,1,9)
# lis=[5,2,8,1,9]
# print(tuple(sorted(tup)))
# print(list(sorted(lis)))

# words=("apple","banana","cherry")
# length=tuple(len(word) for word in words)
# print(len(words))
# print(length)

# squres=tuple(x**2 for x in range(1,11))
# print(squres)

# my_tuple=(1,2,3,4,2)
# print(set(my_tuple))
# print(type(set(my_tuple)))
# x=list(my_tuple)
# print(x)
# print(type(x))
# print(tuple(x))
# print(type(tuple(x)))
# if len(my_tuple)==len(set(my_tuple)):
#     print("Unique")
# else:
#     print("Not unique")    

# words=("hello","world","python")
# upercase_words=tuple(word.upper() for word in words)
# print(upercase_words)

# tuple1=(1,2,3,4)
# tuple2=(2,3,4,5)
# tuple3=(3,4,5,6)
# common_element=tuple(set(tuple1)&set(tuple2)&set(tuple3))
# print(common_element)

# my_dict={"name":"Tanin","age":31}
# con_tuple=tuple(my_dict.items())
# print(con_tuple)

# tuple1=(1,2,3)
# tuple2=(3,4,5)
# print(tuple(set(tuple1+tuple2)))

# tuple1=(1,2,3,4)
# tuple2=(3,4,5,6)
# difference=tuple(set(tuple1)-set(tuple2))
# print(difference)
# unique=tuple(set(tuple1)^set(tuple2))
# print(unique)

# num=(1,2,3,4,5,6)
# even=tuple(x for x in num if x%2==0)
# odd=tuple(x for x in num if x%2!=0)
# print(even)
# print(odd)

# num=(10,20,30,40)
# print(sum(num))

# num=(10,20,40,5,12,15)
# print(tuple(sorted(num)))
# li=list(num)
# print(li)
# li.sort()
# print(li)

