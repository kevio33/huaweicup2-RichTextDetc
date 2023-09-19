import zipfile

"""
    src_path: 源文件位置
    target_path: 目标位置
"""
def unzip(src_path, target_path):
    # 指定要解压的 Zip 文件路径
    zip_file_path = src_path

    # 指定解压目标目录
    extracted_dir = target_path + '/'

    # 创建一个解压对象
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # 解压到指定目录
        zip_ref.extractall(extracted_dir)

    print(f'已将 {zip_file_path} 解压到 {extracted_dir} 目录中。')
