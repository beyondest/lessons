
                    #Decoration
a=1
b=0

def operation_before_target_func():
    pass                    
def operation_on_target_func_args(*args, **kwargs):
    return args,kwargs

'''*a turn a into tuple, **a turn a into dict'''
def decoration_function(target_func):
    def change_function(*args, **kwargs):
       operation_before_target_func()
       args,kwargs=operation_on_target_func_args(args,kwargs)
       result=target_func(*args,**kwargs)
       return result
    return change_function

@decoration_function
def target_func():
    pass

'''example'''
def d(func):
    def wrapper(*a,**k):
        print('wrap_working')
        a=[i*2 for i in a]
        return func(*a,**k)
        
    return wrapper
@d
def b(x,y):
    return x+y

print(b(1,3))



   
                        #change variable
                        
'''notice this will not work'''                        
def change(x):
    x+=1
b=1
change(b)!=2  
'''but list will work'''
def change(x:list):
    x[1],x[0]=x[0],x[1]
b=[1,2]
change(b)==[2,1]
      

                        #open() 
'''r        w      '''              #you can combine 1 row with 2 row 
'''+        x       a       b'''    #like r+/wb, but wbx is not available
                                    #'wx' is not availble ,use x is enough
'''+:   allow r/w'''
'''x:   exclusive write'''
'''a:   add to last line write'''
'''bin mode'''

                        #class
class func:
    def __init__(self,a1,a2) :
        self.a1=a1
        self.a2=a2
    def myprint(self):
        print(self.a1)
        print(self.a2)
class myiteration:
    def __init__(self,start,end) :
        self.start=start
        self.end=end
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>=self.end:
            raise StopIteration
        else:
            current_value=self.start
            self.start+=1
            return current_value
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class P:
    def __init__(self) -> None:
        print('i am p')
#use parent class to init, avoid init repeatly 
class C(P):
    def __init__(self) -> None:
        super().__init__()
        print('i am c')    


book = Book("Python Basics", "John Doe")
print(book.__author)        #this will raise error
print(str(book))  
print(repr(book)) 
a=myiteration(1,10)      
func1=func(3,4)
func1.myprint()

'''use this to make dictionary easily'''
class C:
    pass
c=C()
c.x=1
c.y='sd'
c.z=[1,2,3]


                        #assert
assert 1
'''will not raise error, but if assert 0 , it will raise AssertionError'''


                        #enumerate
'''get index and value at the same time'''
a_iterable=['a','b','c','d']
b_iterable=enumerate(a_iterable)
for index,value in b_iterable:
    print(index,value)
    
                        #raise
if a!='str':
    raise TypeError('a must be str')


                        #generator
'''generator is kind of special iteration, which will record last leave position'''
def counter():
    a=[1,2,3,4,5]
    while 1:
        for i in range(5):
            yield a[i]
            a[i]+=1
counter2=(i**2 for i in range(10))          
a=counter()
for i in range(10):
    next(a)
    
                        #with
with open('test.txt','w') as f:
    f.write('hello world')
'''equal to'''

f = open('test.txt','w')
try:
    f.write('hello world')
except Exception as e:
    print(e)
finally:
    f.close()
                        #globle variable
a=1
def change():
'''if you change global variable, you must use global keyword'''
    global a
    a+=1
def not_change():
'''if you dont change global variable, it is safe not to use global keyword'''
    print(a)


            
