'''
    用来提取铭感信息的正则py
'''
import re

# 定义敏感数据的正则表达式
ip_regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"  # IP 地址
username_regex = r"\b[a-zA-Z0-9._-]{3,16}\b"  # 常见的用户名格式
password_regex = r"^(?=.+[A-Z])(?=.+[a-z])(?=.+\d)(?=.+[\W_]).{8,}$"

# 通常密码要求最少8个字符
email_regex = r"\S*(?=\S{8,})(?=\S*[A-Z])(?=\S*[a-z])(?=\S*[!@#$%^&*?])\S*"  # 邮箱格式
minganword_regex = r"(.*)(研发|邮箱)(.*)"  #研发、邮箱
port1_regex = r"端口:\d+"
port2_regex = r"[A-Z]{3,} [0-9]{3,6}端口"

# 合并所有正则
all_regex = re.compile(f"({ip_regex}|{email_regex}|{username_regex}|{password_regex}|{minganword_regex})")



'''
    提取铭感词
'''
def mathSensitive():
    pass