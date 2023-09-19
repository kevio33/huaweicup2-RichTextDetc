import re


if __name__ == "__main__":
    regex = r"(jdbc:mysql://(localhost:\d{4}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/mydb)"
    str = 'db.url=jdbc:mysql://localhost:3306/mydb'
    #str = 'db.url=jdbc:mysql://192.168.202.2/mydb'
    res = re.findall(regex, str)
    print(res)