# x=None
# print(x)
#
# hello = '''
# 안녕하세요 하하하하하
# 파이선
# '''
# print(hello)
#
#
# s = float(input())
#
# print (s + 1)


#x,y = map(float, input().split())

#print('result:', x+1, y+1)


# from math import sqrt
# #import math
# print(sqrt(2))



x=[0,2,4,6,8,1,3,5,7,9]
print(x[::-1])
print(x[-1:-1:-1])
print(x[::-3])
print(x[::3])
print(x[len(x)-1::-1])


# print(x[len(x)-1], x[len(x)-3])
# print(x[-1], x[-3])
# print(x[2:5])
#
# print(x[:])
# print(x[2:len(x)//2], x[len(x)//2:-2])

print()
print()


a = {1:'x'}
print(a)

a[2] = 'b'
print(a)

a['name'] = 'Lee'
print(a)

a[9] = [3,4,5]
print(a)

del a[2]
print(a)

a[1] = 'y'
print(a)

a.clear()
print(a)


a = {1: 'y', 'name': 'Lee', 9: [3, 4, 5]}
print('name' in a)



mark = [50,30,20]

for mark2 in mark:
    if mark2 > 40: continue
    print('%04d' % mark2)




a = [1,2,3,4]
res = [num*3 for num in a if num%2 == 0]
# res=[]
# for num in a:
#     res.append(num*3)
print(res)



res=[x*y for x in range(2,10) for y in range(1,10)]
print(res)






import numpy as np

a = np.array([1,2,3])
print(type(a))

b = np.arange(5, 10, 0.2)
print(b)




x = np.arange(15)
x2 = x.reshape(5,3)
print (x2, '\n', x2.shape)


print(x2+2) #broadcasting

print(x2[-1][-1])
print(x2[-1, -1])
print(x2[0, 0])
print(x2[::-1, ::-1])
print(x2[2:4, 1:3])


print(x2.sum())
print(x2.sum(axis=1)) #행단위 합계
print(x2.sum(axis=0)) #열단위 합계
