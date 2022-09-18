import sys
from prettytable import PrettyTable

def check_type(v):
    if isinstance(v, bool):
        return "bool"
    elif isinstance(v, int):
        return "int"
    elif isinstance(v, float):
        return "float"
    elif isinstance(v, list):
        return "list"
    elif isinstance(v, tuple):
        return "tuple"
    elif isinstance(v, dict):
        return "dict"
    else:
        return "str"


# 配置类
class Config(dict):
    """
    Makes a dictionary behave like an object,with attribute-style access.
    配置方式：
    preset_config = {"a":1, # parameter a
    "b":"test",
    "c":[1,"2"]
    }
    config = Config(preset_config)
    在preset_config中定义的每一个key为参数名称，每一个value为参数的初始值，同时，参数的初始值类型会根据设置的值的类型自动检测，如上面preset_config的参数a的类型为int，默认值为1；参数b的类型为string，默认值为test；参数c的默认值为数组List，默认值为[1,"2"]。
    对于参数的注释，可以直接在参数后通过Python注释的方式写。
    命令行参数读写方式：
    写入方式：
    1. 接收命令行参数，只需要在命令行通过--a 1传递即可，参数a必须在上面定义的preset_config中
    2. 使用config.a = 2来修改参数值

    读取方式：
    直接通过config.a或者config["a"]的方式读取参数a的值
    参数a的值读取顺序为：最后通过config.a = * 修改的值 > 通过命令行指定的--a 2的值 > 通过preset_config定义的"a":1指定的初始值。

    """

    def __init__(self, preset_config, name=""):
        self.preset_config = preset_config
        for c in self.preset_config:
            if c == "preset_config": # Prevent Loop 防止套娃
                continue
            self[c] = self.preset_config[c]
        self.config_name = name
        self.set_command_line(sys.argv[1:])

    # 命令行一个--参数后面只能跟一个参数值，如果有多个，则用[] List形式表示
    # 用0和1代表True和False
    # 如 --dataset cifar100 --split [\"train[:40000]\",\"train[40000:]\", \"test\"] 如果有空格会被自动合并
    # 命令行中有引号需要加转义符\
    def set_command_line(self, lines):
        for i in range(len(lines)):
            if lines[i].find("--") >= 0:  # 如果是配置项
                key = lines[i].replace("--", "")
                value = []
                for j in range(i + 1, len(lines)):
                    if lines[j].find("--") >= 0:
                        break
                    value.append(lines[j])
                value = " ".join(value)
                # print("origin key-value:", key, value, check_type(value))
                v = self.convert_type(value, key)
                self[key] = v
                # print("after convert key-value:", key, v, check_type(v))

    # 把变量v按照preset_config里的相应key对应的值的类型转换为相应类型，用于命令行参数类型转换，同时保证了所有参数必须在preset_config中出现
    # 如preset_config里的random_seed为2022,是一个int类型，则命令行参数如果指定了--random_seed 2013,则会把2013由原始的字符串形式转换为int
    def convert_type(self, v, key):
        try:
            type = check_type(self.preset_config[key])
            # print("type is", type)
            if type == "str":
                variable = v
            elif type == "float" or type == "int" or type == "bool":  # 如果是int或者float，转换为相应类型
                variable = eval(type + "(" + v + ")")
            else:
                variable = eval("eval('%s')" % v)
        except:
            raise AttributeError("Cannot convert %s to type %s" % (str(v), type))
        # print(variable, check_type(variable))
        # if type == "list" or type == "dict" or type == "tuple":
        #     variable = eval("eval(%s)"%v)
        # else:
        #     variable = eval(type + "('" + v + "')")
        # print(check_type(variable))
        return variable

    def __str__(self):
        if self.config_name == "":
            print("Configurations:")
        else:
            print("Configurations of %s: " % self.config_name)
        output = PrettyTable(["Key", "Value"])
        output.align["Value"] = 'l'
        for key in self.preset_config:
            # output += key + ":" + str(self[key]) + "\n"
            output.add_row([key, str(self[key])])
        print(output)
        return ""

    def get_config(self):
        output = {}
        for key in self.preset_config:
            if key == "_id": # 防止mongodb的ObjectID键冲突
                continue
            output[key] = self[key]
        return output

    def __getattr__(self, name):
        try:
            return self[name]
        except:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == "preset_config" or name == "config_name" or name in self.preset_config:
            self[name] = value  # 暂时没有对通过value进行类型检查，以后可以做
        else:
            raise AttributeError("Can not set value because the key '%s' is not in preset_config!" % name)
