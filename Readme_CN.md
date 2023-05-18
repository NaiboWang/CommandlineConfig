# 请您Star

如果你觉得此工具不错，请轻轻点击此页面右上角**Star**按钮增加项目曝光度，谢谢！

# 简洁命令行配置工具

一个供用户以Python Dict或JSON格式编写（科研中实验）配置的库，在代码中用点.读写属性，同时可以从命令行中读取参数配置并修改参数值。

## 保留字段

以下字段为保留字段，不可用于配置参数名，否则会报错：

* `config_name`，用于存储配置字典

## 新特性

### v2.2.*
* 支持字典内参数无限层级嵌套
* 自动版本检查
* 支持参数值限定为指定值（枚举）
* 支持元组类型tuple
* 支持从本地JSON文件中读取配置
* 可设置参数帮助，并通过命令行-h打印参数说明
* 文档更新提供简单示例

## 简单示例

```python
# 通过pip安装
pip3 install commandline_config

# 导包
from commandline_config import Config

# 定义配置字典
config = {
  "index":1,
  "lr": 0.1,
  "dbinfo":{
    "username":"NUS"
  }
}

# 根据配置生成配置类
c = Config(config)

# 打印参数配置
print(c)

# 代码中通过点.直接读写参数，支持多层：
c.index = 2
c.dbinfo.username = "ZJU"
print(c.index, c.dbinfo.username, c["lr"])

# 在命令行中，通过--修改参数值：
python example.py --index 3 --dbinfo.username XDU

# 代码中通过help方法，或命令行中通过-h或-help来获取参数说明（需要自定义，详情请看下面详细文档）
c.help()

python example.py -h
```

##  目录
- [请您Star](#%E8%AF%B7%E6%82%A8star)
- [简洁命令行配置工具](#%E7%AE%80%E6%B4%81%E5%91%BD%E4%BB%A4%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B7%A5%E5%85%B7)
  - [简单示例](#%E7%AE%80%E5%8D%95%E7%A4%BA%E4%BE%8B)
  - [目录](#%E7%9B%AE%E5%BD%95)
  - [使用方式](#%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%8F)
    - [请提出issue](#%E8%AF%B7%E6%8F%90%E5%87%BAissue)
    - [安装方法](#%E5%AE%89%E8%A3%85%E6%96%B9%E6%B3%95)
    - [配置方式](#%E9%85%8D%E7%BD%AE%E6%96%B9%E5%BC%8F)
    - [配置参数读写方式](#%E9%85%8D%E7%BD%AE%E5%8F%82%E6%95%B0%E8%AF%BB%E5%86%99%E6%96%B9%E5%BC%8F)
      - [写入方式](#%E5%86%99%E5%85%A5%E6%96%B9%E5%BC%8F)
      - [读取方式](#%E8%AF%BB%E5%8F%96%E6%96%B9%E5%BC%8F)
      - [传递配置给函数](#%E4%BC%A0%E9%80%92%E9%85%8D%E7%BD%AE%E7%BB%99%E5%87%BD%E6%95%B0)
      - [拷贝配置](#%E6%8B%B7%E8%B4%9D%E9%85%8D%E7%BD%AE)
      - [配置参数存储至本地或数据库](#%E9%85%8D%E7%BD%AE%E5%8F%82%E6%95%B0%E5%AD%98%E5%82%A8%E8%87%B3%E6%9C%AC%E5%9C%B0%E6%88%96%E6%95%B0%E6%8D%AE%E5%BA%93)
  - [高级配置](#%E9%AB%98%E7%BA%A7%E9%85%8D%E7%BD%AE)
    - [限制参数输入值为固定枚举类型](#%E9%99%90%E5%88%B6%E5%8F%82%E6%95%B0%E8%BE%93%E5%85%A5%E5%80%BC%E4%B8%BA%E5%9B%BA%E5%AE%9A%E6%9E%9A%E4%B8%BE%E7%B1%BB%E5%9E%8B)
    - [打印参数帮助说明](#%E6%89%93%E5%8D%B0%E5%8F%82%E6%95%B0%E5%B8%AE%E5%8A%A9%E8%AF%B4%E6%98%8E)
      - [设置参数说明](#%E8%AE%BE%E7%BD%AE%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)
      - [打印参数帮助](#%E6%89%93%E5%8D%B0%E5%8F%82%E6%95%B0%E5%B8%AE%E5%8A%A9)
  - [注意事项](#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)
    - [与Argparse冲突](#%E4%B8%8Eargparse%E5%86%B2%E7%AA%81)
    - [输入值会自动强制转换为默认值对应类型](#%E8%BE%93%E5%85%A5%E5%80%BC%E4%BC%9A%E8%87%AA%E5%8A%A8%E5%BC%BA%E5%88%B6%E8%BD%AC%E6%8D%A2%E4%B8%BA%E9%BB%98%E8%AE%A4%E5%80%BC%E5%AF%B9%E5%BA%94%E7%B1%BB%E5%9E%8B)
    - [list参数命令行赋值时字符串元素引号前需加反斜线](#list%E5%8F%82%E6%95%B0%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%B5%8B%E5%80%BC%E6%97%B6%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%85%83%E7%B4%A0%E5%BC%95%E5%8F%B7%E5%89%8D%E9%9C%80%E5%8A%A0%E5%8F%8D%E6%96%9C%E7%BA%BF)
    - [tuple参数命令行赋值时需加引号，且字符串元素引号前需加反斜线](#tuple%E5%8F%82%E6%95%B0%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%B5%8B%E5%80%BC%E6%97%B6%E9%9C%80%E5%8A%A0%E5%BC%95%E5%8F%B7%E4%B8%94%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%85%83%E7%B4%A0%E5%BC%95%E5%8F%B7%E5%89%8D%E9%9C%80%E5%8A%A0%E5%8F%8D%E6%96%9C%E7%BA%BF)
    - [参数命名规范](#%E5%8F%82%E6%95%B0%E5%91%BD%E5%90%8D%E8%A7%84%E8%8C%83)
    - [嵌套对象层数可无限](#%E5%B5%8C%E5%A5%97%E5%AF%B9%E8%B1%A1%E5%B1%82%E6%95%B0%E5%8F%AF%E6%97%A0%E9%99%90)
    - [参数完整性检查，所有要修改的参数必须预定义](#%E5%8F%82%E6%95%B0%E5%AE%8C%E6%95%B4%E6%80%A7%E6%A3%80%E6%9F%A5%E6%89%80%E6%9C%89%E8%A6%81%E4%BF%AE%E6%94%B9%E7%9A%84%E5%8F%82%E6%95%B0%E5%BF%85%E9%A1%BB%E9%A2%84%E5%AE%9A%E4%B9%89)
    - [ZSH环境特殊配置](#zsh%E7%8E%AF%E5%A2%83%E7%89%B9%E6%AE%8A%E9%85%8D%E7%BD%AE)
  - [完整转换示例](#%E5%AE%8C%E6%95%B4%E8%BD%AC%E6%8D%A2%E7%A4%BA%E4%BE%8B)
  - [运行脚本示例](#%E8%BF%90%E8%A1%8C%E8%84%9A%E6%9C%AC%E7%A4%BA%E4%BE%8B)
  - [碎碎念](#%E7%A2%8E%E7%A2%8E%E5%BF%B5)
  - [待开发](#%E5%BE%85%E5%BC%80%E5%8F%91)

## 使用方式

### 请提出issue

使用过程中遇到任何问题，请在此项目的github页面中提出issue，我将在第一时间解决遇到的bug和问题。

**当有什么新功能您想添加到此工具中时，也请提交issue，我将在第一时间开发。**

### 安装方法

两种方法安装此库：

* 1. 通过pip安装：

  ```shell
  pip3 install commandline_config
  ```
  
  已安装的可通过以下命令升级：
  
  ```shell
  pip3 install commandline_config --upgrade
  ```

* 2. 直接导入github项目中/commandline_config文件夹下的commandline_config.py文件到自己的项目目录中即可，需要安装依赖包prettytable:
  
    ```shell
    pip3 install prettytable
    ```
    
    或通过requirements.txt安装：
    
    ```shell
    pip3 install -r requirements.txt
    ```
  
### 配置方式

* 0. 导入包：
  
    ```python
    from commandline_config import Config
    ```

* 1. 以JSON/Python Dict形式设定参数名称和初始值，并通过#注释方式添加参数描述。目前支持嵌套**无限层**dict。

    ```python
    preset_config = {
          "index": 1,  # Index of party
          "dataset": "mnist",
          'lr': 0.01,  # learning rate
          'normalization': True,
          "pair": (1,2),
          "multi_information": [1, 0.5, 'test', "TEST"],  # list
          "dbinfo": {
              "username": "NUS",
              "password": 123456,
              "retry_interval_time": 5.5,
              "save_password": False,
              "pair": ("test",3),
              "multi":{
                  "test":0.01,
              },
              "certificate_info": ["1", 2, [3.5]],
          }
      }
    ```
  
  即生成了程序的初始配置，在preset_config dict中定义的每一个key为参数名称，每一个value为参数的初始值，同时，参数的初始值类型会根据设置的值的类型自动检测。

  如上方配置中包含七个参数：index， dataset， batch， normalization, pair, multi_information和dbinfo， 其中参数**index**的类型会自动检测为**int**，默认值为**1**，描述为“Index of party”。

  同理，第二至六个参数的的类型和默认值分别为string:"mnist"； float:0.01； bool:True；tuple:(1,2)； list:[1,0.5,'test',"TEST"]。

  第七个参数是一个嵌套的字典，类型为dict，里面同样包含七个参数，类型和默认值和第一至七个参数同理，此处不再赘述。

* 2. 在任意函数中通过将preset_config传递给Config类来创建配置类对象。

    ```python
    if __name__ == '__main__':
        config = Config(preset_config)
        # 或者给配置设定名称：
        config_with_name = Config(preset_config, name="Federated Learning Experiments")

        # 或者可以将preset_config存储到如configuration.json文件中，并给Config类传递文件名：
        config_from_file = Config("configuration.json")
    ```

  即成功生成配置对象。

* 3. 可通过print直接打印参数配置：
  
  ```python
  print(config_with_name)
  ```

  输出结果为：
  
  ```
  Configurations of Federated Learning Experiments:
  +-------------------+-------+--------------------------+
  |        Key        |  Type | Value                    |
  +-------------------+-------+--------------------------+
  |       index       |  int  | 1                        |
  |      dataset      |  str  | mnist                    |
  |         lr        | float | 0.01                     |
  |   normalization   |  bool | True                     |
  |        pair       | tuple | (1, 2)                   |
  | multi_information |  list | [1, 0.5, 'test', 'TEST'] |
  |       dbinfo      |  dict | See sub table below      |
  +-------------------+-------+--------------------------+

  Configurations of dict dbinfo:
  +---------------------+-------+---------------------+
  |         Key         |  Type | Value               |
  +---------------------+-------+---------------------+
  |       username      |  str  | NUS                 |
  |       password      |  int  | 123456              |
  | retry_interval_time | float | 5.5                 |
  |    save_password    |  bool | False               |
  |         pair        | tuple | ('test', 3)         |
  |        multi        |  dict | See sub table below |
  |   certificate_info  |  list | ['1', 2, [3.5]]     |
  +---------------------+-------+---------------------+

  Configurations of dict multi:
  +------+-------+-------+
  | Key  |  Type | Value |
  +------+-------+-------+
  | test | float | 0.01  |
  +------+-------+-------+
  ```

  这里默认会以表格形式打印所有参数的信息，如想要改变打印方式，可通过`config_with_name.set_print_style(style='')`的方式修改，style可取的值有：`both`，`table`，`json`分别表示同时打印表格和json，只打印表格，只打印json字典。

  如：

  ```python
  # 只打印json
  config_with_name.set_print_style('json')
  print(config_with_name)
  print("----------")
  # 同时打印表格和json
  config_with_name.set_print_style('table')
  print(config_with_name)
  ```

  输出结果为：

  ```
  Configurations of Federated Learning Experiments:
  {'index': 1, 'dataset': 'mnist', 'lr': 0.01, 'normalization': True, 'pair': (1, 2), 'multi_information': [1, 0.5, 'test', 'TEST'], 'dbinfo': 'See below'}

  Configurations of dict dbinfo:
  {'username': 'NUS', 'password': 123456, 'retry_interval_time': 5.5, 'save_password': False, 'pair': ('test', 3), 'multi': 'See below', 'certificate_info': ['1', 2, [3.5]]}

  Configurations of dict multi:
  {'test': 0.01}

  ----------
    
  Configurations of Federated Learning Experiments:
  +-------------------+-------+--------------------------+
  |        Key        |  Type | Value                    |
  +-------------------+-------+--------------------------+
  |       index       |  int  | 1                        |
  |      dataset      |  str  | mnist                    |
  |         lr        | float | 0.01                     |
  |   normalization   |  bool | True                     |
  |        pair       | tuple | (1, 2)                   |
  | multi_information |  list | [1, 0.5, 'test', 'TEST'] |
  |       dbinfo      |  dict | See sub table below      |
  +-------------------+-------+--------------------------+
  {'index': 1, 'dataset': 'mnist', 'lr': 0.01, 'normalization': True, 'pair': (1, 2), 'multi_information': [1, 0.5, 'test', 'TEST'], 'dbinfo': 'See below'}

  Configurations of dict dbinfo:
  +---------------------+-------+---------------------+
  |         Key         |  Type | Value               |
  +---------------------+-------+---------------------+
  |       username      |  str  | NUS                 |
  |       password      |  int  | 123456              |
  | retry_interval_time | float | 5.5                 |
  |    save_password    |  bool | False               |
  |         pair        | tuple | ('test', 3)         |
  |        multi        |  dict | See sub table below |
  |   certificate_info  |  list | ['1', 2, [3.5]]     |
  +---------------------+-------+---------------------+
  {'username': 'NUS', 'password': 123456, 'retry_interval_time': 5.5, 'save_password': False, 'pair': ('test', 3), 'multi': 'See below', 'certificate_info': ['1', 2, [3.5]]}

  Configurations of dict multi:
  +------+-------+-------+
  | Key  |  Type | Value |
  +------+-------+-------+
  | test | float | 0.01  |
  +------+-------+-------+
  {'test': 0.01}
  ```


### 配置参数读写方式

#### 写入方式

可通过三种方式写入配置参数值。

* 1. 接收命令行参数，只需要在命令行通过--index 1传递即可修改index的值为1，同时，不同类型的参数传递的注意事项为：

  * 传递bool类型时，可使用0或False来表示False，使用1或True或参数后面不带任何值来表示True：即--normalization 1或--normalization True或--normalization都可以将配置中normalization的参数值设定为True.
  * 传递list类型时，可传递空数组及多维数组。
  * 修改嵌套对象中的值，请使用"--嵌套参数名.子参数名.子参数名.….子参数名 值"的方式修改嵌套对象中的值，如--dbinfo.password 987654即可将dbinfo子对象内的password参数值改为987654，--dbinfo.multi.test 1即可将dbinfo子对象内的multi子对象内的test参数数值改为1。注意，不可直接操作dbinfo本身，如--dbinfo {'password':987654}的写法是错误的。目前此工具支持无限层嵌套。
  * 注意，**参数index必须在上面定义的preset_config对象中：**
  
  ```python
  python test.py --dbinfo.password 987654 --dbinfo.multi.test 1 --index 0 --dataset emnist --normalization 0 --multi_information [\'sdf\',1,\"3.3\",,True,[1,[]]] 
  ```

* 2. 直接在代码中使用`config.index = 2`来修改参数index的值为2，同样，list类型参数可以赋值为为空或多维数组。对于嵌套对象，可使用`config.dbinfo.save_password=True`的方式修改dbinfo中save_password参数的值为True。

* 3. 1和2两种方式会触发类型检查，即如果赋的值类型和预定义字典preset_config中默认值的类型不匹配时程序将报错，因此，如果不想进行强制类型检查，可通过`config["index"] = "sdf"`强行修改参数index的值为字符串sdf（不推荐，会造成意想不到的影响）。

#### 读取方式

直接通过config.dataset或者config["dataset"]的方式读取参数dataset的值：

```python
print(config.dataset, config["index"])
```

一个参数a的值将被读取为：最后通过config.a = * 修改的值 > 通过命令行指定的--a 2的值 > 通过preset_config定义的"a":1指定的初始值。

对于list类型如果传递了多维数组，直接像正常使用数组一样读取信息即可：

```python
config.dbinfo.certificate_info = [1,[],[[2]]]
print(config.dbinfo.certificate_info[2][0][0])
```

对于单层嵌套对象中的参数，共有四种读取方式，均可读取到参数的值：

```
print(config.dbinfo.username)
print(config["dbinfo"].password)
print(config.dbinfo["retry_interval_time"])
print(config["dbinfo"]["save_password"])
```

#### 传递配置给函数

直接将上面的config对象作为参数传递给函数并调用即可：

```python
def print_dataset_name(c):
  print(c.dataset, c["dataset"], c.dbinfo.certificate_info)

print_dataset_name(c=config)
```

#### 拷贝配置

通过deepcopy方法对配置对象进行深拷贝即可：

```python
from copy import deepcopy
copy_config = deepcopy(config)
# 修改新复制的配置参数值，不会影响原配置
copy_config.index=15 
```

#### 配置参数存储至本地或数据库

整个参数配置可以json方式存储到本地文件中，或者上传到如mongodb的远程服务器：

存储文件时，只需要通过`config.save()`将配置存储为指定目录的`配置名称（如无名称则为config）.json`文件，或可指定文件名和路径：

```python
config.save("config/test_config.json")
```

即我们成功地将配置保存到本地的`config`文件夹下的`configuration.json`文件。该文件内容如下。

```json
{
  "index": 1,
  "dataset": "mnist",
  "lr": 0.01,
  "normalization": true,
  "pair": [1, 2],
  "multi_information": [1, 0.5, "test", "TEST"],
  "dbinfo": {
    "username": "NUS",
    "password": 123456,
    "retry_interval_time": 5.5,
    "save_password": false,
    "pair": ["test", 3],
    "multi": { "test": 0.01 },
    "certificate_info": ["1", 2, [3.5]]
  }
}
```

若想将配置信息存储到数据库中，如`mongodb`，你需要先用`info = config.get_config()`命令获得参数对应的json序列，然后用`json`库将其序列化。

例如，要将`config_with_name`配置存储到`mongodb`：

```python
import pymongo
myclient = pymongo.MongoClient('mongodb://username:example.com:27017/', connect=False)
mydb = myclient['exps']
table = mydb["table"]
# 得到配置信息
configuration = config.get_config()
# 插入配置信息到mongodb数据库
table.insert_one(configuration)

# 或者作为一个大型dict的一部分
all_info = {
  "exp_time":"20220925",
  "configuration":configuration
}
table.insert_one(all_info)
```

需要注意的是，由于tuple类型不被JSON支持，因此，不论是本地文件还是存储到数据库，tuple类型的参数都会被转换为list存储。

## 高级配置

### 限制参数输入值为固定枚举类型

通过传递Config参数的options参数至Config类以设置高级选项，这里是设置枚举Enum类型。

```python
option={}
config = Config(preset_config, options=option)
```

如想要某参数的值限定在某范围，则可以通过配置：

```python
advanced_options = {
    'lr': {
        "enum": [0.001, 15.5, 0.01, 0.1] # 限制lr值只能取0.001，15.5，0.01，0.1中的一个
    },
    'index': {
        "enum": [1, 2, 3] # 限制index值只能设置为1，2和3
    },
    "dbinfo": {
        "username": {
            "enum": ["XDU", "ZJU", "NUS"] # 限制dbinfo.username字段只能输入XDU，ZJU和NUS
        },
        "multi":{
            "test":{
                "enum": [1,0.1, 0.01, 15] # 三级嵌套
            }
        }
    },
}

config = Config(preset_config, options=advanced_options)
```

如设置了enum，则以下三种方式设置为限定值以外的值，均会报错：

* 1. 在preset_config中设置了index的初始值为1,2,3以外的值

  ```python
  preset_config = {
    "index":4,
  }
  ```

* 2.命令行为lr参数传递了非限定值

  ```shell
  python example.py --lr 0.02
  ```

* 3. 代码中修改了dbinfo.username的值为XDU，ZJU和NUS以外的值：

  ```python
  config.dbinfo.username = "UEST"
  ```

  输出分别为：

  ```Shell
  AttributeError: Can not set value 4 because the key 'index' has set enum list and you the value 4 is not in the enum list [1, 2, 3]!

  AttributeError: Can not set value 0.02 because the key 'lr' has set enum list and you the value 0.02 is not in the enum list [0.001, 15.5, 0.01, 0.1]!

  AttributeError: Can not set value nus because the key 'username' has set enum list and you the value nus is not in the enum list ['XDU', 'ZJU', 'NUS']!
  ```

### 打印参数帮助说明

#### 设置参数说明

通过在Config类指定helpers参数来设置参数说明helpers：

```python
helpers = {
    "index": "index of information",
    "dbinfo_help": "information dict for database",
    "dbinfo": {
        "username": "username for database",
         "multi":{
            "test":"test information"
        }
    }
}

config = Config(preset_config, helpers=helpers)
```

注意，由于dbinfo参数为dict，因此若想给dbinfo设置参数说明，则需要在helpers字典中设置一个dbinfo_help参数来写说明，即在dict参数名后加_help来设置dict字段的参数说明。

#### 打印参数帮助

两种方式打印参数说明，命令行传递-h或-help，以及在代码中调用config.help()函数：

```python
config_with_name.help()
```

或

```shell
python example.py -h
# 或
python example.py -help
```
注意是一个短斜线且不可加任何其他命令行参数，才可获取帮助说明，两种方式输出结果均为：

```
Parameter helps for Federated Learning Experiments:
+-------------------+-------+-------------------------------+
|        Key        |  Type | Comments                      |
+-------------------+-------+-------------------------------+
|       index       |  int  | index of information          |
|      dataset      |  str  | -                             |
|         lr        | float | -                             |
|   normalization   |  bool | -                             |
|        pair       | tuple | -                             |
| multi_information |  list | -                             |
|       dbinfo      |  dict | information dict for database |
+-------------------+-------+-------------------------------+

Parameter helps for dict dbinfo:
+---------------------+-------+-----------------------+
|         Key         |  Type | Comments              |
+---------------------+-------+-----------------------+
|       username      |  str  | username for database |
|       password      |  int  | -                     |
| retry_interval_time | float | -                     |
|    save_password    |  bool | -                     |
|         pair        | tuple | -                     |
|        multi        |  dict | Multiple Parameters   |
|   certificate_info  |  list | -                     |
+---------------------+-------+-----------------------+

Parameter helps for dict multi:
+------+-------+------------------+
| Key  |  Type | Comments         |
+------+-------+------------------+
| test | float | test information |
+------+-------+------------------+
```


## 注意事项

### 与Argparse冲突
此包无法和argparse包同时读取命令行参数，因此使用此包请不要同时使用args = parser.parse_args()来读取命令行参数。
  
### 输入值会自动强制转换为默认值对应类型
参数的类型将自动检测为preset_config中设定的初始值类型，同时命令行参数的值将被强制转换为对应类型值，如上面的preset_config中的index的默认值为1，则参数index的类型为int，初始值为1，此时如在命令行中指定--index 15.5则将会自动将参数index赋值为15，即自动将15.5强制转换为int类型。

无法转换的命令行参数将会报错，如命令行指定--index sdf，由于sdf字符串无法强制转换为int类型，因此会报错。


### list参数命令行赋值时字符串元素引号前需加反斜线

命令行参数设置为输入list类型时，如果list中元素是字符串，则必须在每个单/双引号前加入反斜线\以正确解析，否则参数值会被视作int或float类型。如果命令行中有空格会被自动合并（但命令行环境不能是zsh，如果是zsh环境则必须去除list内部所有的空格，bash和sh不存在此问题，即在zsh环境下，`--a [15,\'12\']`的15和\\'12\\'之间不得有空格）。

如参数可设置为： 

```
python test.py --array [1,2.3,\'sdf\',\"msg\"] 
```

即可正确解析array参数，其值为一个list，内容为[1,2.3,'sdf',"msg"],即一个包含int, float, string类型的list。

### tuple参数命令行赋值时需加引号，且字符串元素引号前需加反斜线

命令行参数设置为输入tuple类型时，需使用引号包含指定的tuple类型值；且如果tuple中元素是字符串，则必须在每个单/双引号前加入反斜线\以正确解析，否则参数值会被视作int或float类型。同样，如果命令行中有空格会被自动合并（但命令行环境不能是zsh，如果是zsh环境则必须去除内部所有的空格，bash和sh不存在此问题）。

如参数可设置为： 

```
python test.py --pair "(1,2,\'msg\')"
```

即可正确解析pair参数，其值为一个tuple，内容为(1,2,"msg"),即一个包含int, float, string类型的tuple。



### 参数命名规范

参数名称中如包含特殊字符如-+.空格等python保留字符，则必须使用中括号的方式读写参数值，不能使用.号，如参数名称为*multi-information*，则只能通过config["multi-information"]的方式访问，不能通过config.multi-information访问，因为减号-为python语言保留名称。

### 嵌套对象层数可无限
目前已支持嵌套无限层对象，其他支持的参数类型为：int, float, string, bool, tuple和list。

### 参数完整性检查，所有要修改的参数必须预定义
命令行中传递的参数名称**必须提前在preset_config中定义，否则会报错**，如：

```python
python test.py --arg1 1
```

由于参数名arg1没有在preset_config中定义，因此会报错，提示arg1参数未定义，设置此功能是为了进行参数完整性检查，从而避免通过命令行输入错误参数名。

### ZSH环境特殊配置
在ZSH Shell环境下传递list参数时，如果出现`zsh: no matches found`的错误，则需要在`~/.zshrc`文件的最后加入一行`setopt no_nomatch`，保存后在命令行运行`source ~/.zshrc`刷新zsh即可。


## 完整转换示例

下面将给出一个例子来证明此工具相比于argparse工具的便利性。

使用argparse工具需要写的代码：

```python
parser = argparse.ArgumentParser(description='PyTorch local error training')
parser.add_argument('--model', default='vgg8b',
                    help='model, mlp, vgg13, vgg16, vgg19, vgg8b, vgg11b, resnet18, resnet34, wresnet28-10 and more (default: vgg8b)')
parser.add_argument('--dataset', default='CIFAR10',
                    help='dataset, MNIST, KuzushijiMNIST, FashionMNIST, CIFAR10, CIFAR100, SVHN, STL10 or ImageNet (default: CIFAR10)')
parser.add_argument('--batch-size', type=int, default=128,
                    help='input batch size for training (default: 128)')
parser.add_argument('--num-layers', type=int, default=1,
                    help='number of hidden fully-connected layers for mlp and vgg models (default: 1')
parser.add_argument('--lr', type=float, default=5e-4,
                    help='initial learning rate (default: 5e-4)')
parser.add_argument('--lr-decay-milestones', nargs='+', type=int, default=[200,300,350,375],
                    help='decay learning rate at these milestone epochs (default: [200,300,350,375])')
parser.add_argument('--optim', default='adam',
                    help='optimizer, adam, amsgrad or sgd (default: adam)')
parser.add_argument('--beta', type=float, default=0.99,
                    help='fraction of similarity matching loss in predsim loss (default: 0.99)')
args = parser.parse_args()

args.cuda = not args.no_cuda and torch.cuda.is_available()
if args.cuda:
    cudnn.enabled = True
    cudnn.benchmark = True
```

转换为此工具后需要写的代码：

```python
'''
:param model: model, mlp, vgg13, vgg16, vgg19, vgg8b, vgg11b, resnet18, resnet34, wresnet28-10 and more (default: vgg8b)
:param dataset: dataset, MNIST, KuzushijiMNIST, FashionMNIST, CIFAR10, CIFAR100, SVHN, STL10 or ImageNet (default: CIFAR10)
:param batch-size: input batch size for training (default: 128)
:param num-layers: number of hidden fully-connected layers for mlp and vgg models (default: 1)
:param lr: initial learning rate (default: 5e-4)
:param lr-decay-milestones: decay learning rate at these milestone epochs (default: [200,300,350,375])
:param optim: optimizer, adam, amsgrad or sgd (default: adam)
:param beta: fraction of similarity matching loss in predsim loss (default: 0.99)
'''
config = {
  'model':'vgg8b',
  'dataset':'CIFAR10',
  'batch-size':128,
  'num-layers':1,
  'lr':5e-4,
  'lr-decay-milestones':[200,300,350,375],
  'optim':'adam',
  'beta':0.99,
}
args = Config(config, name='PyTorch local error training')

args.cuda = not args.no_cuda and torch.cuda.is_available()
if args.cuda:
    cudnn.enabled = True
    cudnn.benchmark = True
```

可以看到，代码量降低并且更加结构，整洁。

另外一个Click的例子：

```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
```

可转换为下面的代码：

```python
from commandline_config import Config

def hello(o):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(o.count):
        print(f"Hello {o.name}!")

if __name__ == '__main__':
    args = {
      "count":1, # Number of greetings.
      "name":"", # The person to greet.
    }
    options = Config(args)
    hello(options)
```
## 运行脚本示例

你可以运行Github项目中的`example.py`来测试整个工具，大部分功能的代码已经在文件中提供。

```
# 获取 example.py所有参数的帮助
python example.py -h
# 指定参数值
python example.py --dbinfo.multi.test 0.01 --dbinfo.username NUS
```

## 碎碎念

以下描述了作者个人的开发原因以及此包的好处/便利性。

对于经常跑科研实验的朋友们，大家是不是经常需要在python文件开头设置大量的命令行参数，并在下方代码中以args.*的方式调用：

比如下面的这段示例：

```python
parser = argparse.ArgumentParser(description='index')
parser.add_argument('--index', default=0, type=int, help='party index')
parser.add_argument('--party_num', default=100, type=int)
args = parser.parse_args()

print(args.index)
```

每多一个参数，代码中就会多一行parser.add_argument，手写每个参数的配置时会很繁琐，如名称需要加--，还有修改默认值，类型以及描述的时候很麻烦，最后也会导致自己的代码很冗长，维护不便。

就算用了更高级一点的Click，也需要不停的写option, 而且有几个option对应函数就要写几个输入参数与之匹配，写代码实在是繁琐，比如以下Click代码：

```python
import click

from caesar_encryption import encrypt

@click.command()
@click.argument('text', nargs=-1)
@click.option('--decrypt/--encrypt', '-d/-e')
@click.option('--key', '-k', default=1)
def caesar(text, decrypt, key):
    text_string = ' '.join(text)
    if decrypt:
        key = -key
    cyphertext = encrypt(text_string, key)
    click.echo(cyphertext)

if __name__ == '__main__':
    caesar()
```

我并不想在写代码的时候反复指定option选项，并在函数名参数栏写一大堆对应参数，麻烦的很。

因此，如果可以在代码中通过Python对象/JSON的形式写参数配置，会不会就让代码看得更加结构化，更清晰呢？

同时，能不能直接将命令行参数当做Python对象进行读写，深拷贝等操作，就如同没有配置过命令行参数一样？

最重要的是，能不能让写代码的速度变的很快，而不需要一行一行的添加一点一点的配置呢？

为了解决以上痛点，因此开发了此工具。

我的目标是让大家用更加简单的写出和繁琐的argparse或click这类命令行解析包一样的效果的代码，同时让配置看起来结构化简洁化，选择json格式是因为Python字典类型dict原生就是json格式，所以可以做到和Python代码格式保持一致，从而使我们可以将配置信息直接嵌入到Python代码文件中（任意位置），而不需要建立类似toml这样单独的配置文件，同时，此库也可以在代码文件的任意位置写配置以读取命令行参数以及随时修改配置各字段值的功能等。

类似的工具还有：

| 名称         | 好处  | 不足                                                                                                                                      |
|----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Fire           | 函数参数直接转换为命令行参数 | 无法将参数传递给其它函数，无法嵌套输入                                                                                                                  |
| hydra          | 读取写入yaml方便 | 需要设定额外的yaml文件且路径强制固定，同时无法进行代码完整性检查以及参数类型检查和强制转换，参数打印不够友好清晰。    |
| ml_collections | 功能类似此工具且可配置项更多 | 传递命令行参数时书写麻烦，嵌套输入需要手动指定类，同样没有代码完整性检查以及参数类型检查和强制转换，参数打印不够友好清晰。                              |

## 待开发

* 高级配置功能以实现更多效果，如更改命令行输入方式（从--到-或+）等，欢迎提出issues。
