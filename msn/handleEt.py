import os
import xlrd


def readEt(file_path):
    wb = xlrd.open_workbook(file_path)
    # 读取文件内容
    mappinglist = []
    for x in range(3):  # 循环识别3个工作表
        sheet = wb.sheet_by_index(x)
        column_names = []
        for cell in sheet[0]:  # 遍历第一行
            column_names.append(cell.value)  # 保存第一行的列名
        columnnamecell = sheet[0]  # 获取第一排的所有cell
        columnname = [y.value for y in columnnamecell]  # 字段在excel中的行数列表

        for rownum in range(1, sheet.nrows):
            mapping = {}
            for x in column_names:
                index_num = columnname.index(x)   # excel索引和数组索引差1
                mapping[x] = sheet.cell(rownum, index_num).value
            mappinglist.append(mapping)

    return mappinglist


def handleEt(file_name, file_path):
    lis = readEt(file_path)
    #路径
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_directory, "{}.txt".format(file_name))
    save_to_txt(str(lis), output_path, file_name)


def save_to_txt(data, output_path, file_name):
    dict = {}
    with open(output_path, 'w') as file:
        dict[file_name] = data
        file.write(str(dict) + '\n')


# if __name__ == '__main__':
#     handleEt('资产梳理.et', 'D:\huaweicup\huaweicup2-RichTextDetc\赛题材料\wps\资产梳理.et')