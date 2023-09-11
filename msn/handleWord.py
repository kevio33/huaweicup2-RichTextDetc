import os
import re
from docx import Document

# 定义识别敏感词的正则表达式
ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
port1_regex = r"端口:\d+"
port2_regex = r"[A-Z]{3,} [0-9]{3,6}端口"
username_regex = r"用户名：\w+"
password_regex = r"密码：\w+"
defaultPassword_regex = r"默认密码：\w+"

# 合并所有正则
all_regex = re.compile(
    f"({ip_regex}|{port1_regex}|{port2_regex}|{username_regex}|{password_regex}|{defaultPassword_regex})")

# 路径
current_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_directory, "outputWord.txt")


def handleWord(filePath):
    doc = Document(filePath)
    text = ' '.join([para.text for para in doc.paragraphs])
    return re.findall(all_regex, text)


def save_to_txt(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(item[0] + '\n')


if __name__ == "__main__":
    # 示例
    word_path = "D:\huaweicup\huaweicup2-RichTextDetc\赛题材料\office\Android手机VPN安装指南.doc"

    data = []
    data.extend(handleWord(word_path))

    save_to_txt(data, output_path)
