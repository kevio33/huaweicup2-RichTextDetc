import utils.unzip
import os


# # 获取当前文件的绝对路径
# current_file_path = os.path.abspath(__file__)
# # 获取当前文件所在目录的上级目录
# parent_directory = os.path.dirname(os.path.dirname(current_file_path))
#
# print(parent_directory)
# src_path = parent_directory + '\赛题材料\包含敏感信息的源码\python_fasts3-main.zip'
#
# utils.unzip.unzip(src_path, '.')


def get_all_files(directory, file_list):
    # 遍历当前目录下的所有文件和文件夹
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        # 如果是文件，将其添加到列表中
        if os.path.isfile(item_path):
            file_list.append(item_path)
        # 如果是文件夹，递归调用函数继续处理
        elif os.path.isdir(item_path):
            get_all_files(item_path, file_list)


if __name__ == '__main__':
    # 初始化一个列表用于存储文件路径
    file_list = []
    print(os.getcwd())
    lists = os.listdir(os.getcwd())
    for item in lists:
        # print(item)
        if os.path.isdir(item):
            get_all_files(item, file_list)
    # 调用函数开始遍历文件夹
    # get_all_files('./', file_list)

    # 输出文件列表
    for file_path in file_list:
        print(file_path)
