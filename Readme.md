# 简洁命令行配置工具 Easy-to-use Commandline Configuration Tool

一个供用户以Python Dict或JSON格式编写（科研中实验）配置的库，同时可以从命令行中读取参数。

A library for users to write (experiment in research) configurations in Python Dict or JSON format, while can read parameters from the command line.

Github网址：https://github.com/NaiboWang/CommandlineConfig

Github Address: https://github.com/NaiboWang/CommandlineConfig

## 使用方式 Usage

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

* 1. 以JSON/Python Dict形式设定参数名称和初始值，并通过#注释方式添加参数描述。
* 1. Set the parameter name and initial value in JSON/Python Dict format, and add the parameter description by # comment.

    ```python
      preset_config = {
        "index": 1, # Index of party
        "dataset": "mnist",
        'lr': 0.01, # learning rate 
        'normalization': True,
        "multi-information":[1,0.5,'test',"TEST"]
      }
    ```
  
  即生成了程序的初始配置，在preset_config dict中定义的每一个key为参数名称，每一个value为参数的初始值，同时，参数的初始值类型会根据设置的值的类型自动检测。

  That is, the initial configuration of the program is generated. Each key defined in preset_config dict is the parameter name and each value is the initial value of the parameter, and at the same time, the initial value type of the parameter is automatically detected according to the type of the set value.

  如上方配置中包含五个参数：index， dataset， batch， normalization和 multi-information， 其中参数**index**的类型会自动检测为**int**，默认值为**1**，描述为“Index of party”。

  The above configuration contains five parameters: index, dataset, batch, normalization and multi-information, where the type of the parameter **index** is automatically detected as **int**, the default value is **1** and the description is "Index of party".


  同理，其余四个参数的的类型和默认值分别为string:"mnist"； float:0.01； bool:True； List:[1,0.5,'test',"TEST"]。

  Similarly, the type and default values of the remaining four parameters are string: "mnist"; float:0.01; bool:True; List:[1,0.5,'test', "TEST"].

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
    +-------------------+--------------------------+
    |        Key        | Value                    |
    +-------------------+--------------------------+
    |       index       | 1                        |
    |      dataset      | mnist                    |
    |         lr        | 0.01                     |
    |   normalization   | True                     |
    | multi-information | [1, 0.5, 'test', 'TEST'] |
    +-------------------+--------------------------+
  ```

### 配置参数读写方式 Configuration parameters read and write method

#### 写入方式 Write method

可通过两种方式写入配置参数值。

Configuration parameter values can be written in two ways.

* 1. 接收命令行参数，只需要在命令行通过--index 1传递即可，注意，**参数index必须在上面定义的preset_config对象中：**
* 1. To receive command line arguments, simply pass them on the command line via --index 1. Note that **the argument index must be in the preset_config object defined above:**
  
  ```python
    python test.py --index 0 --dataset emnist --normalization 0
  ```

* 2. 直接在代码中使用config.index = 2来修改参数index的值为2。
* 2. Use config.index = 2 directly in the code to change the value of the parameter index to 2.

#### 读取方式 Reading method

直接通过config.dataset或者config["dataset"]的方式读取参数dataset的值：

Read the value of the parameter *dataset* directly by means of config.dataset or config["dataset"].

```python
print(config.dataset, config["index"])
```

一个参数a的值将被读取为：最后通过config.a = * 修改的值 > 通过命令行指定的--a 2的值 > 通过preset_config定义的"a":1指定的初始值。

The value of an argument *a* will be read by this order: the last value modified by config.a = * > the value of --a 2 specified by the command line > the initial value specified by "a":1 defined by preset_config.

#### 传递配置给函数 Pass configuration to functions

直接将上面的config对象作为参数传递给函数并调用即可：

Simply pass the above config object as a parameter to the function and call it:

```python
def print_dataset_name(c):
  print(c.dataset, c["dataset"])

print_dataset_name(c=config)
```

#### 拷贝配置 Copy configuration

通过deepcopy方法对配置对象进行深拷贝即可：

A deep copy of the configuration object can be made by the *deepcopy* method:

```python
from copy import deepcopy
copy_config = deepcopy(config)
copy_config.index=15 # Modify new configuration's parameter value
```

## 注意事项 Matters needs caution

* 此包无法和argparse包同时读取命令行参数，因此使用此包请不要同时使用args = parser.parse_args()来读取命令行参数。
* This library cannot read command line arguments at the same time as the argparse library, so please do not use args = parser.parse_args() to read command line arguments while using this library.

* 参数的类型将自动检测为preset_config中设定的初始值类型，同时命令行参数的值将被强制转换为对应类型值，如上面的preset_config中的index的默认值为1，则参数index的类型为int，初始值为1，此时如在命令行中指定--index 15.5则将会自动将参数index赋值为15，即自动将15.5强制转换为int类型。
* The type of the parameter will be automatically detected as the same type of the initial value set in preset_config, and the value of the command line parameter will be forced converted to the corresponding type value, such as the default value of index in the above preset_config dict is 1, then the type of the parameter index is **int** with the initial value of 1. If you specify --index 15.5 on the command line, the parameter index will be automatically assigned to value 15, that is, 15.5 will be automatically forced converted to int type.

无法转换的命令行参数将会报错，如命令行指定--index sdf，由于sdf无法转换为int类型，因此会报错。

If the parameter value specified on the command line parameters can not be forced converted to specific type, it will report an error, such as if the command line specified --index sdf, as sdf can not be converted to int type, so it will report an error.

* 命令行配置为输入Bool类型时，需使用0和1来表示False和True： --normalization 0即将配置中normalization的参数值设定为False。
* When the command line is configured as input Bool type, you need to use 0 and 1 to indicate False and True: --normalization 0 is to set the parameter value of normalization in the configuration to False.

* 命令行参数设置为输入List类型时，如果list中元素是字符串，需要在每个单引号或双引号前加入反斜线\以正确解析，否则参数值会被视作int或float类型。如果命令行中有空格会被自动合并。
* When the command line argument is set to the input List type, if the element in the list is a string, you need to add a backslash \ before each single or double quote to parse it correctly, otherwise the argument value will be treated as an int or float type. If there are spaces in the command line they will be merged automatically.

如参数可设置为： 

If the parameters can be set as follows:

```
python test.py --array [1,2.3,\'sdf\',\"qwe\"] 
```

即可正确解析array参数，其值为一个List，内容为[1,2.3,'sdf',"qwe"],即一个包含int, float, string类型的List。

That can correctly resolve the array parameter whose value is a List, and the content of [1,2.3,'sdf', "qwe"], that is, a List containing int, float, string type of data simultaneously.

* 暂不支持嵌套对象，目前支持的参数类型为：int, float, string, bool和List。
* Nested objects are not supported at the moment. The currently supported parameter types are: int, float, string, bool and List.

* 命令行中传递的参数名称**必须提前在preset_config中定义，否则会报错**，如：
* The name of the parameter passed on the command line ** must be defined in preset_config in advance, otherwise an error will be reported **, e.g.

```python
    python test.py --arg1 1
```

由于参数名arg1没有在preset_config中定义，因此会报错，提示arg1参数未定义，设置此功能是为了进行参数完整性检查。

Since the parameter name *arg1* is not defined in preset_config dict, an error is reported indicating that the arg1 parameter is not defined. This function is set to perform parameter integrity checking.

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

## Shattered thoughts 碎碎念

以下描述了作者个人的开发原因以及此包的好处/便利性。

The following describes the author's personal reasons for developing and the benefits/conveniences of this package.

对于经常跑科研实验的朋友们，你们是不是经常需要在python文件开头设置大量的命令行参数，并在下方代码中以args.*的方式调用：

For those of you who often run research experiments, do you often need to set a lot of command line arguments at the beginning of a python file and call them in the following code as args.*：

比如下面的这段示例：

For example, the following example paragraph:

```python
parser = argparse.ArgumentParser(description='index')
parser.add_argument('--index', default=0, type=int, help='party index')
parser.add_argument('--party_num', default=100, type=int)
args = parser.parse_args()

print(args.index)
```

每多一个参数，代码中就会多一行parser.add_argument，手写每个参数的配置时，如名称需要加--，还有修改默认值，类型以及描述的时候很麻烦，最后也会导致自己的代码很冗长，维护不便。

With one more additional parameter, we need to write one line of parser.add_argument(...), when handwriting configuration of each parameter, it will be very tedious such as the name needs to add --, and modify the default value, type and description of the time is very troublesome, finally will lead to very long code and inconvenient to maintain. 

因此，如果可以在代码中通过Python对象/JSON的形式写参数配置，会不会就让代码看得更加结构化，更清晰呢？

So would it make the code look more structured and clearer if the parameter configuration could be written in the format of Python objects/JSON?

同时，能不能直接将命令行参数当做Python 对象进行读写，深拷贝等操作，就如同没有配置过命令行参数一样？

Also, is it possible to directly read and write command line arguments as if they were Python objects, or deep copy them, as if no command line arguments had been configured?

最重要的是，能不能让写代码的速度变的很快，而不需要一行一行的添加一点一点的配置呢？

Most importantly, can you make the process of writing code faster, instead of adding a little bit of configuration line by line?

为了解决以上痛点，因此开发了此工具。

In order to solve the above pain points, this tool has been developed.

