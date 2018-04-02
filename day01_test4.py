def sum(a,b):
    print(a+b)
    return a+b

def sum2(a,b):
    if type(a) != type(b):
        print('not calculatable')
        return
    else:
        res=sum(a,b)

    return res

if __name__=="__main__":
    sum2('k', 5)
    sum2(1,2)
    sum2(1, 3.14)