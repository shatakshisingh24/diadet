#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
from keras import models
from keras.models import load_model
from tensorflow import keras


# In[17]:



model = keras.models.load_model('www')


# In[30]:


def pred(age,fpg,diabp,sysbp,bmi,avgsugar,wcir,hcir,chol,ogtt):
    mean=np.array([ 47.57372401, 152.46691871,  80.99243856, 130.42627599,
        25.15104344,   7.84291115,  95.4073724 ,  98.72117202,
       237.63610586, 217.36672968])
    dev=np.array([13.949183  , 73.80475753,  4.83384664, 12.72021721,  3.98544049,
        2.3917692 , 11.75528716, 10.05522809, 50.12737702, 91.57451541])
    x=np.zeros(10)
    x[0]=age
    x[1]=fpg
    x[2]=diabp
    x[3]=sysbp
    x[4]=bmi
    x[5]=avgsugar
    x[6]=wcir
    x[7]=hcir
    x[8]=chol
    x[9]=ogtt 
    
    for i in range(0,10):
        x[i]=(x[i]-mean[i])/dev[i]
    x=x.reshape((1,10,-1)) 
    out= model.predict([x])
    
    if(out[0][0]>0.5):
        return 'Diabetic'
    else:
        return 'Non-Diabetic'

   

