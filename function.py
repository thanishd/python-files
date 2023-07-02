def demo():
    print("my name is thani")
demo()

def demo1(name):
    print("my name is :",name)
demo1("thani")

def demo2(name,age):
    print("my name is :",name)
    print("my age is :",age)
demo2(name="sri",age="23")

def demo3(country="india"):
    print("i am from :",country)
demo3("island")
demo3("america")
demo3()
demo3("dubai")

def demo4(x,y):
    return(x+y)
print(demo4(3,9))

def demo5(x,y):
    return(x+y,x-y,x*y,x/y)
print(demo5(4,2))

def demo6(*a):
    print(a[2])
demo6("thani","sri","rajesh","jos")


    
