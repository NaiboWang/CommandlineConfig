from copy import deepcopy
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

    def __init__(self, preset_config, name="", read_command_line = True):
        self.__setattr__("preset_config",preset_config,True)
        # self.preset_config = preset_config
        for c in self.preset_config:
            if c == "preset_config": # Prevent Loop 防止套娃
                continue
            type = check_type(self.preset_config[c])
            if type == "dict":
                self[c] = Config(self.preset_config[c], name="dict "+c, read_command_line=False)
            else:
                self[c] = self.preset_config[c]
        self.__setattr__("config_name",name,True)
        self.__setattr__("print_style","both",True)
        if read_command_line:
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
                if key.find(".")>=0:
                    main_key = key.split(".")[0]
                    sub_key = key.split(".")[1]
                    # print("----------", main_key, sub_key, value)
                    self[main_key].__setattr__(sub_key, value)
                else:
                    v = self.convert_type(value, key)
                    self[key] = v
                # print("after convert key-value:", key, v, check_type(v))

    # 把变量v按照preset_config里的相应key对应的值的类型转换为相应类型，用于命令行参数类型转换，同时保证了所有参数必须在preset_config中出现
    # 如preset_config里的random_seed为2022,是一个int类型，则命令行参数如果指定了--random_seed 2013,则会把2013由原始的字符串形式转换为int
    def convert_type(self, v, key):
        try:
            v = str(v)
            if key in self.preset_config.keys():
                type = check_type(self.preset_config[key])
                # print("type is", type)
                if type == "str":
                    variable = v
                elif type == "float" or type == "int":  # 如果是int或者float，转换为相应类型
                    variable = eval(type + "(" + v + ")")
                elif type =="bool":
                    if len(v) == 0:
                        variable = True
                    else:
                        variable = eval(type + "(" + v + ")")
                elif type == "list":
                    # print(v)
                    if v.find("[")>=0:
                        if v.find('"') >=0:
                            v = v.replace('"',"'")
                        variable = eval('eval("%s")' % v)
                    else:
                        print("\033[1;31mCannot convert %s to type %s, make sure you have input a list start with [ and end with ].\n\033[0m" % (str(v), type))
                elif type == "dict":
                    print("\033[1;31mCannot directly parse the whole dict, please use . to spefic the value for the child elements of the dict. \nSuch as, use --nest.a 1 to set the value of 'a' inside dict 'nest' to 1.\n\033[0m")
                else:
                    variable = eval('eval("%s")' % v)
            else:
                print("\033[1;31mThe key '%s' is not exist in your preset configuration dict, please check if you input the correct name.\n\033[0m" % key)
        except:
            if type == "list":
                raise AttributeError("Cannot convert %s to type %s, if your command line value have single/double quote to input strings, please ensure you have an backslash \ before every quote symbol. \nSuch as: --array [1,2.5,\\'msg\\']" % (str(v), type))
            else:
                raise AttributeError("Cannot convert %s to type %s" % (str(v), type))
        # print(variable, check_type(variable))
        # if type == "list" or type == "dict" or type == "tuple":
        #     variable = eval("eval(%s)"%v)
        # else:
        #     variable = eval(type + "('" + v + "')")
        # print(check_type(variable))
        return variable

    def set_print_style(self, style="both"):
        self.__setattr__("print_style",style,True)
        for c in self.preset_config:
            if c == "preset_config": # Prevent Loop 防止套娃
                continue
            type = check_type(self.preset_config[c])
            if type == "dict":
                self[c].set_print_style(style)


    def __str__(self):
        if self.config_name == "":
            print("\nConfigurations:")
        else:
            print("\nConfigurations of %s: " % self.config_name)
        output = PrettyTable(["Key", "Type", "Value"])
        output.align["Value"] = 'l'
        output_json = deepcopy(self.preset_config)
        for key in self.preset_config:
            # output += key + ":" + str(self[key]) + "\n"
            type = check_type(self[key])
            if type != "dict":
                output_json[key] = self[key]
                output.add_row([key, str(check_type(self.preset_config[key])), str(self[key])])
            else:
                output_json[key] = "See below"
                output.add_row([key, str(check_type(self.preset_config[key])), "See sub table below"])
        if self.print_style == "both" or self.print_style == "table":
            print(output)

        if self.print_style == "both" or self.print_style == "json":
            print(output_json)

        for key in self.preset_config:
            type = check_type(self[key])
            if type == "dict":
                print(self[key])

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

    def __setattr__(self, name, value, no_check_type = False):
        if name == "preset_config" or name == "config_name" or name == "print_style" or name in self.preset_config:
            if no_check_type:
                self[name] = value
            else:
                v = self.convert_type(value, name)
                self[name] = v
        else:
            raise AttributeError("Can not set value because the key '%s' is not in preset_config!" % name)
