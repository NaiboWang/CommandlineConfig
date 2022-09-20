# 请您Star Please Star

如果你觉得此工具不错，请轻轻点击此页面右上角**Star**按钮增加项目曝光度，谢谢！

If you think this tool is good, please gently click the **Star** button in the upper right corner at this page to increase the project exposure, thank you!

# 简洁命令行配置工具 Easy-to-use Commandline Configuration Tool

一个供用户以Python Dict或JSON格式编写（科研中实验）配置的库，同时可以从命令行中读取参数。

A library for users to write (experiment in research) configurations in Python Dict or JSON format, while can read parameters from the command line.

标签 Labels： Python, Command Line, commandline, config, configuration, parameters, 命令行，配置，传参，参数值修改。

Github网址：https://github.com/NaiboWang/CommandlineConfig

Github Address: https://github.com/NaiboWang/CommandlineConfig

##  目录 Catalogue

- [请您Star Please Star](#请您star-please-star)
- [简洁命令行配置工具 Easy-to-use Commandline Configuration Tool](#简洁命令行配置工具-easy-to-use-commandline-configuration-tool)
  - [目录 Catalogue](#目录-catalogue)
  - [使用方式 Usage](#使用方式-usage)
    - [请提出issue Please issue](#请提出issue-please-issue)
    - [安装方法 Installation](#安装方法-installation)
    - [配置方式 Configuration Way](#配置方式-configuration-way)
    - [配置参数读写方式 Configuration parameters read and write method](#配置参数读写方式-configuration-parameters-read-and-write-method)
      - [写入方式 Write method](#写入方式-write-method)
      - [读取方式 Reading method](#读取方式-reading-method)
      - [传递配置给函数 Pass configuration to functions](#传递配置给函数-pass-configuration-to-functions)
      - [拷贝配置 Copy configuration](#拷贝配置-copy-configuration)
  - [注意事项 Things need attention](#注意事项-things-need-attention)
    - [完整转换示例 Full conversion example](#完整转换示例-full-conversion-example)
  - [碎碎念 Shattered thoughts](#碎碎念-shattered-thoughts)
  - [待做事项 TODO](#待做事项-todo)



## 使用方式 Usage

### 请提出issue Please issue

使用过程中遇到任何问题，请在此项目的github页面中提出issue，我将在第一时间解决遇到的bug和问题。

If you encounter any problems during using with this tool, please raise an issue in the github page of this project, I will solve the bugs and problems encountered at the first time.

### 安装方法 Installation

两种方法安装此库：

There are two ways to install this library:

* 1. 通过pip安装：
  
* 1. Install via pip:
  ```shell
    pip install commandline_config
  ```

* 2. 直接导入github项目中/commandline_config文件夹下的commandline_config.py文件到自己的项目目录中即可，需要安装依赖包prettytable:
* 2. Import the commandline_config.py file directly from the /commandline_config folder of the github project into your own project directory, you need to install the dependency package prettytable:

    ```shell
    pip install prettytable
    ```
  
### 配置方式 Configuration Way

* 0. 导入包：
* 0. Import library:

    ```python
    from commandline_config import Config
    ```

* 1. 以JSON/Python Dict形式设定参数名称和初始值，并通过#注释方式添加参数描述。目前支持嵌套一层dict。
* 1. Set the parameter name and initial value in JSON/Python Dict format, and add the parameter description by # comment. Currently supports nesting a dict inside, but only one layer.

    ```python
      preset_config = {
        "index": 1, # Index of party
        "dataset": "mnist",
        'lr': 0.01, # learning rate 
        'normalization': True,
        "multi_information":[1,0.5,'test',"TEST"], # list
        "dbinfo":{
          "username":"nus",
          "password":123456,
          "retry_interval_time":5.5,
          "save_password":False,
          "certificate_info":["1",2,[3.5]] 
        }
      }
    ```
  
  即生成了程序的初始配置，在preset_config dict中定义的每一个key为参数名称，每一个value为参数的初始值，同时，参数的初始值类型会根据设置的值的类型自动检测。

  That is, the initial configuration of the program is generated. Each key defined in preset_config dict is the parameter name and each value is the initial value of the parameter, and at the same time, the initial value type of the parameter is automatically detected according to the type of the set value.

  如上方配置中包含六个参数：index， dataset， batch， normalization, multi_information和dbinfo， 其中参数**index**的类型会自动检测为**int**，默认值为**1**，描述为“Index of party”。

  The above configuration contains six parameters: *index, dataset, batch, normalization, multi_information* and *dbinfo*, where the type of the parameter **index** is automatically detected as **int**, the default value is **1** and the description is "Index of party".


  同理，第二至五个参数的的类型和默认值分别为string:"mnist"； float:0.01； bool:True； list:[1,0.5,'test',"TEST"]。

  Similarly, The type and default value of the second to fifth parameter are string: "mnist"; float:0.01; bool:True; list:[1,0.5,'test', "TEST"].

  第六个参数是一个嵌套的字典，类型为dict，里面同样包含五个参数，类型和默认值和第一至五个参数同理，此处不再赘述。

  The sixth parameter is a nested dictionary of type dict, which also contains five parameters, with the same type and default values as the first five parameters, and will not be repeated here.

* 2. 在任意函数中通过preset_config dict创建配置类对象。
* 2. Create a configuration class object by preset_config dict in any function you want.

    ```python
    if __name__ == '__main__':
        config = Config(preset_config)
        # 或者给配置设定名称：
        # Or give the configuration a name:
        config_with_name = Config(preset_config, name="Federated Learning Experiments")
    ```

  即成功生成配置对象。

  This means that the configuration object is successfully generated.

* 3. 可通过print直接打印参数配置：
* 3. Configuration of parameters can be printed directly via print function:

  ```python
    print(config_with_name)
  ```

  输出结果为：

  The output results are:
  
  ```
    Configurations of Federated Learning Experiments:
  +-------------------+-------+--------------------------+
  |        Key        |  Type | Value                    |
  +-------------------+-------+--------------------------+
  |       index       |  int  | 1                        |
  |      dataset      |  str  | mnist                    |
  |         lr        | float | 0.01                     |
  |   normalization   |  bool | True                     |
  | multi_information |  list | [1, 0.5, 'test', 'TEST'] |
  |       dbinfo      |  dict | See sub table below      |
  +-------------------+-------+--------------------------+
  {'index': 1, 'dataset': 'mnist', 'lr': 0.01, 'normalization': True, 'multi_information': [1, 0.5, 'test', 'TEST'], 'dbinfo': 'See below'}

  Configurations of dict dbinfo:
  +---------------------+-------+-----------------+
  |         Key         |  Type | Value           |
  +---------------------+-------+-----------------+
  |       username      |  str  | nus             |
  |       password      |  int  | 123456          |
  | retry_interval_time | float | 5.5             |
  |    save_password    |  bool | False           |
  |   certificate_info  |  list | ['1', 2, [3.5]] |
  +---------------------+-------+-----------------+
  {'username': 'nus', 'password': 123456, 'retry_interval_time': 5.5, 'save_password': False, 'certificate_info': ['1', 2, [3.5]]}
  ```

  这里会同时以表格和字典形式打印所有参数的信息，如想要改变打印方式，可通过`config_with_name.set_print_style(style='')`的方式修改，style可取的值有：`both`，`table`，`json`分别表示同时打印，只打印表格，只打印json字典。

  Here the information of all parameters will be printed in table and dictionary format at the same time. If you want to change the printing style, you can modify it by `config_with_name.set_print_style(style='')`. The values that can be taken for *style* are: `both`, `table`, `json` which means print both table and json at the same time, print only table, and json dictionary only.

  如：
  
  E.g.:

  ```python
    # 只打印json
    # Only print json 
    config_with_name.set_print_style('json')
    print(config_with_name)
    print("----------")
    # 只打印表格
    # Only print table
    config_with_name.set_print_style('table')
    print(config_with_name)
  ```

  输出结果为：

  The output results are:

  ```
  Configurations of Federated Learning Experiments:
  {'index': 1, 'dataset': 'mnist', 'lr': 0.01, 'normalization': True, 'multi_information': [1, 0.5, 'test', 'TEST'], 'dbinfo': 'See below'}

  Configurations of dict dbinfo:
  {'username': 'nus', 'password': 123456, 'retry_interval_time': 5.5, 'save_password': False, 'certificate_info': ['1', 2, [3.5]]}


  ----------

  Configurations of Federated Learning Experiments:
  +-------------------+-------+--------------------------+
  |        Key        |  Type | Value                    |
  +-------------------+-------+--------------------------+
  |       index       |  int  | 1                        |
  |      dataset      |  str  | mnist                    |
  |         lr        | float | 0.01                     |
  |   normalization   |  bool | True                     |
  | multi_information |  list | [1, 0.5, 'test', 'TEST'] |
  |       dbinfo      |  dict | See sub table below      |
  +-------------------+-------+--------------------------+

  Configurations of dict dbinfo:
  +---------------------+-------+-----------------+
  |         Key         |  Type | Value           |
  +---------------------+-------+-----------------+
  |       username      |  str  | nus             |
  |       password      |  int  | 123456          |
  | retry_interval_time | float | 5.5             |
  |    save_password    |  bool | False           |
  |   certificate_info  |  list | ['1', 2, [3.5]] |
  +---------------------+-------+-----------------+
  ```


### 配置参数读写方式 Configuration parameters read and write method

#### 写入方式 Write method

可通过三种方式写入配置参数值。

Configuration parameter values can be written in three ways.

* 1. 接收命令行参数，只需要在命令行通过--index 1传递即可修改index的值为1，同时，不同类型的参数传递的注意事项为：
* 1. To receive command line arguments, simply pass --index 1 on the command line to modify the value of *index* to 1. Also, the considerations for passing values to different types of arguments are：
  
  * 传递bool类型时，可使用0或False来表示False，使用1或True或参数后面不带任何值来表示True：即--normalization 1或--normalization True或--normalization都可以将配置中normalization的参数值设定为True.
  * When passing bool type, you can use *0* or *False* for **False**, *1* or *True* or *no value after the parameter* for **True**: --normalization 1 or --normalization True or --normalization all can set the value of parameter *normalization* in the configuration to **True**.
  * 传递list类型时，可传递空数组及多维数组。
  * When passing list type, empty array and multi-dimensional arrays can be passed.
  * 修改嵌套对象中的值，请使用"--嵌套参数名.子参数名 值"的方式修改嵌套对象中的值，如--dbinfo.password 987654即可将dbinfo子对象内的password参数值改为987654。注意，不可直接操作dbinfo本身，如--dbinfo {'password':987654}的写法是错误的。目前此工具只支持一层嵌套。
  * To modify the value in the nested dict, please use "--nested-parameter-name.sub-parameter-name value" to modify the value in the nested object, such as --dbinfo.password 987654 to change the value of the *password* parameter in the *dbinfo* subobject to *987654*. Currently this tool only supports one level of nesting.
  * 注意，**参数index必须在上面定义的preset_config对象中：**
  * Note that **the argument index must be in the preset_config object defined above:**
  
  ```python
    python test.py --index 0 --dataset emnist --normalization 0 --multi_information [\'sdf\',1,\"3.3\",,True,[1,[]]] --dbinfo.password 987654
  ```

* 2. 直接在代码中使用`config.index = 2`来修改参数index的值为2，同样，list类型参数可以赋值为为空或多维数组。对于嵌套对象，可使用`config.dbinfo.save_password=True`的方式修改dbinfo中save_password参数的值为True。
* 2. Use `config.index = 2` directly in the code to change the value of the parameter index to 2. Again, list type parameters can be assigned as empty or multidimensional arrays. For nested objects, you can use `config.dbinfo.save_password=True` to modify the value of the save_password parameter in dbinfo to `True`.

* 3. 1和2两种方式会触发类型检查，即如果赋的值类型和预定义字典preset_config中默认值的类型不匹配时程序将报错，因此，如果不想进行强制类型检查，可通过`config["index"] = "sdf"`强行修改参数index的值为字符串sdf（不推荐，会造成意想不到的影响）。
* 3. Way 1 and 2 will trigger type checking, that is, if the type of the assigned value and the type of the default value in the predefined dict *preset_config* does not match, the program will report an error, therefore, if you do not want to force type checking, you can use `config["index"] = "sdf"` to force the value of the parameter index to the string *sdf* (not recommended, it will cause unexpected impact).

#### 读取方式 Reading method

直接通过config.dataset或者config["dataset"]的方式读取参数dataset的值：

Read the value of the parameter *dataset* directly by means of config.dataset or config["dataset"].

```python
print(config.dataset, config["index"])
```

一个参数a的值将被读取为：最后通过config.a = * 修改的值 > 通过命令行指定的--a 2的值 > 通过preset_config定义的"a":1指定的初始值。

The value of an argument *a* will be read by this order: the last value modified by config.a = * > the value of --a 2 specified by the command line > the initial value specified by "a":1 defined by preset_config.

对于list类型如果传递了多维数组，直接像正常使用数组一样读取信息即可：

For the list type, if a multidimensional array is passed, the information can be read via standard slice of python:

```python
config.dbinfo.certificate_info = [1,[],[[2]]]
print(config.dbinfo.certificate_info[2][0][0])
```

对于嵌套对象中的参数，共有四种读取方式，均可读取到参数的值：

For parameters in nested objects, there are four ways to read the values of the parameters, all of which can be read successfully:

```
print(config.dbinfo.username)
print(config["dbinfo"].password)
print(config.dbinfo["retry_interval_time"])
print(config["dbinfo"]["save_password"])
```

#### 传递配置给函数 Pass configuration to functions

直接将上面的config对象作为参数传递给函数并调用即可：

Simply pass the above config object as a parameter to the function and call it:

```python
def print_dataset_name(c):
  print(c.dataset, c["dataset"], c.dbinfo.certificate_info)

print_dataset_name(c=config)
```

#### 拷贝配置 Copy configuration

通过deepcopy方法对配置对象进行深拷贝即可：

A deep copy of the configuration object can be made by the *deepcopy* method:

```python
from copy import deepcopy
copy_config = deepcopy(config)
# 修改新复制的配置参数值，不会影响原配置
# Modify new configuration's parameter value, will not affect the orignal configuration
copy_config.index=15 
```

## 注意事项 Things need attention

* 此包无法和argparse包同时读取命令行参数，因此使用此包请不要同时使用args = parser.parse_args()来读取命令行参数。
* This library cannot read command line arguments at the same time with the argparse library, so please do not use args = parser.parse_args() to read command line arguments while using this library.

* 参数的类型将自动检测为preset_config中设定的初始值类型，同时命令行参数的值将被强制转换为对应类型值，如上面的preset_config中的index的默认值为1，则参数index的类型为int，初始值为1，此时如在命令行中指定--index 15.5则将会自动将参数index赋值为15，即自动将15.5强制转换为int类型。
* The type of the parameter will be automatically detected as the same type of the initial value set in preset_config, and the value of the command line parameter will be forced converted to the corresponding type value, such as the default value of index in the above preset_config dict is 1, then the type of the parameter index is **int** with the initial value of 1. If you specify --index 15.5 on the command line, the parameter index will be automatically assigned to value 15, that is, 15.5 will be automatically forced converted to int type.

  无法转换的命令行参数将会报错，如命令行指定--index sdf，由于sdf字符串无法强制转换为int类型，因此会报错。

  If the parameter value specified on the command line parameters can not be forcedly converted to specific type, it will report an error, such as if the command line specified --index sdf, as sdf with orignal format of string can not be converted to int type, so it will report an error.

* 命令行参数设置为输入list类型时，如果list中元素是字符串，则必须在每个单/双引号前加入反斜线\以正确解析，否则参数值会被视作int或float类型。如果命令行中有空格会被自动合并（但命令行环境不能是zsh，如果是zsh环境则必须去除list内部所有的空格，bash和sh不存在此问题，即在zsh环境下，`--a [15,\\'12\\']`的15和\\'12\\'之间不得有空格）。
* When the command line argument is set to the input list type, if the element in the list is a string, you must use add a backslash \ before each single/double quote to parse it correctly, otherwise the argument value will be treated as an int or float type. If there are spaces in the command line they will be merged automatically (but the command line environment can not be *zsh*, if it is zsh environment then must remove all the spaces inside the list, *bash* and *sh* does not have this problem, that is, in the zsh environment, you cannot add any space(s) between 15 and \\\'12\\\' in `--a [15,\\'12\\']`).

  如参数可设置为： 

  If the parameters can be set as follows:

  ```
  python test.py --array [1,2.3,\'sdf\'] 
  ```

  即可正确解析array参数，其值为一个list，内容为[1,2.3,'sdf'],即一个包含int, float, string类型的list。

  That can correctly resolve the array parameter whose value is a list, and the content of [1,2.3,'sdf', "qwe"], that is, a list containing int, float, string type of data simultaneously.

* 参数名称中如包含特殊字符如-+空格等python保留字符，则必须使用中括号的方式读写参数值，不能使用.号，如参数名称为*multi-information*，则只能通过config["multi-information"]的方式访问，不能通过config.multi-information访问，因为减号为python语言保留名称。
* If the parameter name contains special characters such as -+ or space or other python reserved characters, you must use the middle bracket to read and write the parameter value instead of **.** E.g., if the parameter name is *multi-information*, it can only be accessed by *config["multi-information"]*, cannot do *config.multi-information*, because the minus sign - is a python language's reserved symbol.

* 目前暂只支持一层嵌套对象，其他支持的参数类型为：int, float, string, bool和list。
* Only one layer of nested objects is supported for now, other supported parameter types are: int, float, string, bool and list.

* 命令行中传递的参数名称**必须提前在preset_config中定义，否则会报错**，如：
* The name of the parameter passed on the command line **must be defined in preset_config in advance, otherwise an error will be reported**, e.g.

  ```python
      python test.py --arg1 1
  ```

  由于参数名arg1没有在preset_config中定义，因此会报错，提示arg1参数未定义，设置此功能是为了进行参数完整性检查，从而避免通过命令行输入错误参数名。

  Since the parameter name *arg1* is not defined in preset_config dict, an error is reported indicating that the arg1 parameter is not defined. This function is set to perform parameter integrity checking to avoid entering incorrect parameter names through the command line.

* 在ZSH Shell环境下传递list参数时，如果出现`zsh: no matches found`的错误，则需要在`~/.zshrc`文件的最后加入一行`setopt no_nomatch`，保存后在命令行运行`source ~/.zshrc`刷新zsh即可。
* If `zsh: no matches found` occurs when passing list arguments in the ZSH Shell environment, please add a line `setopt no_nomatch` at the end of the `~/.zshrc` file, after save it then run `source ~/.zshrc` on the command line to refresh ZSH, then the problem will be solved.


### 完整转换示例 Full conversion example

下面将给出一个例子来证明此工具相比于argparse工具的便利性：

An example will be given below to demonstrate the convenience of this tool compared to the *argparse* tool:

使用argparse工具需要写的代码：

The code that needs to be written using the *argparse* tool:

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

Code to be written after conversion with this tool:

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

As we can see, the amount of code has been reduced and is more structured and neat.

另外一个Click的例子：

Another case with library click:

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

Can be converted to the following code:

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

## 碎碎念 Shattered thoughts

以下描述了作者个人的开发原因以及此包的好处/便利性。

The following describes the author's personal reasons for developing and the benefits/conveniences of this package.

对于经常跑科研实验的朋友们，大家是不是经常需要在python文件开头设置大量的命令行参数，并在下方代码中以args.*的方式调用：

For us who often run research experiments, do you often need to set a lot of command line arguments at the beginning of a python file and call them in the following code as args.*：

比如下面的这段示例：

For example, the following example paragraph:

```python
parser = argparse.ArgumentParser(description='index')
parser.add_argument('--index', default=0, type=int, help='party index')
parser.add_argument('--party_num', default=100, type=int)
args = parser.parse_args()

print(args.index)
```

每多一个参数，代码中就会多一行parser.add_argument，手写每个参数的配置时会很繁琐，如名称需要加--，还有修改默认值，类型以及描述的时候很麻烦，最后也会导致自己的代码很冗长，维护不便。

With one more additional parameter, we need to write one line of parser.add_argument(...), when handwriting configuration of each parameter, it will be very tedious such as the name needs to add --, and modify the default value, type and description of the time is very troublesome, finally will lead to very long code and inconvenient to maintain. 

就算用了更高级一点的Click，也需要不停的写option, 而且有几个option对应函数就要写几个输入参数与之匹配，写代码实在是繁琐，比如以下Click代码：

Even if you use a more advanced library *click*, you still need to write option constantly, and you need to write the same amount of parameters at the input parameter field of the function to match all the option, writing code is really tedious, such as the following Click code:

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

I don't want to specify option over and over again when writing code, and write a lot of corresponding parameters in the function name parameter field, which is very troublesome.

因此，如果可以在代码中通过Python对象/JSON的形式写参数配置，会不会就让代码看得更加结构化，更清晰呢？

So would it make the code look more structured and clearer if the parameter configuration could be written in the format of Python objects/JSON?

同时，能不能直接将命令行参数当做Python对象进行读写，深拷贝等操作，就如同没有配置过命令行参数一样？

Also, is it possible to directly read and write command line arguments as if they were Python objects, or deep copy them, as if no command line arguments had been configured?

最重要的是，能不能让写代码的速度变的很快，而不需要一行一行的添加一点一点的配置呢？

Most importantly, can we make the process of writing code faster, instead of adding a little bit of configuration line by line?

为了解决以上痛点，因此开发了此工具。

In order to solve the above pain points, this tool has been developed.

我的目标是让大家用更加简单的写出和繁琐的argparse或click这类命令行解析包一样的效果的代码，同时让配置看起来结构化简洁化，选择json格式是因为Python字典类型dict原生就是json格式，所以可以做到和Python代码格式保持一致，从而使我们可以将配置信息直接嵌入到Python代码文件中（任意位置），而不需要建立类似toml这样单独的配置文件，同时，此库也可以在代码文件的任意位置写配置以读取命令行参数以及随时修改配置各字段值的功能等。

My goal is to make it easier for us to write more concise codes that works as the same as verbose command line parsing packages like Argparse or Click, while also making the configuration look structured and easy to maintain. Json was chosen because the Python dictionary type Dict is native in JSON format, so can make the same format as Python code. In this way, the configuration information can be directly embedded in the Python code file (anywhere), without the need to establish a separate configuration file such as TOML. At the same time, you can use the library to write the configuration at any position within the code file to read the command line parameters and modify the value of each field at any time.

类似的工具还有：

Similar tools including:

| 名称         | 好处  | 不足                                                                                                                                      |
|----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Fire           | 函数参数直接转换为命令行参数 | 无法将参数传递给其它函数，无法嵌套输入                                                                                                                  |
| hydra          | 读取写入yaml方便 | 需要设定额外的yaml文件且路径强制固定，同时无法进行代码完整性检查以及参数类型检查和强制转换，参数打印不够友好清晰。    |
| ml_collections | 功能类似此工具且可配置项更多 | 传递命令行参数时书写麻烦，同样没有代码完整性检查以及参数类型检查和强制转换，参数打印不够友好清晰。                              |

| Name           | Advantage| Disadvantage                                                                                                                              |
|----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Fire           | Can direct do conversion of function parameters to command line parameters | Cannot pass parameters to other functions.                                                                                                |
| hydra          | Easy to read and write to yaml | Need additional yaml file with specifed path, also cannot perform integrity check and type conversion/check, not friendly for printing    |
| ml_collections | Similar functionality to this tool with more configurable items | A little tideous to pass commandline parameters, and also without integrity check, not friendly for printing                              |

## 待做事项 TODO

* 实现多层循环嵌套功能。
* Implement multi-layer loop nesting function.
