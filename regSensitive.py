'''
    用来提取铭感信息的正则py
'''
import re

# 定义敏感数据的正则表达式
ip_regex = r"(ip|服务器地址|服务器|ip地址|IP|IP地址)?[:：]?\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  # IP 地址
port2_regex = r"\d{0,5}(port|端口号|端口)[:：]?\d{1,5}" #端口号


username_regex = r"(账号|username|name|用户名|用户|root|admin)[:：]?[^,\n]+"  # 匹配用户名，长度需要确定？可能包含中文字符
password_regex = r"(password|pwd|密码|psw|authorization|authentication|key|secure|salt|密钥|auth)[:：]?[a-zA-Z_0-9,]+"

email_regex = r"(邮箱|email)?[:：]?[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$"
# email_regex = r"^(邮箱|email|邮箱:|email:)?[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$"

http_regex = r"^https?:\/\/([a-z0-9][-a-z0-9]{0,62}(\.[a-z0-9][-a-z0-9]{0,62})+)(:\d+)?(\/\S*)?$"

# 合并所有正则
all_regex = re.compile(f"({ip_regex}|{port2_regex}|{username_regex}|{password_regex}|{email_regex}|{http_regex})")
# all_regex = re.compile(f"({port2_regex})")

'''
    提取敏感词
    可以考虑先找铭感词关键信息，然后通过正则匹配(如果直接每个正则都尝试匹配速度很慢)
'''
def regexSensitive(textLis=[]):
    # resSet = set()
    if len(textLis)==0:
        print('输入为空')
        return []
    matchRes = []
    for text in textLis:
        text = text.lower()
        resLis = all_regex.findall(text)#返回是列表，里面可能有多个匹配tuple
        # print(resLis)
        for tup in resLis:
            # for item in tup:
            #     if item != '':
            #         matchRes.append(item)
            matchRes.append(tup[0])

    return matchRes


if  __name__ == '__main__':
    # mathSensitive('sdsdsd')
    # tex = '今天我们吃什么username:kevinang@qq.com，好啊，kevinang@qq.com'
    # res = re.findall(port2_regex,tex)#返回形式[('33', '端口号', '3434')]
    # res = re.match(ip_regex,tex)#返回形式:1212端口:3434
    # res = re.match(email_regex,tex)

    # re.group()

    texLis = [
                "我们一起去吃饭username:kevin,密码:1223455",
                "http://xxx.xxx.cn:9980/student",
                "我的邮箱是:kevinang@qq.com.cn",
                "学校的ip地址是:192.168.173.10"
              ]
    res = regexSensitive(texLis)
    for i in res:
        print(i)