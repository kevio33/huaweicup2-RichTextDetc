import os
import re
import win32com.client as win32
from docx import Document




# from kevin.handlePic import OCR

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


# .doc转.docx
def convert_doc_to_docx(doc_file, docx_file):
    # 创建一个新的.docx文件
    docx_document = Document(doc_file)
    # 读取.doc文件的内容
    with open(doc_file, 'rb') as doc:
        content = doc.read()
        byte_data = bytes.fromhex(str(content))
        content_utf_8 = byte_data.decode('utf-8')
        # content_utf_8 = bytes(content, encoding = "utf-8").decode()
    # 将.doc文件的内容写入.docx文件
    docx_document.add_paragraph(str(content_utf_8))
    # 保存.docx文件
    docx_document.save("save.docx")
    # 将.doc文件转换为.docx文件


def readWord(filePath):
    word = win32.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(filePath)
    text = doc.Content.Text
    doc.Close()
    word.Quit()
    return text


def handleWord(file_name, file_path):
    text = readWord(file_path)
    # 读取文档中的所有段落并匹配敏感信息
    sensitive_data = re.findall(all_regex, text)
    if isinstance(sensitive_data, list):   # 可能得到元组列表，先转换成字符串列表，不然file.write报错
        sensitive_data = ' '.join([' '.join(t) for t in sensitive_data])   # 转换成一整个字符串
        sensitive_data = sensitive_data.split()  # 按空格切割data，转变成列表，方便保存
    # 保存路径
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_directory, "{}.txt".format(file_name))
    # 保存文件
    save_to_txt(sensitive_data, output_path, file_name)


def save_to_txt(data, output_path, file_name):
    dict = {}
    with open(output_path, 'w') as file:
        # for item in data:
        #     file.write(item + '\n')
        dict[file_name] = data
        file.write(str(dict) + '\n')


# if __name__ == "__main__":
#     # 示例
#      handleWord('Android手机VPN安装指南.doc', 'D:\huaweicup\huaweicup2-RichTextDetc\赛题材料\office\Android手机VPN安装指南.doc')
#     # text = handleWord(word_path)

    