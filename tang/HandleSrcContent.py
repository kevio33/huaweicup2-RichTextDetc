import os
import re
from utils import unzip


class HandleSrcContent(object):
    def __init__(self):
        self.file_list = []
        self.cur_path = os.path.dirname(os.path.abspath(__file__))
        self.root_path = os.path.dirname(self.cur_path)
        self.file_list = []

    def unzip(self) -> None:
        target_path = self.root_path + "/赛题材料" + "/包含敏感信息的源码"
        path_list = []
        self.get_all_zips(target_path, path_list)
        print(path_list)
        for path in path_list:
            unzip.unzip(path, '.')

    def get_cur_dir(self):
        for item in os.listdir(self.cur_path):
            if os.path.isdir(item):
                self.get_all_files(item)

    def get_all_files(self, directory):
        # 遍历当前目录下的所有文件和文件夹
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            # 如果是文件，将其添加到列表中
            if os.path.isfile(item_path):
                self.file_list.append(item_path)
            # 如果是文件夹，递归调用函数继续处理
            elif os.path.isdir(item_path):
                self.get_all_files(item_path)

    def get_all_zips(self, directory, file_list):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                if item.split('.')[-1] == 'zip':
                    file_list.append(item_path)
            elif os.path.isdir(item_path):
                self.get_all_zips(item_path, file_list)

    def handle_file(self):
        res = set()
        for file in self.file_list:
            # print(file)
            suffix = file.split('\\')[-1].split('.')[-1]
            res.add(suffix)
            if suffix == 'py':
                self.handle_py_file(file)
        return res

    @staticmethod
    def handle_py_file(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        print(content)
        # 编译正则表达式模式
        port_pattern = re.compile(r"\b\d{1,5}\b")

        # 使用 findall() 查找匹配的端口号
        ports = port_pattern.findall(content)

        # 打印匹配到的端口号
        for port in ports:
            print("Port:", port)


if __name__ == '__main__':
    class1 = HandleSrcContent()
    # class1.unzip()
    class1.get_cur_dir()

    # print(class1.file_list)
    print(class1.handle_file())
