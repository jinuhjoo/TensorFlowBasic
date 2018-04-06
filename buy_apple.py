from layer_naive import *

apple=100
apple_num=2
tax=1.1

mul_apple_layer=MultiLayer()
mul_tax_layer=MultiLayer()

#forward
apple_price=mul_apple_layer.forward(apple, apple_num)
price=mul_tax_layer.forward(apple_price, tax)

#backward
dprice=1
dapple_price, dtax=mul_tax_layer.backward(dprice)
dapple, dapple_num=mul_apple_layer.backward(dapple_price)

print("price:", int(price))
print("dapple:", dapple)
print("dapple_num:", int(dapple_num))
print("dtax:", dtax)






