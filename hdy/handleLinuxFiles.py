import os
import regSensitive

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
    #全文敏感的文件名
    special_file_names = {
        'id_rsa',
        'id_rsa.pub',
        'authorized_keys'
    }

    # 尝试匹配敏感词
    directory_path = 'D:\sundries\huaweiCup\contentCheck\huaweicup2-RichTextDetc\赛题材料\linux'
    output_file = 'output.txt'

    files = get_file_list(directory_path)
    write_files_to_txt(files, output_file, special_file_names)
