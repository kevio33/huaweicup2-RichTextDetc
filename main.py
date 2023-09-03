'''
项目启动项
1.负责启动项目界面(最后的工程了)
2.解压缩文件(将压缩文件放到本目录下)
3.读取所有文件的内容，并提取敏感信息
'''
import os
import rarfile


# 解压缩文件
def unzipFile():

    # 打开 RAR 文件
    rar = rarfile.RarFile('题目1：富文本敏感信息泄露检测.rar')

    # 解压缩文件到指定路径
    rar.extractall()

    # 关闭 RAR 文件
    rar.close()



if __name__ == "__main__":
    unzipFile() #解压缩文件
    






