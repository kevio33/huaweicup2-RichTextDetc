import os
import re
from openpyxl import load_workbook


# 定义识别敏感词的正则表达式
ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#port_regex = r"端口:\d+"
username_regex = r"用户名：\w+"
password_regex = r"密码：\w+"

# 合并所有正则
all_regex = re.compile(f"({ip_regex}|{username_regex}|{password_regex})")

def handleExcel(fileName,filePath):
    sensitive_columns = ["用户名", "设备地址", "密码"]
    wb = load_workbook(filePath)
    sheet = wb.active

    # 获取列名和对应的索引
    col_indices = {}
    for col_num, col_cells in enumerate(sheet.iter_cols(values_only=True)):
        if col_cells[0] in sensitive_columns:
            col_indices[col_cells[0]] = col_num

    sensitive_data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):  # 从第2行开始，因为第1行是列名
        for col_name, col_num in col_indices.items():
            sensitive_data.append(row[col_num])

    save_to_txt(sensitive_data,"output.txt")


def save_to_txt(data, output_path):
    with open(output_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')
