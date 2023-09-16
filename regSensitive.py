'''
    用来提取铭感信息的正则py
'''
import re

# 定义敏感数据的正则表达式
ip_regex = r"(ip|服务器[地址]*)?([:]?)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # IP 地址
port2_regex = r"([0-9]{1,5})?(port|端口[号]?)([:]?)([0-9]{1,5})?" #端口号


username_regex = r"(username|name|用户[名]?)([:]?)(.{3,16})"  # 匹配用户名，长度需要确定？可能包含中文字符
password_regex = r"(password|pwd|密码|psw|authorization|authentication|key|secure|salt|密钥)([:]?)([a-zA-Z0-9]*)"


# email_regex = r"\S*(?=\S{8,})(?=\S*[A-Z])(?=\S*[a-z])(?=\S*[!@#$%^&*?])\S*"  # 邮箱格式
email_regex = r"(邮箱|email)([:]?)([a-zA-Z0-9_.+-]+)(@)([a-zA-Z0-9-]+)(\.)([a-zA-Z]{2,6})"# ^ 表示字符串的开头 $ 表示字符串的结尾[a-zA-Z0-9_.+-] 表示任意字母、数字、下划线、句点、加号或减号@ 表示 @ 符号[a-zA-Z0-9-]+ 表示任意数量的字母、数字或连字符;\.[a-zA-Z]{2,6} 表示一个 . 符号后面跟着 2 到 6 个字母
# minganword_regex = r"(.*)(研发|邮箱)(.*)"  #研发、邮箱
# port1_regex = r"端口:\d+"


# 合并所有正则
# all_regex = re.compile(f"({ip_regex}|{email_regex}|{username_regex}|{password_regex}|{minganword_regex})")
all_regex = re.compile(f"({ip_regex}|{port2_regex}|{username_regex}|{password_regex}|{email_regex})")


'''
    提取铭感词
    可以考虑先找铭感词关键信息，然后通过正则匹配(如果直接每个正则都尝试匹配速度很慢)
'''
def mathSensitive(textLis=[]):
    if len(textLis)==0:
        print('输入为空')
        return []
    matchRes = []
    for text in textLis:
        resLis = all_regex.findall(text)#返回是列表，里面可能有多个匹配tuple
        for tup in resLis:
            joinText = "".join(tup)
            matchRes.append(joinText)
    return matchRes


if  __name__ == '__main__':
    # mathSensitive('sdsdsd')
    # tex = '今天我们吃什么username:kevinang@qq.com，好啊，kevinang@qq.com'
    # res = re.findall(port2_regex,tex)#返回形式[('33', '端口号', '3434')]
    # res = re.match(ip_regex,tex)#返回形式:1212端口:3434
    # res = re.match(email_regex,tex)

    # re.group()

    texLis = ["今天我们吃什么username:kevinIo33，好啊，kevinang@qq.com",
              "我的邮箱是:kevinang@qq.com",
              "学校的ip地址是:192.168.173.10"
              ]
    res = mathSensitive(texLis)
    for i in res:

        print(i)