import os
import re
from docx import Document

# 定义识别敏感词的正则表达式
ip_regex = r"(服务器地址)?\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  # 匹配1-3个数字
port1_regex = r"端口:\d+"  # 1-多个数字
port2_regex = r"[A-Z]{3,} [0-9]{3,6}端口"  # 最少3个字母，3-6个数字
username_regex = r"用户名：\w+"  # a-z A-Z 数字(+代表可以出现多次)
password_regex = r"密码：\w+"
stuId_regex = r"学号：\w{10}"
defaultPwd1_regex = r"默认密码：(?=.*[a-zA-Z])(?=.*\d)(?=.*[@]).{8,16}"#
defaultPwd2_regex = r"初始密码为\w{6}"  # 出现6次，没有+代表固定次数
name_regex = r"虚拟专用网名称“\w{4,}”"
sharePwd_regex = r"共享密钥为“\w+”"


# 合并所有正则
all_regex = re.compile(
    f"({ip_regex}|{port1_regex}|{port2_regex}|{username_regex}|{password_regex}|{defaultPwd1_regex}|{sharePwd_regex}|{defaultPwd2_regex}|{stuId_regex}|{name_regex})")

# 路径
current_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_directory, "outputWordx.txt")


def handleWordx(filePath):
    docx = Document(filePath)
    sensitive_data = []
    for para in docx.paragraphs:
        word = re.match(all_regex, para)
        sensitive_data.append(word.group())
    # 读取文档中的所有段落并匹配敏感信息
    # sensitive_data = re.findall(all_regex, text)
    # if isinstance(sensitive_data, list):   # 可能得到元组列表，先转换成字符串列表，不然file.write报错
    #     sensitive_data = ' '.join([' '.join(t) for t in sensitive_data])   # 转换成一整个字符串
    #     sensitive_data = sensitive_data.split()  # 按空格切割data，转变成列表，方便保存

    save_to_txt(sensitive_data, output_path)


def save_to_txt(data, output_path):
    with open(output_path, 'r+') as file:   # 文件可读可写模式打开
        content = file.read()
        file.seek(0, 2)   # 使文件指针移动到文件的末尾(追加)
        if content:
            file.write('---------------------------------------\n')
        for item in data:
            file.write(item + '\n')


if __name__ == "__main__":
    # 示例
    word_path = r'D:\huaweicup\huaweicup2-RichTextDetc\赛题材料\wps\Android手机VPN安装指南.docx'

    # print(handleWord(word_path))
    text = handleWordx(word_path)
