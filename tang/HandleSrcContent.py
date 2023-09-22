import os
import re
from utils import unzip
from regSensitive import regexSensitive

class HandleSrcContent(object):
    def __init__(self,fileName,filePath):
        self.file_list = []
        # self.cur_path = os.path.dirname(os.path.abspath(__file__))
        # print(self.cur_path)
        
        # self.root_path = os.path.dirname(self.cur_path)
        # print(self.root_path)
        rootPath = os.path.abspath(__file__)
        rootPath = rootPath[:-19] #父目录
        self.current_path = rootPath
        self.file_path = filePath
        self.file_name = fileName

    def unzip(self) -> None:
        # target_path = self.root_path + "/赛题材料" + "/包含敏感信息的源码"
        target_path = os.path.dirname(self.file_path)#解压到原目录
        # path_list = []
        # self.get_all_zips(target_path, path_list)
        # print(path_list)
        # for path in path_list:
        #     unzip.unzip(path, '.')
        unzip.unzip(self.file_path,target_path)
        self.unzip_path = target_path+'\\'+self.file_name[:-4]#保存解压后文件的地址

    

    #递归遍历下面文件
    def get_cur_dir(self):
        for item in os.listdir(self.unzip_path):
            if os.path.isdir(item):
                self.get_all_files(item)
    #遍历所有文件
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
        self.unzip()
        self.get_all_files(self.unzip_path)
        # self.get_all_files('E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\包含敏感信息的源码\python_fasts3-main')

        res_txt = {}
        for file in self.file_list:
            # print(file)
            filename = file.split('\\')[-1]
            # suffix = file.split('\\')[-1].split('.')[-1]
            suffix = filename.split('.')[-1]           
            # res.add(suffix)
            # if suffix == 'py':
            #     self.handle_py_file(file)
            # else:
            #     # file = open(file,'r',encoding='utf-8')
            #     lis = []
            #     for lines in file.readlines():
            #         lis.append(lines)
            #     res = regexSensitive(lis)
            #     res_txt[filename] = res
            #     # file.close()
            reg_lis = []
            try:
                file = open(file,'r')
                for lines in file.readlines():
                    reg_lis.append(lines.strip())
                res = regexSensitive(reg_lis)
                res_txt[filename] = res
                file.close()
            except Exception:
                res_txt[filename] = Exception
        fwrite = open(self.current_path+'src_output.txt','w',encoding='utf-8')
        fwrite.write(str(res_txt))
        fwrite.close()
        # return reg_lis

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
    import sys
    sys.path.append(r'..')
    from regSensitive import regexSensitive
    # # from utils.unzip import unzip
    class1 = HandleSrcContent('python_fasts3-main.zip',r'E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\包含敏感信息的源码\python_fasts3-main.zip')
    # class1.unzip()
    # class1.get_all_files('E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\包含敏感信息的源码\python_fasts3-main')
    # print(class1.file_list)
    class1.handle_file()
    