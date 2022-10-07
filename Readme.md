# 请您Star Please Star

如果你觉得此工具不错，请轻轻点击此页面右上角**Star**按钮增加项目曝光度，谢谢！

If you think this tool is good, please gently click the **Star** button in the upper right corner at this page to increase the project exposure, thank you!

# 中文文档

[点此查看中文文档](https://github.com/NaiboWang/CommandlineConfig/blob/master/Readme_CN.md)

# Easy-to-use Commandline Configuration Tool

A library for users to write (experiment in research) configurations in Python Dict or JSON format, read and write parameter value via `dot .` in code, while can read parameters from the command line to modify values.

标签 Labels： Python, Command Line, commandline, config, configuration, parameters, 命令行，配置，传参，参数值修改。

Github URL: <https://github.com/NaiboWang/CommandlineConfig>

## New Features

### v2.2.*
* Support infinite level nesting of parameters in dictionary
* Automatic version checking
* Support parameter value constrained to specified value (enumeration)
* Support for tuple type
* Support reading configuration from local JSON file
* Support for setting parameter help and printing parameter descriptions via command line `-h`
* Documentation updates, provide simple example

## Simple Example

```python
# Install via pip
pip3 install commandline_config

# import package
from commandline_config import Config

# Define configuration dictionary
config = {
  "index":1,
  "lr": 0.1,
  "dbinfo":{
    "username": "NUS"
  }
}

# Generate configuration class based on configuration dict
c = Config(config)

# Print the configuration of the parameters
print(c)

# Read and write parameters directly via dot . and support multiple layers.
c.index = 2
c.dbinfo.username = "ZJU"
print(c.index, c.dbinfo.username, c["lr"])

# On the command line, modify the parameter values with --
python example.py --index 3 --dbinfo.username XDU

# Get the parameter descriptions via the help method in the code, or on the command line via -h or -help (customization required, see detailed documentation below for details)
c.help()

python example.py -h
```

## Catalogue
- [请您Star Please Star](#请您star-please-star)
- [中文文档](#中文文档)
- [Easy-to-use Commandline Configuration Tool](#easy-to-use-commandline-configuration-tool)
  - [New Features](#new-features)
    - [v2.2.*](#v22)
  - [Simple Example](#simple-example)
  - [Catalogue](#catalogue)
  - [Usage](#usage)
    - [Please submit issue](#please-submit-issue)
    - [Installation](#installation)
    - [Configuration Way](#configuration-way)
    - [Configuration parameters read and write method](#configuration-parameters-read-and-write-method)
      - [Write method](#write-method)
      - [Reading method](#reading-method)
      - [Pass configuration to functions](#pass-configuration-to-functions)
      - [Copy configuration](#copy-configuration)
      - [Store configuration parameters to local file or database](#store-configuration-parameters-to-local-file-or-database)
  - [Advanced options](#advanced-options)
    - [Restrict parameter input values to fixed enum types](#restrict-parameter-input-values-to-fixed-enum-types)
    - [Print parameter help descriptions](#print-parameter-help-descriptions)
      - [Set parameter descriptions](#set-parameter-descriptions)
      - [Print parameter help](#print-parameter-help)
  - [Things need attention](#things-need-attention)
    - [Conflict with Argparse](#conflict-with-argparse)
    - [Input value forced conversion](#input-value-forced-conversion)
    - [The list parameter needs to be assigned with a backslash before the string element quotes when passing by commandline](#the-list-parameter-needs-to-be-assigned-with-a-backslash-before-the-string-element-quotes-when-passing-by-commandline)
    - [Quotes are required for command-line assignment of tuple parameters, and string elements must be preceded by a backslash](#quotes-are-required-for-command-line-assignment-of-tuple-parameters-and-string-elements-must-be-preceded-by-a-backslash)
    - [Parameter naming convention](#parameter-naming-convention)
    - [Unlimited layer of nested objects](#unlimited-layer-of-nested-objects)
    - [Parameter integrity check, all parameters to be modified must be predefined](#parameter-integrity-check-all-parameters-to-be-modified-must-be-predefined)
    - [Special configurations in zsh environment](#special-configurations-in-zsh-environment)
  - [Full conversion example](#full-conversion-example)
  - [Example Running Script](#example-running-script)
  - [Shattered thoughts](#shattered-thoughts)
  - [TODO](#todo)


## Usage

### Please submit issue

If you encounter any problems during using with this tool, please raise an issue in the github page of this project, I will solve the bugs and problems encountered at the first time.

**Meanwhile, welcome to submit issues to propose what functions you want to add to this tool and I will implement them when possible.** 


### Installation

There are two ways to install this library:
  
* 1. Install via pip:
  ```shell
  pip3 install commandline_config
  ```
  
  If already installed, you can upgrade it by the following command:

  ```shell
  pip3 install commandline_config --upgrade
  ```
  
* 2. Import the commandline_config.py file directly from the `/commandline_config` folder of the github project into your own project directory, you need to install the dependency package `prettytable`:

    ```shell
    pip3 install prettytable
    ```

    Or install via `requirements.txt`:
  
    ```shell
    pip3 install -r requirements.txt
    ```
  
### Configuration Way

* 0. Import library:

    ```python
    from commandline_config import Config
    ```

* 1. Set the parameter name and initial value in JSON/Python Dict format, and add the parameter description by `#` comment. Currently supports nesting a dict inside another dict, and **can nest unlimited layers**.

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
  
  That is, the initial configuration of the program is generated. Each key defined in `preset_config` dict is the parameter name and each value is the initial value of the parameter, and at the same time, the initial value type of the parameter is automatically detected according to the type of the set value.

  The above configuration contains seven parameters: `index, dataset, batch, normalization, pair, multi_information and dbinfo`, where the type of the parameter **index** is automatically detected as **int**, the default value is **1** and the description is "Index of party".

  Similarly, The type and default value of the second to fifth parameter are string: `"mnist"; float:0.01; bool:True; tuple:(1,2); list:[1,0.5,'test', "TEST"]`.

  The seventh parameter is a nested dictionary of type dict, which also contains 7 parameters, with the same type and default values as the first 7 parameters, and will not be repeated here.

* 2. Create a configuration class object by passing `preset_config` dict to `Config` in any function you want.

    ```python
    if __name__ == '__main__':
        config = Config(preset_config)
        # Or give the configuration a name:
        config_with_name = Config(preset_config, name="Federated Learning Experiments")

        # Or you can store the preset_config in local file configuration.json and pass the filename to the Config class.
        config_from_file = Config("configuration.json")
    ```

  This means that the configuration object is successfully generated.

* 3. Configuration of parameters can be printed directly via `print` function:

  ```python
  print(config_with_name)
  ```

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

  Here the information of all parameters will be printed in table format. If you want to change the printing style, you can modify it by `config_with_name.set_print_style(style='')`. The values that can be taken for `style` are: `both`, `table`, `json` which means print both table and json at the same time, print only table, and json dictionary only.

  E.g.:

  ```python
  # Only print json 
  config_with_name.set_print_style('json')
  print(config_with_name)
  print("----------")
  # Print table and json at the same time
  config_with_name.set_print_style('table')
  print(config_with_name)
  ```

  The output results are:

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


### Configuration parameters read and write method

#### Write method

Configuration parameter values can be written in three ways.

* 1. To receive command line arguments, simply pass `--index 1` on the command line to modify the value of `index` to `1`. Also, the considerations for passing values to different types of arguments are：
  
  * When passing bool type, you can use `0` or `False` for **False**, `1` or `True` or `no value after the parameter` for **True**: `--normalization 1` or `--normalization True` or `--normalization` all can set the value of parameter `normalization` in the configuration to **True**.
  * When passing list type, empty array and multi-dimensional arrays can be passed.
  * To modify the value in the nested dict, please use `--nested-parameter-name.sub-parameter-name.sub-parameter-name.….sub-parameter-name value` to modify the value in the nested object, such as `--dbinfo.password 987654` to change the value of the `password` parameter in the `dbinfo` subobject to `987654`; `--dbinfo.multi.test 1` to change the value of the `test` parameter in the `multi` dict which is in `dbinfo` subobject to ```. Currently this tool can supports unlimited layers/levels of nesting.
  * Note that **the argument index must be in the `preset_config` object defined above:**
  
  ```python
  python test.py --dbinfo.password 987654 --dbinfo.multi.test 1 --index 0 --dataset emnist --normalization 0 --multi_information [\'sdf\',1,\"3.3\",,True,[1,[]]] 
  ```

* 2. Use `config.index = 2` directly in the code to change the value of the parameter `index` to `2`. Again, list type parameters can be assigned as empty or multidimensional arrays. For nested objects, you can use `config.dbinfo.save_password=True` to modify the value of the `save_password` parameter in sub dict `dbinfo` to `True`.

* 3. Way 1 and 2 will trigger type checking, that is, if the type of the assigned value and the type of the default value in the predefined dict `preset_config` does not match, the program will report an error, therefore, if you do not want to force type checking, you can use `config["index"] = "sdf"` to force the value of the parameter index to the string `sdf` (not recommended, it will cause unexpected impact).

#### Reading method

Read the value of the parameter `dataset` directly by means of `config.dataset` or `config["dataset"]`.

```python
print(config.dataset, config["index"])
```

The value of an argument `a` will be read by this order: the last value modified by `config.a = *` > the value of `--a 2` specified by the command line > the initial value specified by `"a":1` defined by preset_config.

For the list type, if a multidimensional array is passed, the information can be read via standard slice of python:

```python
config.dbinfo.certificate_info = [1,[],[[2]]]
print(config.dbinfo.certificate_info[2][0][0])
```

For parameters in a single nested object, there are four ways to read the values of the parameters, all of which can be read successfully:

```
print(config.dbinfo.username)
print(config["dbinfo"].password)
print(config.dbinfo["retry_interval_time"])
print(config["dbinfo"]["save_password"])
```

#### Pass configuration to functions

Simply pass the above config object as a parameter to the function and call it:

```python
def print_dataset_name(c):
  print(c.dataset, c["dataset"], c.dbinfo.certificate_info)

print_dataset_name(c=config)
```

#### Copy configuration

A deep copy of the configuration object can be made by the `deepcopy` method:

```python
from copy import deepcopy
copy_config = deepcopy(config)
# Modify new configuration's parameter value, will not affect the orignal configuration
copy_config.index=15 
```

#### Store configuration parameters to local file or database

The entire parameter configuration can be stored to a local file or uploaded to a remote server such as mongodb, simply by `config.save()` storing the configuration as a `config name (or config if there is no name).json` file in the directory, or you can specify the file name and path as follows:

```python
config.save("config/test_config.json")
```

Then we successfully save the configuration to the local `configuration.json` file inside the `config` folder. The file content is as follows:

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

To store it into the database such as `mongodb`, you need to get the json sequence first corresponding to the parameters with the `info = config.get_config()` command, and serialize it with the `json` library.

For example, to store the `config_with_name` configuration to `mongodb`:

```python
import pymongo
myclient = pymongo.MongoClient('mongodb://username:example.com:27017/', connect=False)
mydb = myclient['exps']
table = mydb["table"]
# Get the configurations
configuration = config.get_config()
# Insert configuration dict into mongodb table
table.insert_one(configuration)

# Or make configuration as part of a bigger dict
all_info = {
  "exp_time":"20220925",
  "configuration":configuration
}
table.insert_one(all_info)
```

Note that tuples are not supported by JSON, so whether stored locally or in a database, tuple arguments will be converted to lists.

## Advanced options

### Restrict parameter input values to fixed enum types

Set advanced options, such as enumerating Enum types, by passing the `options` parameter of the `Config` argument to the `Config` class.

```python
option={}
config = Config(preset_config, options=option)
```

If you want to limit the value of a parameter to a certain range, you can do so by configuring:

```python
advanced_options = {
    'lr': {
        "enum": [0.001, 15.5, 0.01, 0.1] # restrict the lr value to one of 0.001, 15.5, 0.01, 0.1
    },
    'index': {
        "enum": [1, 2, 3] # Restrict the index value to 1, 2 and 3
    },
    "dbinfo": {
        "username": {
            "enum": ["XDU", "ZJU", "NUS"] # restrict the dbinfo.username field to XDU, ZJU and NUS
        },
        "multi":{
            "test":{
                "enum": [1,0.1, 0.01, 15] # 3 layers nested
            }
        }
    },
}

config = Config(preset_config, options=advanced_options)
```

If enum is set, the following three ways to set a parameter to a value other than the qualified/speficied value will all report an error.

* 1. The initial value of `index` is set to a value other than `1,2,3` in `preset_config`:

  ```python
  preset_config = {
    "index":4,
  }
  ```

* 2. The command line passes unqualified/unspecified values for the `lr` argument

  ```shell
  python example.py --lr 0.02
  ```

* 3. The code changes the value of `dbinfo.username` to a value other than `XDU, ZJU and NUS`.

  ```python
  config.dbinfo.username = "UEST"
  ```

  The output are:

  ```Shell
  AttributeError: Can not set value 4 because the key 'index' has set enum list and you the value 4 is not in the enum list [1, 2, 3]!

  AttributeError: Can not set value 0.02 because the key 'lr' has set enum list and you the value 0.02 is not in the enum list [0.001, 15.5, 0.01, 0.1]!

  AttributeError: Can not set value nus because the key 'username' has set enum list and you the value nus is not in the enum list ['XDU', 'ZJU', 'NUS']!
  ```

### Print parameter help descriptions

#### Set parameter descriptions

Set the parameter description helpers by specifying the `helpers` parameter in the `Config` class.

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

Note that since the `dbinfo` parameter is a `dict`, if you want to set the parameter description for `dbinfo`, you need to set a `dbinfo_help` parameter to write the description in the `helpers` dictionary, i.e. add `_help` after the dict parameter name to set the parameter description for the dict field.

#### Print parameter help

Two ways to print parameter descriptions, by passing `-h` or `-help` on the command line, or by calling the `help()` function in code.

```python
config_with_name.help()
```

or

```shell
python example.py -h
# OR
python example.py -help
```

Note that it is only one short slash `-` and no other command line arguments be added to get help instructions, and the output of both methods is:

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


## Things need attention

### Conflict with Argparse
This library cannot read command line arguments at the same time with the argparse library, so please do not use `args = parser.parse_args()` to read command line arguments while using this library.

### Input value forced conversion
The type of the parameter will be automatically detected as the same type of the initial value set in `preset_config`, and the value of the command line parameter will be forced converted to the corresponding type value, such as the default value of `index` in the above `preset_config` dict is `1`, then the type of the parameter index is `int` with the initial value of `1`. If you specify `--index 15.5` on the command line, the parameter `index` will be automatically assigned to value `15`, that is, `15.5` will be automatically forced converted to `int` type.

If the parameter value specified on the command line parameters can not be forcedly converted to specific type, it will report an error, such as if the command line specified `--index sdf`, as sdf with orignal format of `string` can not be converted to `int` type, so it will report an error.

### The list parameter needs to be assigned with a backslash before the string element quotes when passing by commandline

When the command line argument is set to the input `list` type, if the element in the list is a `string,` you must use add a `backslash \` before each `single/double quote` to parse it correctly, otherwise the argument value will be treated as an `int` or `float` type. If there are `spaces` in the command line they will be merged automatically (but the command line environment can not be `zsh`, if it is zsh environment then must remove all the spaces inside the list, `bash` and `sh` does not have this problem, that is, in the zsh environment, you cannot add any space(s) between `15` and `\'12\'` in `--a [15,\'12\']`).

If the parameters can be set as follows:

  ```
  python test.py --array [1,2.3,\'sdf\'] 
  ```

That can correctly resolve the array parameter whose value is a `list`, and the content of `[1,2.3,'sdf', "qwe"]`, that is, a list containing int, float, string type of data simultaneously.

### Quotes are required for command-line assignment of tuple parameters, and string elements must be preceded by a backslash

When the command line parameter is set to the input `tuple` type, the specified tuple type value must be enclosed in `quotes`; and if the element in the tuple is a `string`, a `backslash` must be added before each single/double quote `\` for proper parsing, otherwise the parameter value will be treated as an `int` or `float` type. Similarly, if there are `spaces` in the command line they will be merged automatically (but the command line environment cannot be `zsh`, if it is zsh environment then all internal spaces must be removed, bash and sh do not have this problem).

For example, the parameter can be set to 

```
python test.py --pair "(1,2,\'msg\')"
```

The value of the pair parameter is a tuple of type `(1,2, "msg")`, i.e. a tuple of type `int`, `float`, `string`.


### Parameter naming convention

If the parameter name contains special characters such as `-+.` or `space` or `other python reserved characters`, you must use the `middle bracket []` to read and write the parameter value instead of **.** E.g., if the parameter name is `multi-information`, it can only be accessed by `config["multi-information"]`, cannot do `config.multi-information`, because the minus `sign -` is a python language's reserved symbol.

### Unlimited layer of nested objects
Now the tool can support unlimited layers of nesting, other supported parameter types are: `int, float, string, bool, tuple and list`.

### Parameter integrity check, all parameters to be modified must be predefined
The name of the parameter passed on the command line **must be defined in `preset_config` in advance, otherwise an error will be reported**, e.g.

  ```python
  python test.py --arg1 1
  ```

Since the parameter name `arg1` is not defined in `preset_config` dict, an error is reported indicating that the `arg1` parameter is not defined. This function is set to perform parameter integrity checking to avoid entering incorrect parameter names through the command line.

### Special configurations in zsh environment
If `zsh: no matches found` occurs when passing list arguments in the zsh Shell environment, please add a line `setopt no_nomatch` at the end of the `~/.zshrc` file, after save it then run `source ~/.zshrc` on the command line to refresh zsh, then the problem will be solved.


## Full conversion example

An example will be given below to demonstrate the convenience of this tool compared to the `argparse` tool.

The code that needs to be written using the `argparse` tool:

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

As we can see, the amount of code has been reduced and is more structured and neat.

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

## Example Running Script

You can run `example.py` in the Github project to test the whole tool, most functions's codes had been provided inside the file:

```
# Get help for all parameters of example.py
python example.py -h
# Specify parameter values
python example.py --dbinfo.multi.test 0.01 --dbinfo.username NUS
```

## Shattered thoughts

The following describes the author's personal reasons for developing and the benefits/conveniences of this package.

For us who often run research experiments, do you often need to set a lot of command line arguments at the beginning of a python file and call them in the following code as `args.*`：

For example, the following example paragraph:

```python
parser = argparse.ArgumentParser(description='index')
parser.add_argument('--index', default=0, type=int, help='party index')
parser.add_argument('--party_num', default=100, type=int)
args = parser.parse_args()

print(args.index)
```

With one more additional parameter, we need to write one line of `parser.add_argument(...)`, when handwriting configuration of each parameter, it will be very tedious such as the name needs to add --, and modify the default value, type and description of the time is very troublesome, finally will lead to very long code and inconvenient to maintain. 

Even if you use a more advanced library `click`, you still need to write option constantly, and you need to write the same amount of parameters at the input parameter field of the function to match all the option, writing code is really tedious, such as the following Click code:

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

I don't want to specify option over and over again when writing code, and write a lot of corresponding parameters in the function name parameter field, which is very troublesome.

So would it make the code look more structured and clearer if the parameter configuration could be written in the format of Python objects/JSON?

Also, is it possible to directly read and write command line arguments as if they were Python objects, or deep copy them, as if no command line arguments had been configured?

Most importantly, can we make the process of writing code faster, instead of adding a little bit of configuration line by line?

In order to solve the above pain points, this tool has been developed.

My goal is to make it easier for us to write more concise codes that works as the same as verbose command line parsing packages like Argparse or Click, while also making the configuration look structured and easy to maintain. Json was chosen because the Python dictionary type Dict is native in JSON format, so can make the same format as Python code. In this way, the configuration information can be directly embedded in the Python code file (anywhere), without the need to establish a separate configuration file such as TOML. At the same time, you can use the library to write the configuration at any position within the code file to read the command line parameters and modify the value of each field at any time.

Similar tools including:

| Name           | Advantage| Disadvantage                                                                                                                              |
|----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Fire           | Can direct do conversion of function parameters to command line parameters | Cannot pass parameters to other functions.                                                                                                |
| hydra          | Easy to read and write to yaml | Need additional yaml file with specifed path, also cannot perform integrity check and type conversion/check, not friendly for printing    |
| ml_collections | Similar functionality to this tool with more configurable items | A little tideous to pass commandline parameters, when nesting need to artificially set specifed Class, and also without integrity check, not friendly for printing                              |

## TODO

**Welcome to submit issues to propose what functions you want to add to this tool and I will implement them when possible.** 

* Advanced options to support more advanced features such as commandline style (instead of use --, can change to - or +), etc.
