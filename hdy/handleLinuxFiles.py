import os
import regSensitive


class LinuxFilesHandler:
    # 类属性，用来存储不需要特殊处理的文件名集合
    no_need_to_handle_file = {
        'id_rsa',
        'id_rsa.pub',
        'authorized_keys'
    }

    def __init__(self, directory, output_file):
        self.directory = directory
        self.output_file = output_file

    def get_file_list(self):
        file_list = []
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    def write_files_to_txt(self):
        with open(self.output_file, 'w') as file:
            for file_path in self.get_file_list():
                file_name = os.path.basename(file_path)
                with open(file_path, 'r') as f:
                    content = f.read()
                    if file_name in self.no_need_to_handle_file:
                        file.write(f'File Name: {file_name}\n')
                        file.write(f'Content:\n{content}\n\n')
                    else:
                        sensitive = regSensitive.regexSensitive(content)
                        file.write(f'File Name: {file_name}\n')
                        file.write(f'Content:\n{sensitive}\n\n')



def get_file_list(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def write_files_to_txt(file_list, output_file, no_need_to_handle_file):
    with open(output_file, 'w') as file:
        for file_path in file_list:
            if os.path.basename(file_path) in no_need_to_handle_file:
                with open(file_path, 'r') as f:
                    content = f.read()
                    file_name = os.path.basename(file_path)
                    file.write(f'File Name: {file_name}\n')
                    file.write(f'Content:\n{content}\n\n')
            else:
                with open(file_path, 'r') as f:
                    content = f.read()
                    sensitive = regSensitive.regexSensitive(content)
                    file_name = os.path.basename(file_path)
                    file.write(f'File Name: {file_name}\n')
                    file.write(f'Content:\n{sensitive}\n\n')






if __name__ == "__main__":

    # 尝试匹配敏感词
    directory_path = 'D:\sundries\huaweiCup\contentCheck\huaweicup2-RichTextDetc\赛题材料\linux'
    output_file = 'output.txt'

    handler = LinuxFilesHandler(directory_path, output_file);
    handler.write_files_to_txt();
