def counter():
    a=[1,2,3,4,5]
    while 1:
        for i in range(5):
            yield a[i]
            a[i]+=1
counter2=(i**2 for i in range(10))          
a=counter()
print(a)
for i in range(10):
    print(next(a))
    

        
        