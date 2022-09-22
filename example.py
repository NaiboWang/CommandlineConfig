import json
from commandline_config.commandline_config import Config
from copy import deepcopy

# preset_config = {
#     "index": 1, # Index of party
#     "dataset": "mnist",
#     'lr': 0.01, # learning rate
#     'normalization': True,
#     "multi_information":[1,0.5,'test',"TEST"],
#     "nested":{
#         "a":"1",
#         "b":"2",
#         "c":3.0,
#         'd':False,
#         'e':[1,2.2,True,"TEST2"]
#     }
#   }
# c = Config(preset_config)
# c.set_print_style("json")
# # c.lr = "15s"
# # c.index="15sd"
# # c.normalization = False
# # c["multi_information"] = "sdf"
# # c.index = 2.8
# # c["index"] = "3.5s"
# # c.index = "3.5"
# # c.multi_information = [1,"2",'3',["dsf"]]
# # c.multi_information = [1,0,.5]
# print(c)
# print(c.nested.a)
# c.nested.a = "sdf"
# print(c.nested.a)
# c.nested["a"] = "sdf2"
# print(c.nested["a"])
# c["nested"].a = "sdf3"
# print(c["nested"].a)
# c["nested"]["a"] = "sdf4"
# print(c["nested"]["a"])

# c.nested.c = "15.6"
# print(c)


preset_config = {
    "index": 1,  # Index of party
    "dataset": "mnist",
    'lr': 0.01,  # learning rate
    'normalization': True,
    # 'msg_config': {
    #     "test": "ttt",
    # },
    "multi_information": [1, 0.5, 'test', "TEST"],  # list
    "dbinfo": {
        "username": "NUS",
        "password": 123456,
        "retry_interval_time": 5.5,
        "save_password": False,
        "certificate_info": ["1", 2, [3.5]]
    }
}
advanced_options = {
    'lr': {
        "enum": [0.001, 15.5, 0.01, 0.1]  # 限制lr值只能取0.001，15.5，0.01，0.1中的一个
    },
    'index': {
        "enum": [1, 2, 3]  # 限制index值只能设置为1，2和3
    },
    "dbinfo": {
        "username": {
            "enum": ["XDU", "ZJU", "NUS"]  # 限制dbinfo.username字段只能输入XDU，ZJU和NUS
        }
    },
}

helpers = {
    "index": "index of information",
    "dbinfo_help": "information dict for database",
    "dbinfo": {
        "username": "username for database",
    }
}

config_with_name = Config(
    preset_config, name="Federated Learning Experiments", options=advanced_options, helpers=helpers)
config_with_name.help()

# config_with_name.index = "5.5"
config_with_name.dataset = "[]"
config_with_name.lr = "15.5"
config_with_name.normalization = True
config_with_name.multi_information = [2, 'sd', 'sdfdsf']
config_with_name["dataset"] = "sdf"
# config_with_name.dbinfo.username = "sdfasd"
# config_with_name.dbinfo.password = "1"
# config_with_name.sdf = 1
config_with_name.dbinfo.retry_interval_time = "22"
config_with_name.dbinfo.save_password = False
config_with_name.dbinfo.certificate_info = [1, [], [[2]]]

print(config_with_name.dbinfo.certificate_info[2][0][0])

print(config_with_name)
config_with_name.set_print_style('json')
print(config_with_name)
print("----------")
config_with_name.set_print_style('table')
print(config_with_name)

# def print_dataset_name(c):
#   c.dbinfo.certificate_info = [3]
#   print(c.dataset, c["dataset"], c.dbinfo.certificate_info)

# print_dataset_name(c=config_with_name)
# copy_config = deepcopy(config_with_name)
# copy_config.dbinfo.password=456456
# print(copy_config, config_with_name)
print(config_with_name.get_config())
with open("configuration.json", "w") as f:
    configuration = config_with_name.get_config()
    print(configuration)
    json.dump(configuration, f)
