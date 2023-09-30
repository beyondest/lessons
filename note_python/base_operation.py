
                    #Decoration


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

        
        