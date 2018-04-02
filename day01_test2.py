mydict = dict(addr = 'seoul', age = 30)

print(mydict)
print(mydict['addr'])
print(mydict['age'])


mydict['name'] = 'Park'
mydict['addr'] = 'Suwon'
print(mydict)


for mykey in mydict.keys():
    print (mykey, mydict[mykey])

print()

for myval in mydict.values():
    print (myval)
print()


for myitem in mydict.items():
    print(myitem)

for key, val in mydict.items():
    print(key, val)

print()
for x in mydict:
    print(x, mydict[x])


print()
#for x in reversed(list(mydict.keys())):
for x in list(mydict.keys()):
    print(x, mydict[x])


print()
print()


import matplotlib.pyplot as plt


def lossf(x,y,w):
    loss=0
    for i in range(len(x)):
        hf = w*x[i]   #bias 생략
        loss += (hf-y[i])**2

    return loss/len(x)


x=[1,2,3]
y=[1,2,3]
w=10 #5


print('loss: ', lossf(x,y,w))

x2,y2 = [],[]
for i in range(-50, 50):
    w = i/10
    loss = lossf(x,y,w)
    print(w, loss)
    x2.append(w)
    y2.append(loss)

plt.plot(x2, y2)
plt.plot(x2, y2, 'ro')
plt.show()

