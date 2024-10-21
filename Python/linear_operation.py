#try to turn octave into python
import numpy as np
import numpy.linalg as npl
import math
import matplotlib.pyplot as plt
m='row_nums';n='col_nums'

                            #basic notes
a=math.pi
A=np.array([[0]])
B=np.array([[0]])
'''0 is row, but remeber max(axis=0) means find max in cols, return list_vector'''
'''1 is column'''
'''index begin from 0'''
'''(3,)means list_vector ,it is same as row_vector\n
but (3,) has no transpose, (1,3) has transpose'''



                        #common used commands
a=f'{a:.5f}'
a='{:.5f}'.format(a)

'''when in ipython'''
'''pwd'''
'''cd'''
'''who'''
'''whos'''
'''reset -f'''
'''xdel value_name'''


                    #load dat or txt or npy or npz
                    #notice present dir
'''bin form'''
np.save('bindata.npy',A)
np.savez('bindata2.npz',A=A,B=B)    #after load return dict,dict[A]=A,dict[B]=B
X=np.load('bindata.npy/npz',mmap_mode=['r+','r','w+','c'])#mmap_mode means map content of data to memory but not copy them to memory(unless mode='c')


'''text form'''
np.savetxt('txt_data.txt',A,fmt='%5.4f',delimiter=';')
'''first column is integer while second is float'''
np.savetxt('txt_data.txt',A,fmt=['%d','{:.4f}'])
X=np.loadtxt('txt_data.txt',delimiter=';',dtype=np.int64)


                        #create matrix
'''notice:python can only use list_vector as x_list'''
list_vector=np.arange('start_close','stop_open','step',dtype=np.float64)
list_vector=np.reshape([1,2,3],3)
A=np.reshape([1,2,3,4],(2,2),order='F')        
'''F means[1,3;2,4] , if default, m=[1,2;3,4]'''


row_vector=np.array([[1,2,3]])
row_vector=np.reshape([1,2,3],(1,3))

column_vector=np.array([[1],[2],[3]])
column_vector=np.reshape([1,2,3],(3,1))

'''notice:if size is not tuple but num, then return list_vector'''
ONE=np.ones((m,n))
ZERO=np.zeros((m,n))
A=np.random.rand(m,n)
A=np.random.randn(m,n)
A=np.random.randint('begin','stop',size=(m,n))
A=np.random.normal(loc='center',scale='scale',size=(m,n))
E=np.eye(m,n)

                    #get info/part of matrix
A=np.array([1,2])
A.shape     #return [row,col]
len('list_vector')
A['row','col']
B=A['row_begin':'row_end+1','col_begin':'col_end+1']

'''get not adjacent lines'''
B=A[['row1','row3']]
B=A[:,['col1','col3']]

'''A and B must have same dimension, list_vector better not use'''
D=np.concatenate([A,B],axis=0 if 'row' else 1)
D=np.vstack([A,B])
D=np.hstack([A,B])
D=np.c_[A,B]    #best column combine
D=np.r_[A,B]    #best row combine

row_A=A.reshape(1,-1)
col_A=A.reshape(-1,1)
R=np.repeat(col_A,"repeat_times",1)

#complicate calculate
A@B                 
np.dot(A,B)             #same as A@B
A+B
A*B                     #A.*B in octave
np.multiply(A,B)        #same as A*B
A+1
A+np.ones_like(A)
npl.matrix_power(A,2)   #A@A
A**2                    #A*A
A.T
A.transpose()
npl.pinv(A)
npl.inv(A)



#useful function
np.exp(A)
np.abs(A)
np.log(A)
np.max(A,axis=0)    #colomn max return row_v
np.max(A,axis=1)    #row max return col_v

A<3
[v1,v2]=np.where(A<3)   #v1 and v2 is list_vector

np.sum(A)
np.sum(A,axis=0)
np.prod(A)
np.prod(A,axis=0)
np.floor(A)
np.ceil(A)
np.flipud(A)        #flip in horizon
np.fliplr(A)        #flip in vertical


#visialization

'''specify step=0.01,do not include 1'''
x=np.arange(0,1,0.01)
'''specify len=100, do include 1'''
x=np.linspace(0,1,100)
y=np.sin(x)


plt.figure(1)
plt.plot(x,y,label='sin')               #one plot one label
plt.xlabel('time')
plt.ylabel('value')
plt.title('name')
plt.legend(loc=0 if 'leftup' else 1)    #choose where to show label
plt.axis(['x_min','x_max','y_min','y_max'])

plt.show()
plt.close('figure_num')

"""show plus"""
f=plt.figure()
ax=f.add_subplot(221)
ax.scatter("x","y")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('pic1')
ax2=f.add_subplot(222)
'''blablabla'''





'''show matric in img'''
plt.imshow(A,cmap='gray',interpolation='nearest')
plt.colorbar()
plt.show()

'''show histogram'''
plt.hist(row_vector,'square_nums')

'''convolution'''
np.convolve([1,2,3],[1,2,3])
