# # #a = 5
# # #if a % 2  == 1:
# #
# # a = 0
# #
# # #if a % 2:
# # if a:
# #     print('홀수')
# # else:
# #     print('짝수')
#
#
# b=int('10')
# if b>0:
#     print('양수')
# elif b == 0:
#     print('0')
# else:
#     print('음수')
#
# #print(type(b))
#
#
# n=5
# print('hi' * n)
#
#
# for i in range(5):
#     print(i, end=' ')
# print()
#
# for i in range(0,5,2):
#     print(i)
# print()
#
# for i in range(10, -1, -1):
#     print(i)
# print()
#
#
#
# for i in range(4):
#     for j in range(1,i+2):
#         print(j, end=' ')
#     print()
#
#
# a=''
# for i in range(4):
#     a += str(i+1)+' '
#     print(a)
#




a=[1,3,5] #list
a[0] = a[2]
a.append(7)
print(a)


for i in range(len(a)-1, -1, -1):
    print(a[i])

print()

for i in reversed(a):
    print(i)


print()

a,b=5,7
a,b=b,a
print(a, b)

print()

#자료구조 : 리스트 [], 튜플 (), 딕셔너리 {}, 셋 {}

t1=(3,5)
print(t1)
print(t1[1], type(t1))




def order(a, b):
    if a>b:
        return b,a
    return a,b


#res = order(7,5)
#print(res, type(res))


min,max = order(7,5)
print(min, max)


_,max = order(7,5)
print(max)


a=[1,3,5,7,2,4,6,8]

for i in range(len(a)):
    print(i, a[i], end=', ')
print()


k=0
for i in a:
    print(k, i, end=', ')
    k+=1
print()


for i in enumerate(a):
    print(i, i[0], i[1], end=', ')
print()


for i,j in enumerate(a):
    print(i,j,end=', ')
print()



def mydef():
    pass

print(mydef())



myset=[1,2,3,1,2,3]

print(myset)

myset2=[]
for i in myset:
    if not i in myset2:
        myset2.append(i)
print(myset2)


print( list(set(myset)) )