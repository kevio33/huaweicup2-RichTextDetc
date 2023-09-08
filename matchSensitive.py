'''
    用来匹配敏感信息
    给定输入数据，将匹配到的敏感信息以map形式返回
'''

import yaml

yamlPath = 'sensitiveWord.yml'

f = open(yamlPath, 'r', encoding='utf-8')
cfg = f.read()
d = yaml.load(cfg,Loader=yaml.FullLoader)  # 用load方法转字典
print(d['sensitive_word'])
