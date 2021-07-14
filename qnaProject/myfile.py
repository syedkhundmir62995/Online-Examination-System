# def myfun(input1,input2,input3):
#     for i in range(0,len(input2)):
#         data = input2[i]
#         sum = 0
#         for j in range(i+1,len(input2)-1):
#             data += input2[j]
#             if data == input3:
#                 print("yes")
            # print(input2[i],input2[j])





# myfun(5,[4,7,8,2,3],12)
# for i in range(1,20):
#     print(i)

# l = [4,7,8,2,3]
# for i in range(0,len(l)):
#     print(i)


# for i in range(0,3):
#     for j in range(i+1,4):
#         print(i,j)

# import itertools
# # l = [9,7,3,12,7]
# # n = 2
#
# def myfunc(input1,input2,input3):
#     n = 2
#     while(n <= input1):
#         mylist = list(itertools.combinations(input2,n))
#         n = n + 1
#         for i in mylist:
#             if sum(i) == input3:
#                 print(i)
#                 print("yes")
#             else:
#                 pass
#
# myfunc(5,[4,7,8,2,3],12)






# s = "my name is granar"
# input2 = "y"
# input1 = "my name is granar"
# try:
#     a = input1.index(input2)
#     b = input1.rindex(input2)
#     count = 0
#     for i in input1[a:b]:
#         if 65 <= ord(i) <= 122 and i != input2:
#             print(i)
#             count = count + 1
#
#     print(count)
# except:
#     print(-1)






s = "Hello world"
l = s.split(" ")

l2 = []

# print(s[-1::-1].capitalize())

for i in l:
    res = i[-1::-1].capitalize()
    l2.append(res)

data = " ".join(l2)
print(data)





















