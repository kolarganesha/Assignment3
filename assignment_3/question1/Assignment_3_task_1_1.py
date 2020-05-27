#!/usr/bin/env python
# coding: utf-8
'''Task 1: 1.
Write a function to compute 5/0 and use try/except to catch the exceptions.'''
# In[3]:


def cal_div(a,b):
    try:
        res=a/b
    except Exception as e:
        print("The exception is : ",e)
        
cal_div(5,0)


# In[ ]:




