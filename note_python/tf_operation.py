import tensorboard
import tensorflow as tf
import numpy as np


a=tf.constant([1,2],name='a')
b=tf.constant([3,4],name='b')

r=tf.add(a,b,name='a+b')
print('before session,r=',r)

