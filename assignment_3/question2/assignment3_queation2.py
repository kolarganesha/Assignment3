#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''2.
Implement a Python program to generate all sentences where subject is in ["Americans",
"Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]'''


# In[5]:


subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
sentence_list = [(i+" "+j+" "+k) for i in subjects for j in verbs for k in objects ]
for s in sentence_list:
    print(s)


# In[ ]:





# In[ ]:




