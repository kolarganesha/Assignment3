#!/usr/bin/env python
# coding: utf-8
'''Task 2: 1.
Write a function so that the columns of the output matrix are powers of the input vector.
The order of the powers is determined by the increasing boolean argument. Specifically, when
increasing is False, the i-th output column is the input vector raised element-wise to the power
of N - i - 1.'''

# In[2]:


import numpy as np
x = np.array([1, 2, 3, 5])
N = 3
np.vander(x, N)


# In[3]:


np.vander(x, N,increasing=True)


# In[ ]:




