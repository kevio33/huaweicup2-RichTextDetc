import json
import os
import re

# 定义敏感数据的正则表达式
ip_regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"  # IP 地址
username_regex = r"\b[a-zA-Z0-9._-]{3,16}\b"  # 常见的用户名格式
password_regex = r"^(?=.+[A-Z])(?=.+[a-z])(?=.+\d)(?=.+[\W_]).{8,}$"

# 通常密码要求最少8个字符
email_regex = r"\S*(?=\S{8,})(?=\S*[A-Z])(?=\S*[a-z])(?=\S*[!@#$%^&*?])\S*"  # 邮箱格式
minganword_regex = r"(.*)(研发|邮箱)(.*)"  #研发、邮箱


# 合并所有正则
all_regex = re.compile(f"({ip_regex}|{email_regex}|{username_regex}|{password_regex}|{minganword_regex})")

# 路径
current_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_directory, "outputTxt.txt")


def handleTxt(file_name, file_path):
    result = handle_txt(file_path)
    # 路径
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_directory, '{}.txt'.format(file_name))
    save_to_txt(result, output_path, file_name)  # 保存结果


    '''
        处理txt文件
    '''
def handle_txt( file_path):   #处理txt文件通用方法

    # 原代码
    # with open(filePath, 'r',encoding='utf-8') as file:
    #     content = file.read()
    #     # print(content)
    #     sensitive_data = re.findall(all_regex, content)
    #     current_directory = os.path.dirname(os.path.abspath(__file__))
    #     output_path = os.path.join(current_directory, "outputTxt.txt")
    #     save_to_txt(sensitive_data, output_path)
    # isR = True # 是否是换行符号
    readRes =[] # 因为读取的结果是一个列表，所有定义列表保存所有读取结果
    for line in open(file_path, 'r', encoding='utf-8'):
        # print(line) 
        if line != '\n':
            sensitive_data = re.findall(all_regex, line)
            readRes.extend(sensitive_data)
            # isR = True
        # else:# 如果是换行符，直接写入文件，不进行正则匹配
        #     if isR is True:
        #         readRes.extend(line)
        #         isR = False
    return readRes


'''
    写入提取信息
'''
def save_to_txt(data, output_path, file_name):
    dict = {}
    content = []
    for item in data:
        content.append(item[0])
    dict[file_name] = content
    with open(output_path, 'w') as file:
        file.write(str(dict) + '\n')

    # with open(output_path, 'w') as file:
    #     for item in data:
    #         # 如果本身换行符不需要再加换行符
    #         if item != '\n':
    #             file.write(item[0] + '\n')
    #         else:
    #             file.write(item[0])
    # dict = {}
    # with open(output_path, 'w') as file:
    #     # for item in data:
    #     #     file.write(item + '\n')
    #     dict[file_name] = data
    #     file.write(str(dict) + '\n')

# 测试使用
# if __name__ == "__main__":
#     handleTxt('环境信息.txt', 'D:\huaweicup\huaweicup2-RichTextDetc\赛题材料\环境信息.txt')