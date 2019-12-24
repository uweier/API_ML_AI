#!/usr/bin/env python
# coding: utf-8

# ## 路径规划API之代码输入输出调试
# 
# [驾车路径规划](https://lbs.amap.com/api/webservice/guide/api/direction#driving)

# In[8]:


import requests

key_api = 'bbefb4b3848672a7a43bf6a4003f19f2'

# 驾车路径规划
def driving(origin,destination):
    "步行路径规划"
    url = 'https://restapi.amap.com/v3/direction/driving?parameters'
    params = {
        'key' : key_api,
        'origin' : origin,
        'destination' : destination,
        'extensions':all,
    }
    response = requests.get(url,params = params)
    data = response.json()
    return data


# In[9]:


driving("113.327023,23.13216","113.35208,23.139325")


# In[ ]:




