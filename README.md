
<div align="center">
  <h1>安全行APP</h1>
</div>

### Product Requirements
|Target release|2020-1|
|---|---|
|Epic|安全行APP|
|Document status|已完成|
|Document owner、Designer、Developer、QA|黄煜惠|


## 目录
- [PRD价值主张设计](# PRD价值主张设计)
    - [背景](## 背景)
    - [目标](## 目标)
    - [目标用户](## 目标用户)
    - [加值宣言](## 加值宣言)
    - [核心价值（最小可行性）](## 核心价值（最小可行性）)
    - [核心价值与用户痛点](## 核心价值与用户痛点)
    - [人工智能概率性与用户痛点](## 人工智能概率性与用户痛点)
    - [需求列表与人工智能API加值](## 需求列表与人工智能API加值)
- [原型](# 原型)
    - [原型文档](## 原型文档)



# PRD价值主张设计
## 背景
交通安全问题被屡屡提起，但是每年仍有很多交通事故发生，原因大多是司机的驾驶行为不当，例如在行驶过程中使用手机、抽烟、不系安全带、双手离开方向盘等等。我们无法保证每一位司机都有足够的安全意识，即使有的司机安全意识高，但也难免会在一些特殊情况下存在驾驶不当的行为，如疲劳驾驶时。

目前，市面上暂时还很少被广泛使用的、能够检测、分析和提醒司机驾驶行为的APP。为了提高行车的安全性，开发一个司机安全驾驶检测APP是有必要的。

## 目标
立足于提高司机的交通安全意识、减少交通事故的发生、保障司机行车安全，开发具有识别、分析、警告司机危险驾驶行为的软件，同时，软件还具备车辆路径规划、语音输入、语音播报等功能。

## 目标用户
司机

## 加值宣言
基于现状，现采用**百度的驾驶行为分析API**对市场上现有的同类产品进行加值和优化，能够实时输入司机的驾驶情况的画面，输出司机安全驾驶的分值，当分值达到警戒值，安全行APP会发出警告的声音，警醒司机。当司机结束一段驾驶路程，APP会给出一个综合驾驶评分。此外，APP还加入**高德地图路径规划API**来进行导航，使用**百度的语音识别API**、**百度在线语音合成API**来实现语音功能，为司机安全驾驶保驾护航。

（主要）
- 驾驶行为分析API首先依托人体分析技术进行驾驶员检测，然后再进行驾驶员行为识别，针对每类属性行为，分别返回概率分数和建议阈值，以此提醒司机。且可针对不同的车载场景，对驾驶员的危险驾驶行为进行识别。

（次要）
- 短语音识别API采用领先国际的流式端到端语音语言一体化建模方法，近场中文普通话识别准确率达98%，方便司机在行车过程中接听电话和操作导航。
- 在线语音合成API基于业界领先的深度神经网络技术，提供高度拟人、流畅自然的语音合成服务，可在手机APP进行语音播报，将文字合成为声音。
- 路径规划API为司机提供道路规划，方便行车。

## 核心价值（最小可行性）
1. 能够检测司机的危险驾驶行为，并对司机发出危险提示信号。
2. 可通过语音识别功能在APP内进行语音操作，如，搜索地址等；通过语音合成功能将提醒信息由文字转换为语音。
3. 提供驾车路径规划功能。

## 核心价值与用户痛点
痛点一：司机独自一人疲劳驾驶时无人提醒，不得不通过抽烟、吃零食的方式提神
- 通过驾驶行为分析API监测司机驾驶，当出现危险的驾驶行为时，会发出语音提示音，警告司机。

痛点二：司机驾驶过程中需要把注意力集中在路面上，不能临时使用手机调取导航
- 将路径规划API的功能嵌入APP，实现路径规划的功能，而语音识别API能够让司机语音操作APP，在线语音合成API能够将文字转换为语音播报信息。
 
## 人工智能概率性与用户痛点
人工智能的准确率并不是百分百的，所以API可能出现以下的问题：
- 驾驶行为分析API：错误识别司机的驾驶行为，在司机正常驾驶的过程中不断发出警告，进而影响司机正常驾驶。
- 驾车路径规划API：路径规划有误，道路改建，API没有及时更新，导致司机走错路。
- 语音识别API：语音识别错误，让部分普通话不太标准的用户产生抵触心理。
- 在线语音合成API：当司机出现危险驾驶行为，而恰好网络不佳时，无法及时提醒司机。

## 需求列表与人工智能API加值

||优先级|需求|API的使用|
|---|---|---|---|
|1|高|用户有时会无意识做出危险的驾驶行为，所以需要被提醒|百度-[驾驶行为分析](https://ai.baidu.com/tech/body/driver)|
|2|中|司机在驾驶过程中突然需要使用导航|高德地图-[驾车路径规划API](https://lbs.amap.com/api/webservice/guide/api/direction#driving)、[语音识别API](https://ai.baidu.com/tech/speech/asr)、[语音合成API](https://ai.baidu.com/tech/speech/tts)|

# 原型
## 原型文档
[**原型文档**](https://github.com/uweier/API_ML_AI/tree/master/%E5%AE%89%E5%85%A8%E8%A1%8CAPP)

[**安全行APP.rp文档下载**](https://github.com/uweier/API_ML_AI/blob/master/%E5%AE%89%E5%85%A8%E8%A1%8CAPP_recovered.rp)

图片加载不出？想体验交互效果？请点击查看[原型](https://nfunm034.gitee.io/api_ml_al_final)

## 信息设计
- 在驾驶行为分析中，使用了驾驶行为分析API的监测功能
- 在驾驶行为分析中，使用了语音识别API和语音合成API的功能
- 在路径规划中，使用了语音识别API和语音合成API的功能

### 产品架构图
![产品架构图](https://github.com/uweier/API_ML_AI/blob/master/API_image/jiagou.png)

### 产品流程图
![产品功能流程图](https://github.com/uweier/API_ML_AI/blob/master/API_image/liucheng.png)

## 交互及界面设计
[交互](https://nfunm034.gitee.io/api_ml_al_final/#g=1&p=%E9%A9%BE%E9%A9%B6%E7%9B%91%E6%B5%8B%E5%89%8D)

驾驶行为监测功能：

![驾驶行为监测1](https://github.com/uweier/API_ML_AI/blob/master/API_image/jiashi1.png)

![驾驶行为监测2](https://github.com/uweier/API_ML_AI/blob/master/API_image/jiashi2.png)

驾驶行为监测语音功能：

![驾驶行为监测语音功能1](https://github.com/uweier/API_ML_AI/blob/master/API_image/jiashi_yuyin1.png)

![驾驶行为监测语音功能2](https://github.com/uweier/API_ML_AI/blob/master/API_image/jiashi_yuyin2.png)

路径规划功能：

![路径规划功能](https://github.com/uweier/API_ML_AI/blob/master/API_image/lujing1.png)

路径规划语音功能：

![路径规划语音功能1](https://github.com/uweier/API_ML_AI/blob/master/API_image/lujing_yuyin1.png)

![路径规划语音功能2](https://github.com/uweier/API_ML_AI/blob/master/API_image/lujing_yuyin2.png)

## 口头操作说明
**1句话版本**

这款安全行APP的主要功能是通过驾驶行为分析API检测司机的危险驾驶行为，除此之外，还有语音合成、语音识别、驾车路径规划的功能。

**1分钟版本**

大家好，今天为大家介绍一款安全行APP，这款APP基于为司机保驾护航目的，监测司机的驾驶过程，识别、分析出司机危险驾驶行为，并通过语音合成向司机发出“口头”警告。同时，司机还可以在行车过程中，通过语音识别的方式进入路径规划页面，使用语音输入起点和终点，开启路径规划功能。为司机带来便利的同时又不忽视交通安全问题。

# API 产品使用关键AI或机器学习之API的输出入展示
## 所使用的API
- 百度API[驾驶行为分析](https://ai.baidu.com/tech/body/driver)
- 高德地图API[驾车路径规划](https://lbs.amap.com/api/webservice/guide/api/direction#driving)
- 百度API[在线语音合成](https://ai.baidu.com/tech/speech/tts)
- 百度API[短语音识别](https://ai.baidu.com/tech/speech/asr)

## 使用水平
核心功能所应用的API之输入及输出代码
- [驾驶行为分析API](https://github.com/uweier/API_ML_AI/blob/master/drive_api.ipynb)
- [驾驶路径规划API](https://github.com/uweier/API_ML_AI/blob/master/driving_api.ipynb)
- [语音识别与语音合成API](https://github.com/uweier/API_ML_AI/blob/master/speech.ipynb)

#### 百度驾驶行为分析API
输入不同的司机驾驶图片，输出关于司机是否双手离开方向盘、使用手机、不系安全带、目视前方、抽烟的数值。

其中的“score”为判断的数值，数值越接近0，则表示“否”，数值越接近1，则表示“是”。
![driver_code](https://upload-images.jianshu.io/upload_images/9460722-79752669265cf4b6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 百度语音合成API
代码见： [语音识别与语音合成API](https://github.com/uweier/API_ML_AI/blob/master/speech.ipynb)

输入文字，输出音频文件，以下为输出代码：

![speech synthesis1](https://upload-images.jianshu.io/upload_images/9460722-936dbc5774989f49.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 百度语音识别API
代码见： [语音识别与语音合成API](https://github.com/uweier/API_ML_AI/blob/master/speech.ipynb)

输入音频文件，输出文字，以下为输出代码：

![speech recognition1](https://upload-images.jianshu.io/upload_images/9460722-029070d35719119a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 高德驾驶路径规划API
输入起点与终点即可得到最佳的路径规划。
![drivering_code](https://upload-images.jianshu.io/upload_images/9460722-9b798bfccc033b01.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 使用比较分析与使用后风险报告
### 百度驾驶行为分析API分析
目前，只找到[百度AI开放平台](https://ai.baidu.com/tech/body/driver)的**驾驶行为分析API**。其定价如下图，该免费调用量足以提供个人日常学习和企业测试的使用，但是对于企业正式开发使用，价格还是较高的。而且对图片有一定的要求，人体必须清晰可见，且服务只适用于车载司机场景，使用网图、非车载场景的普通监控图片、或者乘客的监控图片测试，测试效果会不准。

![drive_fee1](https://upload-images.jianshu.io/upload_images/9460722-b7a294047ba8a87b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![drive_fee2](https://upload-images.jianshu.io/upload_images/9460722-371c10b54ed1d57d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 随着滴滴、出租车、公交车等运营车辆行业的发展及各类交通安全事故的发生，驾驶行为分析及其相关的API需求将增加，所以具有发展性。
- 其输出结果的判断依据还需完善，仅仅依据双手离开方向盘、使用手机、不系安全带、目视前方、抽烟这五个点来判断司机的驾驶行为还不够全面。还应考虑闭眼时长、吃东西等方面的危险驾驶行为。


### 语音识别API分析
|对比项|百度|微软Azure|讯飞|
|---|:---:|:---:|:---:|
|功能/特色|多语种和多方言识别、深度语义解析|自定义的语音识别、灵活的部署|支持多种语种和方言、支持垂直领域和应用级听写|
|价格|基础（免费）、付费版（80元/QPS/天）|基础（每月5小时免费）、标准（每小时音频 $1）|基础（一年免费 需个人认证）、低配版套餐（40元/万次/年）|
|接口|API、SDK|SDK|API、SDK|
|使用难度|低（有python示例代码）|中（有python SDK示例代码）|中（有调用示例）|
|成熟度|高|高|高|
|准确度|中|高|高|
|性价比|高|中|低|
|发展性|高|高|高|


### 语音合成API分析
|对比项|百度|微软Azure|讯飞|
|---|:---:|:---:|:---:|
|功能/特色|多场景音库、语速、音调可调节|逼真的语音、全球参与、自定义体验|专属的语音个性定制|
|价格|基础（免费）、付费版（600-1000元/QPS/天）|基础（每月 500 万个字符免费）、标准（每 100 万个字符 $4）|基础（一年免费 需个人认证）、低配版套餐（58元/万次/年）|
|接口|API、SDK|SDK|API、SDK|
|使用难度|低（有python示例代码）|低（有python SDK示例代码）|中（有调用示例）|
|成熟度|高|高|高|
|准确度|中|高|高|
|性价比|高|低|中|
|发展性|高|高|高|


## 加分项
所使用的API
- 百度驾驶行为分析API
- 高德地图驾车路径规划API
- 百度在线语音合成API
- 百度短语音识别API

核心功能所应用的API之输入及输出代码
- [驾驶行为分析API](https://github.com/uweier/API_ML_AI/blob/master/drive_api.ipynb)
- [驾驶路径规划API](https://github.com/uweier/API_ML_AI/blob/master/driving_api.ipynb)
- [语音识别与语音合成API](https://github.com/uweier/API_ML_AI/blob/master/speech.ipynb)
