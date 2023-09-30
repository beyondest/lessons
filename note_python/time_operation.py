import time
def your_process():
    pass

'''influenced by system time, low accuracy'''
time.time()   #return seconds from 1970/1/1 00.00  


   
'''best timing function to calculate time of entire process'''            
time.perf_counter() #return timestamp of a very accurate timer 
t1=time.perf_counter()
your_process()
t2=time.perf_counter()
all_time=t2-t1




'''only return cpu_running_time, do not include read or write or sleep'''
time.process_time() #return timestamp
t1=time.process_time()
your_process()
t2=time.process_time()
cpu_time=t2-t1


#time_decoration

def timing_process(func):
    '''return time_s,out'''
    def inner(*args, **kwargs):
        t1=time.perf_counter()
        out=func(*args,**kwargs)
        t2=time.perf_counter()
        t=t2-t1
        return t,out
    return inner
