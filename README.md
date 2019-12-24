# 安全行APP
### Product Requirements
|Target release|2019-12|
|---|---|
|Epic|安全行APP|
|Document status|正在进行|
|Document owner、Designer、Developer、QA|黄煜惠|

# PRD价值主张设计
## 背景
交通安全问题被屡屡提起，但是每年仍有很多交通事故发生，原因大多是司机的驾驶行为不当，例如在行驶过程中使用手机、抽烟、不系安全带、双手离开方向盘等等。我们无法保证每一位司机都有足够的安全意识，即使有的司机安全意识高，但也难免会在一些特殊情况下存在驾驶不当的行为，如疲劳驾驶时。

目前，市面上暂时还很少被广泛使用的、能够检测、分析和提醒司机驾驶行为的APP。为了提高行车的安全性，开发一个司机安全驾驶检测APP是有必要的。

## 目标
立足于提高司机的交通安全意识、减少交通事故的发生、保障司机行车安全，开发具有识别、分析、警告司机危险驾驶行为的软件，同时，软件还具备车辆导航、语音识别等功能。安全行APP还可以应用到出租车、客车等运营车辆，实时监控车内情况、保障人身财产安全。

## 目标用户
司机

## 加值宣言
基于现状，现采用**百度的驾驶行为分析API**对市场上现有的同类产品进行加值和优化，能够实时输入司机的驾驶情况的画面，输出司机安全驾驶的分值，当分值达到境界值，安全行APP会发出警告的声音，警醒司机。当司机结束一段驾驶路程，APP会给出一个综合驾驶评分，车辆运营公司可根据此综合评分对司机进行筛选、警告。此外，APP还加入**高德地图路径规划API**来进行导航，使用**百度的语音识别API**、**百度离线语音合成API**来实现语音搜索的功能，为司机安全驾驶保驾护航。

（主要）
- 驾驶行为分析API首先依托人体分析技术进行驾驶员检测，然后再进行驾驶员行为识别，针对每类属性行为，分别返回概率分数和建议阈值，以此提醒司机。且可针对不同的车载场景，对驾驶员的危险驾驶行为进行识别。

（次要）
- 短语音识别API采用领先国际的流式端到端语音语言一体化建模方法，近场中文普通话识别准确率达98%，方便司机在行车过程中接听电话和操作导航。
- 离线语音合成API在无网或弱网环境下，可在手机APP进行语音播报，将文字合成为声音，提供稳定一致、流畅自然的合成体验。
- 路径规划API为司机提供道路规划，方便行车。

## 核心价值（最小可行性）
1. 能够检测司机的危险驾驶行为，并对司机发出危险提示信号。
2. 可通过语音识别功能在APP内进行任何操作，如，接听电话、搜索地址等；通过语音合成功能将提醒信息由文字转换为语音。
3. 提供驾车路径规划功能。

## 核心价值与用户痛点
痛点一：司机独自一人疲劳驾驶时无人提醒，不得不通过抽烟、吃零食的方式提神
- 通过驾驶行为分析API监测司机驾驶，当出现危险的驾驶行为时，会发出语音提示音，警告司机。

痛点二：司机驾驶过程中需要把注意力集中在路面上，不能临时使用手机调取导航
- 将路径规划API的功能嵌入APP，实现导航的功能，而语音识别API能够让司机语音操作APP，离线语音合成API能够将文字转换为语音播报信息。
 
## 人工智能概率性与用户痛点
人工智能的准确率并不是百分百的，所以API可能出现以下的问题：
- 驾驶行为分析API：错误识别司机的驾驶行为，在司机正常驾驶的过程中不断发出警告，进而影响司机正常驾驶。
- 驾车路径规划API：路径规划有误，道路改建，API没有及时更新，导致司机走错路。
- 语音识别API：语音识别错误，让部分普通话不太标准的用户产生抵触心理。
- 语音合成API：

## 需求列表与人工智能API加值

||优先级|需求|API的使用|
|---|---|---|---|
|1|高|用户有时会无意识做出危险的驾驶行为，所以需要被提醒|百度-[驾驶行为分析](https://ai.baidu.com/tech/body/driver)|
|2|中|司机在驾驶过程中突然需要使用导航|高德地图-[驾车路径规划API](https://lbs.amap.com/api/webservice/guide/api/direction#driving)、语音识别API、语音合成API|

# 原型
## 交互及界面设计
交互及界面设计：在PRD文件中是否有说明且原型是否有做到：交互及界面设计的某个核心交互环节使用了人工智能的加值

## 信息设计
信息设计：在PRD文件中是否有说明且原型是否有做到：信息设计的某个核心信息或设计使用了人工智能的加值

## 原型文档
原型文档：多少程度上有提供MVP可交互的原型文档，供它人在Github上下载使用

## 口头操作说明
口头操作说明：多少程度上在2-3分钟时间限制内，对听众留下了「的确这是个可行丶可用的人工智能加值产品」的印象

# API 产品使用关键AI或机器学习之API的输出入展示
## 所使用的API
- 百度API[驾驶行为分析](https://ai.baidu.com/tech/body/driver)
- 高德地图API[驾车路径规划](https://lbs.amap.com/api/webservice/guide/api/direction#driving)
- 百度API[在线语音合成](https://ai.baidu.com/tech/speech/tts)
- 百度API[短语音识别](https://ai.baidu.com/tech/speech/asr)

## 使用水平
核心功能所应用的API之输入及输出
- [驾驶行为分析API](https://github.com/uweier/API_ML_AI/blob/master/drive_api.ipynb)
- [驾驶路径规划API](https://github.com/uweier/API_ML_AI/blob/master/driving_api.ipynb)
- 
- 

#### 驾驶行为分析API
输入不同的司机驾驶图片，会得到关于司机是否双手离开方向盘、使用手机、不系安全带、目视前方、抽烟的数值。

其中的“score”为判断的数值，数值越接近0，则表示“否”，数值越接近1，则表示“是”。
![driver_code](https://upload-images.jianshu.io/upload_images/9460722-79752669265cf4b6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 百度语音合成API
```
# coding=utf-8
import sys
import json

IS_PY3 = sys.version_info.major == 3

if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode

API_KEY = 'Nc8qeti23Pi9qRtfHONjwlRH'
SECRET_KEY = 'toGHyd0ra1dDL8VGq8o6rDBa47Iq7caL'
TEXT = "每天都要加油呀。"

# 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
# 精品音库：5为度小娇，103为度米朵，106为度博文，110为度小童，111为度小萌，默认为度小美 
PER = 4
# 语速，取值0-15，默认为5中语速
SPD = 5
# 音调，取值0-15，默认为5中语调
PIT = 5
# 音量，取值0-9，默认为5中音量
VOL = 5
# 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
AUE = 3

FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
FORMAT = FORMATS[AUE]
CUID = "123456PYTHON"
TTS_URL = 'http://tsn.baidu.com/text2audio'
class DemoError(Exception):
    pass

"""  TOKEN start """
TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选

def fetch_token():
    print("fetch token begin")
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()
    print(result_str)
    result = json.loads(result_str)
    print(result)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not SCOPE in result['scope'].split(' '):
            raise DemoError('scope is not correct')
        print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')

"""  TOKEN end """

if __name__ == '__main__':
    token = fetch_token()
    tex = quote_plus(TEXT)  # 此处TEXT需要两次urlencode
    print(tex)
    params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
              'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

    data = urlencode(params)
    print('test on Web Browser' + TTS_URL + '?' + data)
    req = Request(TTS_URL, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        headers = dict((name.lower(), value) for name, value in f.headers.items())
        has_error = ('content-type' not in headers.keys() or headers['content-type'].find('audio/') < 0)
    except  URLError as err:
        print('asr http response http code : ' + str(err.code))
        result_str = err.read()
        has_error = True
    save_file = "error.txt" if has_error else 'result.' + FORMAT
    with open(save_file, 'wb') as of:
        of.write(result_str)
    if has_error:
        if (IS_PY3):
            result_str = str(result_str, 'utf-8')
        print("tts api  error:" + result_str)
    print("result saved as :" + save_file)
```

#### 驾驶路径规划API
输入起点与终点即可得到最佳的路径规划。
![drivering_code](https://upload-images.jianshu.io/upload_images/9460722-9b798bfccc033b01.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 使用比较分析
使用比较分析：在PRD文件中是否有说明且提供连结证据，所使用的API是查找过最适用的（主要竞争者无或比较次），如考量其成熟度丶性价比丶等等
#### 百度驾驶行为分析API分析
目前，只找到[百度AI开放平台](https://ai.baidu.com/tech/body/driver)的**驾驶行为分析API**。其定价如下图，该调用量足以提供日常学习的使用，性价比较高。但是对图片有一定的要求，人体必须清晰可见，且服务只适用于车载司机场景，使用网图、非车载场景的普通监控图片、或者乘客的监控图片测试，测试效果会不准，所以还不够成熟。

![drive_fee1](https://upload-images.jianshu.io/upload_images/9460722-b7a294047ba8a87b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![drive_fee2](https://upload-images.jianshu.io/upload_images/9460722-2a4c1f0c2e6f7652.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![drive_fee3](https://upload-images.jianshu.io/upload_images/9460722-371c10b54ed1d57d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 使用后风险报告
使用后风险报告：在PRD文件中是否有说明且提供连结证据，所使用的API类别的现在及未来发展性，如API市场竞争程度丶输入输出限制丶定价丶及可替代的程序库（改用自己开发的代码及数据库而不用API）等等

#### 百度驾驶行为分析API
- 随着滴滴、出租车、公交车等运营车辆行业的发展及各类安全事故的发生，驾驶行为分析及其相关的API需求将增加。
- 其输出结果的判断依据还需完善，仅仅依据双手离开方向盘、使用手机、不系安全带、目视前方、抽烟这五个点来判断司机的驾驶行为还不够全面。还应考虑闭眼时长、吃东西等方面的危险驾驶行为。


## 加分项
使用复杂度：用了2个以上机器学习与人工智能的API之输入及输出
