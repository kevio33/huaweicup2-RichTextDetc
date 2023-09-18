import os
import re
import regSensitive


'''
    处理txt文件
'''


def read_file_line_by_line(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line.strip()  # 返回每行内容，并去掉末尾的换行符
                sensitive = regSensitive.mathSensitive(line)
    except FileNotFoundError:
        print(f"文件 '{file_path}' 不存在.")
    except Exception as e:
        print(f"发生错误: {e}")



'''
    写入提取信息
'''


def save_to_txt(data, output_path):
    # 原代码
    # with open(output_path, 'a',encoding='utf-8') as file:
    #     for item in data:
    #         file.write(item[0] + '\n')

    with open(output_path, 'w', encoding='utf-8') as file:
        for item in data:
            # 如果本身换行符不需要再加换行符
            if item != '\n':
                file.write(item[0] + '\n')
            else:
                file.write(item[0])


def read_files_in_directories(root_dir):
    all_files = []  # 用来存储所有文件的内容

    # 遍历所有目录和文件
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            read_file_line_by_line(file_path)



# 使用示例
root_directory = 'D:\sundries\huaweiCup\contentCheck\huaweicup2-RichTextDetc\赛题材料\linux'  # 替换成实际的目录路径
files_content = read_files_in_directories(root_directory)

