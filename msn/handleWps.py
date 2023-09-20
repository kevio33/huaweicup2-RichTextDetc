from docx import Document
import re
import os
import re
import win32com.client as win32
import wps


from kevin.handlePic import OCR

# 定义识别敏感词的正则表达式
ip_regex = r"(服务器地址)?\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
port1_regex = r"端口:\d+"
port2_regex = r"[A-Z]{3,} [0-9]{3,6}端口"
username_regex = r"用户名：\w+"
password_regex = r"密码：\w+"
stuId_regex = r"学号：\w{10}"
defaultPwd1_regex = r"默认密码：(?=.*[a-zA-Z])(?=.*\d)(?=.*[@]).{8,16}"
defaultPwd2_regex = r"初始密码为\w{6}"
# picture1_regex = r"服务器\d :"
# picture2_regex = r"端口\d:"
name_regex = r"虚拟专用网名称“\w{4,}”"
sharePwd_regex = r"共享密钥为“\w+”"


# 合并所有正则
all_regex = re.compile(
    f"({ip_regex}|{port1_regex}|{port2_regex}|{username_regex}|{password_regex}|{defaultPwd1_regex}|{sharePwd_regex}|{defaultPwd2_regex}|{stuId_regex}|{name_regex})")

# 路径
current_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_directory, "outputWps.txt")


def handleWps(filePath):
    pass


def save_to_txt(data, output_path):
    with open(output_path, 'r+') as file:  # 文件可读可写模式打开
        content = file.read()
        file.seek(0, 2)  # 使文件指针移动到文件的末尾(追加)
        if content:
            file.write('---------------------------------------\n')
        for item in data:
            file.write(item + '\n')


if __name__== "__main__":
    filePath = "D:\huaweicup\huaweicup2-RichTextDetc\赛题材料\office\222.doc"
    handleWps(filePath)