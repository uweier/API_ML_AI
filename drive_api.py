#!/usr/bin/env python
# coding: utf-8

# ## 驾驶行为分析API之代码输入输出调试
# 
# [驾驶行为分析API文档](https://ai.baidu.com/ai-doc/BODY/Nk3cpywct)

# In[37]:


# 获取access_token

# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=NkKpaNkEeS2Zh6GbcdwYpcpj&client_secret=FslfBCjm4KID6NDsVSLqWlwM16fsx3zE'
response = requests.get(host)
if response:
    print(response.json())


# ### 测试图片一

# ![driver_test3.jpg](http://img2018.cnblogs.com/news/34358/201907/34358-20190727103933209-605120633.jpg)

# In[38]:


# encoding:utf-8

import requests
import base64
from pprint import pprint

'''
驾驶行为分析
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/driver_behavior"
# 二进制方式打开图片文件
f = open('driver_test3.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.c041ae58223f0995e114baedbbe9b33a.2592000.1579751847.282335-18083464'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    pprint(response.json())


# ![driver_test.jpg](http://thumbs.dreamstime.com/b/%E9%A9%BE%E9%A9%B6%E5%9F%8E%E5%B8%82-%E7%9A%84%E5%85%AC%E5%85%B1%E6%B1%BD%E8%BD%A6%E7%9A%84%E6%84%89%E5%BF%AB%E7%9A%84%E5%8F%B8%E6%9C%BA-68482349.jpg)

# In[39]:


# encoding:utf-8

import requests
import base64
from pprint import pprint

'''
驾驶行为分析
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/driver_behavior"
# 二进制方式打开图片文件
f = open('driver_test2.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.c041ae58223f0995e114baedbbe9b33a.2592000.1579751847.282335-18083464'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    pprint(response.json())


# ## 使用Python SDK也能实现输入输出
# [Python SDK快速入门](https://ai.baidu.com/ai-doc/BODY/Rk3cpyo93)
# 
# [驾驶行为分析SDK文档](https://ai.baidu.com/ai-doc/BODY/Ak3cpymcf)

# In[40]:


from aip import AipBodyAnalysis

""" 你的 APPID AK SK """
APP_ID = '18083464'
API_KEY = 'NkKpaNkEeS2Zh6GbcdwYpcpj'
SECRET_KEY = 'FslfBCjm4KID6NDsVSLqWlwM16fsx3zE'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)


# 

# In[41]:


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('driver_test3.jpg')

""" 调用驾驶行为分析 """
client.driverBehavior(image);

""" 如果有可选参数 """
options = {}
options["type"] = "both_hands_leaving_wheel"


""" 带参数调用驾驶行为分析 """
client.driverBehavior(image, options)


# In[42]:


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('driver_test2.jpg')

""" 调用驾驶行为分析 """
client.driverBehavior(image);

""" 如果有可选参数 """
options = {}
options["type"] = "not_facing_front"

""" 带参数调用驾驶行为分析 """
client.driverBehavior(image, options)


# In[ ]:




